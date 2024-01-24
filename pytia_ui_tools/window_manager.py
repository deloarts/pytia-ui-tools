"""
    Module for the WindowManager class.
"""

from ctypes import windll
from ctypes import wintypes
from tkinter import Tk
from tkinter import Toplevel

from pytia_ui_tools.const import GWL_STYLE
from pytia_ui_tools.const import SWP_FRAMECHANGED
from pytia_ui_tools.const import SWP_NOACTIVATE
from pytia_ui_tools.const import SWP_NOMOVE
from pytia_ui_tools.const import SWP_NOSIZE
from pytia_ui_tools.const import WS_CHILD
from pytia_ui_tools.const import WS_SYSMENU


class WindowManager:
    """Class for managing tk window objects."""

    def __init__(self, window: Tk | Toplevel) -> None:
        """Inits the window manager class.

        Example of usage:

            import tkinter as tk
            class GUI(tk.Tk):
                def __init__(self):
                    tk.Tk.__init__(self)
                    self.window_manager = WindowManager(self)
                    self.window_manager.remove_window_buttons()
                    self.mainloop()

        Args:
            window (Tk): The tkinter toplevel widget that needs handling.
        """
        self.window = window
        self.get_window_long = windll.user32.GetWindowLongW
        self.get_window_long.restype = wintypes.ULONG
        self.set_window_long = windll.user32.SetWindowLongW
        self.set_window_long.restype = wintypes.ULONG
        self.set_window_pos = windll.user32.SetWindowPos

    def _get_hwnd(self) -> int:
        """
        Get the window handler.

        Returns:
            int: The window handler id.
        """
        w_id = self.window.winfo_id()
        style = self.get_window_long(w_id, GWL_STYLE)
        newstyle = style & ~WS_CHILD
        self.set_window_long(w_id, GWL_STYLE, newstyle)
        self.set_window_pos(
            w_id,
            0,
            0,
            0,
            0,
            0,
            SWP_FRAMECHANGED | SWP_NOACTIVATE | SWP_NOMOVE | SWP_NOSIZE,
        )
        hwnd = int(self.window.wm_frame(), 16)
        self.set_window_long(w_id, GWL_STYLE, style)
        self.set_window_pos(
            w_id,
            0,
            0,
            0,
            0,
            0,
            SWP_FRAMECHANGED | SWP_NOACTIVATE | SWP_NOMOVE | SWP_NOSIZE,
        )
        return hwnd

    def remove_window_buttons(self) -> None:
        """Removes title bar buttons and the icon from the window."""
        hwnd = self._get_hwnd()
        style = self.get_window_long(hwnd, GWL_STYLE)
        style = style & ~WS_SYSMENU
        self.set_window_long(hwnd, GWL_STYLE, style)
        self.set_window_pos(
            hwnd,
            0,
            0,
            0,
            0,
            0,
            SWP_FRAMECHANGED | SWP_NOACTIVATE | SWP_NOMOVE | SWP_NOSIZE,
        )

    def add_window_buttons(self) -> None:
        """Adds title bar buttons and the icon to the window."""
        hwnd = self._get_hwnd()
        style = self.get_window_long(hwnd, GWL_STYLE)
        style = style | WS_SYSMENU
        self.set_window_long(hwnd, GWL_STYLE, style)
        self.set_window_pos(
            hwnd,
            0,
            0,
            0,
            0,
            0,
            SWP_FRAMECHANGED | SWP_NOACTIVATE | SWP_NOMOVE | SWP_NOSIZE,
        )
