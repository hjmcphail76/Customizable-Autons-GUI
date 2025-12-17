import tkinter as tk
from enum import Enum
from sequence_area import SequenceArea
from block import Block


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

root = tk.Tk()
root.geometry("800x400")
root.title("Configurable Autonomous Program Builder")

# template boxes live here
palette = tk.Frame(root, width=250, bg="#dddddd")
palette.pack(side="left", fill="y")

program_container = tk.Frame(root)
program_container.pack(side="right", fill="both", expand=True)

program = SequenceArea(program_container)


def handle_drop(block, x, y):
    """When the block is dropped in the sequence area, clone a non template block there."""
    if program.contains(x, y):
        if block.is_template:
            new_block = block.clone(program.frame)
            program.add_block(new_block)
        else:
            block.destroy()


# creates the block templates in the palette
for block_type, color in template_blocks:
    block = Block(palette, block_type, color, is_template=True)
    block.drop_callback = handle_drop
    block.pack(pady=5, padx=10, fill="x")

root.mainloop()
