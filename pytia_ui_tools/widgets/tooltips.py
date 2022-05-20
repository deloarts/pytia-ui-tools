"""
    Module for the Tooltip class.
"""

import tkinter as tk


class ToolTip:
    """Class for creating tooltips over widgets."""

    def __init__(self, widget: tk.Widget, text: str, delay_ms: int = 500):
        """
        Create a tooltip for a given widget.

        Args:
            widget (_type_): The tkinter widget for tooltip-ing.
            text (str): The tooltip text.
            delay_ms (int, optional): Time after which the tooltip should show on hover in \
                milliseconds. Defaults to 500.
        """
        self.delay_ms = delay_ms  # milliseconds
        self.wraplength = 300  # pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self._enter)
        self.widget.bind("<Leave>", self._leave)
        self.widget.bind("<ButtonPress>", self._leave)
        self.tip_id = None
        self.tip_window = None

    def _enter(self, _):
        """Binding for entering the widget."""
        self._schedule()

    def _leave(self, _):
        """Binding for leaving the widget."""
        self._unschedule()
        self.hidetip()

    def _schedule(self):
        """Schedule for showing the widget."""
        self._unschedule()
        self.tip_id = self.widget.after(self.delay_ms, self.showtip)

    def _unschedule(self):
        """Removes schedule."""
        tip_id = self.tip_id
        self.tip_id = None
        if tip_id:
            self.widget.after_cancel(tip_id)

    def showtip(self):
        """Shows the tooltip."""
        if self.text != "":
            x = y = 0
            x, y, cx, cy = self.widget.bbox("insert")  # type:ignore
            x += self.widget.winfo_rootx() + 25
            y += self.widget.winfo_rooty() + 20
            # creates a toplevel window
            self.tip_window = tk.Toplevel(self.widget)
            # Leaves only the label and removes the app window
            self.tip_window.wm_overrideredirect(True)
            self.tip_window.attributes("-topmost", True)
            self.tip_window.wm_geometry(f"+{x}+{y}")
            label = tk.Label(
                self.tip_window,
                text=self.text,
                justify="left",
                background="#ffffff",
                relief="solid",
                borderwidth=1,
                wraplength=self.wraplength,
                font=("Segoe UI", 9),
            )
            label.pack(ipadx=5, ipady=5)

    def hidetip(self):
        """Removes the tooltip."""
        tip_window = self.tip_window
        self.tip_window = None
        if tip_window:
            tip_window.destroy()
