from typing import List

from roam_data.roam.graph import Block
from markdown_builder.document import MarkdownDocument


def merge_retros(rb: List[Block]):
    rr = [[],[],[]]
    for retro in rb:
        for i in range(3):
            block =retro.children[i]
            rr[i]+=block.children
    return rr


def append_block_to_markdown(block: Block, doc: MarkdownDocument, level=0):
    doc.append_bullet(block.string, level)
    for child in block.children:
        append_block_to_markdown(child, doc, level + 1)

