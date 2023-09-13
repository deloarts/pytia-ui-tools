"""
    A simple text editor that accepts tkinter StringVars.
"""

from tkinter import END, WORD, StringVar
from typing import Optional

from ttkbootstrap import Button, Frame
from ttkbootstrap.scrolled import ScrolledText
from ttkbootstrap.window import Style, Toplevel

from pytia_ui_tools.window_manager import WindowManager


class TextEditor(Toplevel):
    """Toplevel subclass that spawns a text editor window with `ttkbootstrap` styling"""

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
        Style()

        self.textvariable = textvariable

        self.title(title if title else "Text Editor")
        self.attributes("-topmost", True)
        self.update()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (width / 2))
        y_coordinate = int((screen_height / 2) - (height / 2))
        self.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")
        self.minsize(width, height)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_data = Frame(master=self)
        self.frame_data.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 5))
        self.frame_data.grid_columnconfigure(0, weight=1)
        self.frame_data.grid_rowconfigure(0, weight=1)

        self.frame_footer = Frame(master=self, height=30)
        self.frame_footer.grid(row=1, column=0, sticky="swe", padx=10, pady=(5, 10))
        self.frame_footer.grid_columnconfigure(0, weight=1)

        self.text_widget = ScrolledText(self.frame_data, wrap=WORD)
        self.text_widget.grid(row=0, column=0, sticky="nsew")
        self.text_widget.focus_set()
        self.text_widget.text.delete("1.0", END)
        self.text_widget.text.insert(END, self.textvariable.get())

        self.btn_save = Button(
            self.frame_footer,
            command=self.on_btn_apply,
            text="Apply",
            style="outline",
            width=10,
        )
        self.btn_save.grid(row=0, column=0, padx=(5, 2), pady=0, sticky="e")

        self.btn_abort = Button(
            self.frame_footer,
            command=self.on_btn_abort,
            text="Abort",
            style="outline",
            width=10,
        )
        self.btn_abort.grid(row=0, column=1, padx=(2, 0), pady=0, sticky="e")

        self.bind("<Escape>", lambda _: self.on_btn_abort())

        self.update()
        self.grab_set()

        window_manager = WindowManager(self)
        window_manager.remove_window_buttons()

        self.mainloop()

    def on_btn_apply(self) -> None:
        """
        Callback function for the apply button.
        Closes the window and writes the text value to the textvariable.
        """
        self.textvariable.set(self.text_widget.text.get("1.0", END))
        self.grab_release()
        self.withdraw()
        self.destroy()

    def on_btn_abort(self) -> None:
        """Callback function for the abort button. Closes the window."""
        self.grab_release()
        self.withdraw()
        self.destroy()
