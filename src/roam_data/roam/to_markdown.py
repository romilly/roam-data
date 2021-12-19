from typing import List

from roam_data.roam.graph import Block, Entry
from markdown_builder.document import MarkdownDocument


def append_entry_to_markdown(entry: Entry, doc: MarkdownDocument, level=0):
    doc.append_bullet(entry.text(), level)
    for child in entry.children:
        append_entry_to_markdown(child, doc, level + 1)

# TODO: move this back to pip, along with the retro stuff in filter-entries


def retro_blocks_to_markdown(rr: List[Block]):
    doc = MarkdownDocument()
    headings = ['[WW]','[WDNW]','[WDD]']
    for (i, heading) in enumerate(headings):
        doc.append_heading(heading)
        for block in rr[i]:
            append_entry_to_markdown(block, doc)
    with open('retro.md','w') as md:
        md.write(doc.contents())
    doc.close()