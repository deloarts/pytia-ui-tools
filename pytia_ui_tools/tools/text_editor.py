"""
    A simple text editor that accepts tkinter StringVars.
"""

import tkinter as tk
from tkinter import StringVar, Toplevel, font, scrolledtext, ttk
from typing import Optional

from pytia_ui_tools.window_manager import WindowManager


class TextEditor(Toplevel):
    """Toplevel subclass that spawns a text editor window."""

    def __init__(
        self,
        textvariable: StringVar,
        width: int = 500,
        height: int = 350,
        title: Optional[str] = None,
    ) -> None:
        """
        Inits the text editor window. Opens the window on instantiation.

        Args:
            textvariable (StringVar): The tkinter StringVar.
            title (str): The title of the window.
            width (int, optional): Window width. Defaults to 500.
            height (int, optional): Window height. Defaults to 350.
        """
        Toplevel.__init__(self)

        self.textvariable = textvariable
        self.window_manager = WindowManager(self)

        self.title(title if title else "Text Editor")
        self.attributes("-topmost", True)
        self.default_font = font.nametofont("TkDefaultFont")
        self.default_font.configure(family="Segoe UI", size=9)
        self.update()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (width / 2))
        y_coordinate = int((screen_height / 2) - (height / 2))
        self.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")
        self.minsize(width, height)

        style = ttk.Style(self)
        style.configure("Footer.TButton", width=14)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_data = ttk.Frame(master=self, style="Data.TFrame")
        self.frame_data.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 5))
        self.frame_data.grid_columnconfigure(0, weight=1)
        self.frame_data.grid_rowconfigure(0, weight=1)

        self.frame_footer = ttk.Frame(master=self, height=30, style="Footer.TFrame")
        self.frame_footer.grid(row=1, column=0, sticky="swe", padx=10, pady=(5, 10))
        self.frame_footer.grid_columnconfigure(0, weight=1)

        self.text_widget = scrolledtext.ScrolledText(
            self.frame_data, font=("Segoe UI", 9)
        )
        self.text_widget.grid(row=0, column=0, sticky="nsew")
        self.text_widget.focus_set()
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert(tk.END, self.textvariable.get())

        self.btn_save = ttk.Button(
            self.frame_footer,
            text="Apply",
            command=self.on_btn_apply,
            style="Footer.TButton",
        )
        self.btn_save.grid(row=0, column=0, padx=(5, 2), pady=0, sticky="e")

        self.btn_abort = ttk.Button(
            self.frame_footer,
            text="Abort",
            command=self.on_btn_abort,
            style="Footer.TButton",
        )
        self.btn_abort.grid(row=0, column=1, padx=(2, 0), pady=0, sticky="e")

        self.update()
        self.grab_set()
        self.window_manager.remove_window_buttons()
        self.mainloop()

    def on_btn_apply(self) -> None:
        """
        Callback function for the apply button.
        Closes the window and writes the text value to the textvariable.
        """
        self.textvariable.set(self.text_widget.get("1.0", tk.END))
        self.grab_release()
        self.withdraw()
        self.destroy()

    def on_btn_abort(self) -> None:
        """Callback function for the abort button. Closes the window."""
        self.grab_release()
        self.withdraw()
        self.destroy()
