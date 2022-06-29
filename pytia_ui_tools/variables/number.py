"""
    Tkinter number variable.
"""

import tkinter as tk

from pytia_ui_tools.helper.validators import validate_number


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
        self.set(validate_number(self.get(), self.repl))
