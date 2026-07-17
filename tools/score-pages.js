#!/usr/bin/env node
/**
 * Score every course page for AI-writing tells.
 *
 * Uses the detection engine from conorbronsdon/avoid-ai-writing (MIT), vendored
 * in tools/aiwriting-detector/patterns.js. Extracts the lesson prose from each
 * page (the .content block, tags stripped) and runs it through analyzeText().
 *
 * Usage:  node tools/score-pages.js docs
 */
const fs = require('fs');
const path = require('path');

const M = require(path.join(__dirname, 'aiwriting-detector', 'patterns.js'));
const analyze =
  M.analyzeText ||
  (M.default && M.default.analyzeText) ||
  (M.AIDetector && M.AIDetector.analyzeText) ||
  (typeof M === 'function' ? M : null);

if (!analyze) {
  console.error('Could not find analyzeText(). Module exports:', Object.keys(M));
  process.exit(1);
}

function walk(dir, out = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) walk(p, out);
    else if (e.name.endsWith('.html')) out.push(p);
  }
  return out;
}

function proseOf(file) {
  const h = fs.readFileSync(file, 'utf8');
  const m =
    h.match(/<div class="content">([\s\S]*?)<!-- PAGE-NAV/) ||
    h.match(/<div class="content">([\s\S]*)/);
  let b = m ? m[1] : '';
  b = b.replace(/<script[\s\S]*?<\/script>/g, '').replace(/<style[\s\S]*?<\/style>/g, '');
  b = b.replace(/<[^>]+>/g, ' ');
  b = b
    .replace(/&nbsp;/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/&mdash;/g, '—')
    .replace(/&ndash;/g, '–')
    .replace(/&rsquo;|&lsquo;/g, "'")
    .replace(/&ldquo;|&rdquo;/g, '"')
    .replace(/&[a-z]+;/g, ' ');
  return b.replace(/\s+/g, ' ').trim();
}

const root = process.argv[2] || 'docs';
const files = walk(root).sort();
const rows = [];

for (const f of files) {
  const t = proseOf(f);
  const words = t ? t.split(' ').length : 0;
  if (words < 80) continue; // skip nav-only / stub pages
  let r;
  try {
    r = analyze(t);
  } catch (e) {
    console.error('ERROR scoring', f, '->', e.message);
    continue;
  }
  const byType = {};
  for (const i of r.issues || []) byType[i.type || i.category || 'unknown'] = (byType[i.type || i.category || 'unknown'] || 0) + 1;
  rows.push({
    f: path.relative(root, f),
    score: r.score,
    label: r.label,
    words,
    nIssues: (r.issues || []).length,
    byType,
  });
}

rows.sort((a, b) => b.score - a.score);
const mean = rows.reduce((s, r) => s + r.score, 0) / rows.length;

console.log(`pages scored: ${rows.length}`);
console.log(`mean AI-tell score: ${mean.toFixed(1)} / 100  (higher = more AI-like)`);
const buckets = {};
for (const r of rows) buckets[r.label] = (buckets[r.label] || 0) + 1;
console.log('labels:', JSON.stringify(buckets));

console.log('\n=== WORST 15 PAGES ===');
for (const r of rows.slice(0, 15))
  console.log(`  ${String(r.score).padStart(3)}  ${String(r.label).padEnd(9)} ${String(r.nIssues).padStart(3)} issues  ${r.f}`);

console.log('\n=== BEST 5 PAGES ===');
for (const r of rows.slice(-5))
  console.log(`  ${String(r.score).padStart(3)}  ${String(r.label).padEnd(9)} ${String(r.nIssues).padStart(3)} issues  ${r.f}`);

const agg = {};
for (const r of rows) for (const [k, v] of Object.entries(r.byType)) agg[k] = (agg[k] || 0) + v;
console.log('\n=== TOP ISSUE CATEGORIES SITE-WIDE ===');
Object.entries(agg)
  .sort((a, b) => b[1] - a[1])
  .slice(0, 25)
  .forEach(([k, v]) => console.log(`  ${String(v).padStart(4)}  ${k}`));

fs.writeFileSync(
  path.join(__dirname, 'score-baseline.json'),
  JSON.stringify({ mean, rows }, null, 2)
);
console.log('\nbaseline written to tools/score-baseline.json');
