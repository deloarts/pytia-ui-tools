"""
    Tkinter Vars templates.
"""

import re
import tkinter as tk


class NumberVar(tk.StringVar):
    """StringVar subclass that only accepts digits and a floating point."""

    def __init__(self, replace_comma: bool = True, **kwargs):
        """
        Constructs a number variable, based on a StringVar object.

        Args:
            replace_comma (bool, optional): Replaces a comma with a dot. Defaults to True.
        """
        super().__init__(**kwargs)
        self.trace_variable("w", self._validate)
        self.repl = replace_comma

    def _validate(self, *_):
        """Validates the input."""
        value = self.get()

        if self.repl:
            value = value.replace(",", ".")

        if not re.match(r"(\d|\d.\d)$", value):
            fp = False
            v = ""
            for c in value:
                if c.isdigit():
                    v += c
                if c in [".", ","] and not fp:
                    v += c
                    fp = True
            self.set(v)
