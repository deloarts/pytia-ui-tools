"""
    Tkinter text widgets.
"""

from tkinter import DISABLED
from tkinter import NORMAL
from tkinter import StringVar
from tkinter import Toplevel
from typing import Optional

from ttkbootstrap import Frame
from ttkbootstrap import Labelframe
from ttkbootstrap import Window
from ttkbootstrap import scrolled

from pytia_ui_tools.tools.text_editor import TextEditor


class ScrolledText(scrolled.ScrolledText):
    """
    `ttkbootstrap` ScrolledText subclass widget with a vertical scrollbar and
    textvariable support.
    """

    def __init__(
        self,
        *args,
        parent: Window | Frame | Labelframe | Toplevel,
        textvariable: Optional[StringVar] = None,
        **kwargs,
    ):
        """Inits the widget.

        Args:
            parent (Window | Frame | Labelframe | Toplevel):  The `ttkbootstrap` \
                master object.
            textvariable (Optional[StringVar], optional): The tkinter textvariable. \
                Defaults to None.
        """
        self._textvariable = textvariable or StringVar()

        super().__init__(parent, *args, **kwargs)

        if "state" in kwargs:
            self.state = kwargs["state"]
        else:
            self.state = NORMAL

        if self._textvariable is not None:
            self.text.insert("1.0", self._textvariable.get())

        self.text.bind("<KeyRelease>", self._on_widget_change)
        self.text.bind("<Double-Button-1>", lambda _: TextEditor(self._textvariable))

        # if self._textvariable is not None:
        self._textvariable.trace("wu", self._on_var_change)

    def _on_var_change(self, *args):
        """
        Callback function for the textvariable trace.
        Writes the textvariable value to the text widget.
        """
        state = self.text["state"]
        self.text["state"] = NORMAL
        text_current = self.text.get("1.0", "end-1c")
        var_current = self._textvariable.get()
        if text_current != var_current:
            self.text.delete("1.0", "end")
            self.text.insert("1.0", var_current)
        self.text["state"] = state

    def _on_widget_change(self, event=None):
        """
        Callback function for the text widget change-binding.
        Writes the widget value to the textvariable.
        """
        if self._textvariable is not None:
            self._textvariable.set(self.text.get("1.0", "end-1c"))

    @property
    def state(self) -> str:
        """Returns the state of the widget."""
        return self._state

    @state.setter
    def state(self, value: str) -> None:
        """Sets the state of the widget. State can either be 'normal' or 'disabled'."""
        if value == NORMAL:
            self.text["state"] = NORMAL
            self.text["cursor"] = "xterm"
            self.text.bind(
                "<Double-Button-1>",
                lambda _: TextEditor(self._textvariable),
            )
        elif value == DISABLED:
            self.text["state"] = DISABLED
            self.text["cursor"] = "arrow"
            self.text.unbind("<Double-Button-1>")
        else:
            raise ValueError(f"Cannot set widget to state {value}")
        self._state = value
