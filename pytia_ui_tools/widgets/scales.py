"""
    Tkinter Scales templates.
"""

from tkinter import IntVar
from typing import Callable
from typing import Optional

from ttkbootstrap import Frame
from ttkbootstrap import Labelframe
from ttkbootstrap import Scale
from ttkbootstrap import Window


class SnapScale(Scale):
    """`ttkbootstrap` scale subclass that limits the precision of values."""

    def __init__(
        self,
        master: Window | Frame | Labelframe,
        int_var: IntVar,
        from_: int,
        to: int,
        tick: int,
        command: Optional[Callable] = None,
        **kwargs
    ):
        """
        Inits the widget.

        Args:
            master (Window | Frame | Labelframe): The `ttkbootstrap` master object.
            int_var (IntVar): The int variable that connects to the scale.
            from_ (int): Scale minimum.
            to (int): Scale maximum.
            tick (int): Scale tick (or step).
            command (Optional[Callable], optional): The callback function. Defaults to None.
        """
        self.command = command
        self.value = int_var
        self.from_ = from_
        self.to = to
        self.tick = tick
        self.store = 0
        super().__init__(
            master,
            variable=self.value,
            from_=from_,
            to=to,
            command=self._value_changed,
            **kwargs
        )

    def configure(self, *args, **kwargs) -> None:
        """Overwrites the configure method of the widget and applies the correct command."""
        if "command" in kwargs:
            self.command = kwargs["command"]
            kwargs.pop("command")
            super().configure(command=self._value_changed, *args, **kwargs)
        else:
            super().configure(*args, **kwargs)

    def _value_changed(self, _):
        """Callback function on value change."""
        multiples = [n for n in range(self.from_, self.to + 1) if n % self.tick == 0]
        closest = min(multiples, key=lambda x: abs(x - self.get()))
        self.value.set(closest)
        if closest != self.store:
            self.store = closest
            if self.command:
                self.command()
