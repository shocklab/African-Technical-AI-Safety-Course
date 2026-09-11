#!/usr/bin/env python3
"""Rebuild the course's read-only notebook pages without executing cells.

Requires nbconvert and nbformat. Run from any directory; the existing page wrapper
and navigation are retained, while the notebook body is generated from the ipynb.
"""
from pathlib import Path
import copy
import re
from urllib.parse import unquote
from html import escape
import nbformat
from nbconvert import HTMLExporter

ROOT = Path(__file__).resolve().parents[1]

def render(path):
    notebook = nbformat.read(path, as_version=4)
    nbformat.validate(notebook)
    notebook = copy.deepcopy(notebook)
    if notebook.cells and notebook.cells[0].cell_type == 'markdown':
        # The course page wrapper already supplies the title.
        notebook.cells[0].source = re.sub(r'^# [^\n]+\n+', '', notebook.cells[0].source, count=1)
    exporter = HTMLExporter(template_name='basic')
    exporter.exclude_input_prompt = True
    exporter.exclude_output_prompt = True
    body, _ = exporter.from_notebook_node(notebook)
    # nbconvert percent-encodes some Unicode heading IDs as well as their hrefs.
    # Keep IDs as text so decoded URL fragments resolve to the actual heading.
    body = re.sub(r'id="([^"]+)"',
                  lambda m: 'id="' + escape(unquote(m.group(1)), quote=True) + '"', body)
    page = path.with_suffix('.html')
    old = page.read_text()
    # Notebook Markdown uses dollar delimiters as well as the course's TeX delimiters.
    old = old.replace(r"inlineMath:[['\\(','\\)']]",
                      r"inlineMath:[['$','$'],['\\(','\\)']]")
    old = old.replace(r"displayMath:[['\\[','\\]']]",
                      r"displayMath:[['$$','$$'],['\\[','\\]']]")
    marker = '    <div class="notebook">'
    start = old.index(marker) + len(marker)
    end = old.index('    <nav class="page-nav">', start)
    # Replace the notebook container's contents and closing tag, preserving navigation.
    page.write_text(old[:start] + '\n' + body + '\n    </div>\n' + old[end:])
    return page

if __name__ == '__main__':
    for path in sorted((ROOT / 'docs/labs').glob('*.ipynb')):
        print(render(path).relative_to(ROOT))
