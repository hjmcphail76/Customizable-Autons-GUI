import tkinter as tk


class Block:
    def __init__(self, parent, block_type, color, is_template=False):
        self.block_type = block_type
        self.color = color
        self.is_template = is_template

        self.widget = tk.Label(
            parent,
            text=block_type.value,
            bg=color,
            fg="white",
            padx=10,
            pady=5,
            # relief="raised"
        )

        self.widget.bind("<ButtonPress-1>", self.on_press)
        self.widget.bind("<ButtonRelease-1>", self.on_release)

        self.drag_start = None
        self.drop_callback = None

    def pack(self, **kwargs):
        self.widget.pack(**kwargs)

    def on_press(self, event):
        self.drag_start = (event.x_root, event.y_root)

    def on_release(self, event):
        if self.drop_callback:
            self.drop_callback(self, event.x_root, event.y_root)

    def clone(self, new_parent):
        """Create a new instance of this block"""
        return Block(
            new_parent,
            self.block_type,
            self.color,
            is_template=False
        )

    def destroy(self):
        self.widget.destroy()
