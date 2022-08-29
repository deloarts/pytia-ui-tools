"""
    Value related helper functions.
"""

from tkinter import ttk


def add_current_value_to_combobox_list(widget: ttk.Combobox) -> None:
    """
    Helper function to add the current value of a combobox to the list of values of that combobox.

    Args:
        widget (ttk.Combobox): The widget to add the current value to.

    Example:
        Bind this function on focus-out to a combobox to add the current value of the combobox to
        the combobox' list items:

        my_combobox.bind(
            "<FocusOut>",
            lambda _: add_current_value_to_combobox_list(my_combobox),
        )
    """
    if (value := widget.get()) not in (values := list(widget["values"])):
        widget["values"] = (*values, value)
