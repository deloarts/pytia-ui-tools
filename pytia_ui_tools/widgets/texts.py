"""
    Tkinter text widgets.
"""

import tkinter as tk
from tkinter import StringVar, Toplevel, scrolledtext, ttk
from typing import Optional

from pytia_ui_tools.tools.text_editor import TextEditor


class ScrolledText(scrolledtext.ScrolledText):
    """Text subclass widget with a vertical scrollbar."""

    def __init__(
        self,
        parent: tk.Tk | tk.Frame | ttk.Frame | ttk.Labelframe | Toplevel,
        textvariable: Optional[StringVar] = None,
        *args,
        **kwargs,
    ):
        self._state = tk.NORMAL
        self._textvariable = textvariable or StringVar()

        if "state" in kwargs:
            self._state = kwargs["state"]
            kwargs.pop("state")

        super().__init__(parent, *args, **kwargs)

        if self._textvariable is not None:
            self.insert("1.0", self._textvariable.get())
        self.tk.eval(
            """
            proc widget_proxy {widget widget_command args} {
                set result [uplevel [linsert $args 0 $widget_command]]
                if {([lindex $args 0] in {insert replace delete})} {
                    event generate $widget <<Change>> -when tail
                }
                return $result
            }
            """
        )
        self.tk.eval(
            """
            rename {widget} _{widget}
            interp alias {{}} ::{widget} {{}} widget_proxy {widget} _{widget}
        """.format(
                widget=str(tk.Text.__str__(self))
            )
        )
        self.bind("<<Change>>", self._on_widget_change)
        self.bind(
            "<Double-Button-1>",
            lambda _: TextEditor(self._textvariable),
        )

        if self._textvariable is not None:
            self._textvariable.trace("wu", self._on_var_change)

    def _on_var_change(self, *args):
        """
        Callback function for the textvariable trace.
        Writes the textvariable value to the text widget.
        """
        text_current = self.get("1.0", "end-1c")
        var_current = self._textvariable.get()  # type: ignore
        if text_current != var_current:
            self.delete("1.0", "end")
            self.insert("1.0", var_current)

    def _on_widget_change(self, event=None):
        """
        Callback function for the text widget change-binding.
        Writes the widget value to the textvariable.
        """
        if self._textvariable is not None:
            self._textvariable.set(self.get("1.0", "end-1c"))

    @property
    def state(self) -> str:
        """Returns the state of the widget."""
        return self._state

    @state.setter
    def state(self, value: str) -> None:
        """Sets the state of the widget. State can either be 'normal' or 'disabled'."""
        match value:
            case tk.NORMAL:
                self.configure(
                    state=tk.NORMAL,
                    foreground="#000000",
                    background="#ffffff",
                    cursor="xterm",
                )
                self.bind(
                    "<Double-Button-1>",
                    lambda _: TextEditor(self._textvariable),
                )
            case tk.DISABLED:
                self.configure(
                    state=tk.DISABLED,
                    foreground="#6d6d6d",
                    background="#f0f0f0",
                    cursor="arrow",
                )
                self.unbind("<Double-Button-1>")
            case _:
                raise ValueError(f"Cannot set widget to state {value}")
        self._state = value
