import tkinter as tk
from enum import Enum
from sequence_area import SequenceArea
from block import Block
from block_types import *


class BlockTypes(Enum):
    TEST_ONE = "Test Block One"
    TEST_TWO = "Test Block Two"
    TEST_THREE = "Test Block Three"


# networktables will configure this for us eventually and we will build this dynamically

template_blocks = [
    (BlockTypes.TEST_ONE, "blue"),
    (BlockTypes.TEST_TWO, "blue"),
    (BlockTypes.TEST_THREE, "blue")
]

# template_blocks = [
#     (TestBlockOne())
# ]

root = tk.Tk()
root.geometry("800x400")
root.title("Configurable Autonomous Program Builder")

# template boxes live here
palette = tk.Frame(root, width=450, bg="#dddddd")
palette.pack(side="left", fill="y")

program_container = tk.Frame(root)
program_container.pack(side="right", fill="both", expand=True)

sequence_area = SequenceArea(program_container)


def handle_drop(block, x, y):
    """When the block is dropped in the sequence area, clone a non template block there."""
    print(f"Dropped block {block.block_type} at ({x}, {y})")

    if block.is_template:
        if sequence_area.contains(x, y):
            new_block = block.clone(sequence_area.frame)
            new_block.drop_callback = handle_drop
            sequence_area.add_block(new_block)
    else:
        if not sequence_area.contains(x, y):
            block.destroy()
            sequence_area.blocks.remove(block)


# creates the block templates in the palette
for block_type, color in template_blocks:
    block = Block(palette, block_type, color, is_template=True)
    block.drop_callback = handle_drop
    block.pack(pady=15, padx=15, fill="x")

root.mainloop()
