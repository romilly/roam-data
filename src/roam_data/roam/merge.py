from typing import List

from roam_data.roam.graph import Block


def merge_retros(rb: List[Block]):
    rr = [[],[],[]]
    for retro in rb:
        for i in range(3):
            block = retro.children[i]
            rr[i] += block.children
    return rr
