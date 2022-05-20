"""
    Tkinter Entries templates.
"""

import re
import tkinter as tk
from tkinter import StringVar, ttk


class NumberEntry(ttk.Entry):
    """Entry subclass widget that only accepts digits and a floating point."""

    def __init__(
        self,
        master: tk.Tk | tk.Frame | ttk.Frame,
        string_var: StringVar,
        replace_comma: bool = True,
        **kwargs
    ):
        """
        Inits the widget.

        Args:
            master (_type_): The tkinter window master object.
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
        value = self.get()
        if self.repl:
            value = value.replace(",", ".")

        if not re.match(r"(\d|\d.\d)$", value):
            # if not value.isdigit():
            self.set("".join(x for x in value if x.isdigit() or x in [".", ","]))
