"""
    Tkinter Entries templates.
"""

from tkinter import StringVar

from ttkbootstrap import Entry, Frame, Labelframe, Window

from pytia_ui_tools.helper.validators import validate_number


class NumberEntry(Entry):
    """
    `ttkbootstrap` entry subclass widget that only accepts digits and a floating point.
    """

    def __init__(
        self,
        master: Window | Frame | Labelframe,
        string_var: StringVar,
        replace_comma: bool = True,
        **kwargs,
    ):
        """
        Inits the widget.

        Args:
            master (Window | Frame | Labelframe): The `ttkbootstrap` master object.
            string_var (StringVar): The tkinter string variable.
            replace_comma (bool): Replaces comma inputs with dots. Defaults to True.
        """
        self.repl = replace_comma
        self.var = string_var
        self.var.trace("w", self._validate)
        super().__init__(master, textvariable=self.var, **kwargs)
        self.get, self.set = self.var.get, self.var.set

    def _validate(self, *_):
        """Validates the input."""
        self.set(validate_number(self.get(), self.repl))
