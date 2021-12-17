from typing import List

from roam_data.roam.graph import Block
from markdown_builder.document import MarkdownDocument


def append_block_to_markdown(block: Block, doc: MarkdownDocument, level=0):
    doc.append_bullet(block.string, level)
    for child in block.children:
        append_block_to_markdown(child, doc, level + 1)


def retro_blocks_to_markdown(rr: List[Block]):
    doc = MarkdownDocument()
    headings = ['[WW]','[WDNW]','[WDD]']
    for (i, heading) in enumerate(headings):
        doc.append_heading(heading)
        for block in rr[i]:
            append_block_to_markdown(block, doc)
    with open('retro.md','w') as md:
        md.write(doc.contents())
    doc.close()