"""
    Value related helper functions.
"""


from ttkbootstrap import Combobox


def add_current_value_to_combobox_list(widget: Combobox) -> None:
    """
    Helper function to add the current value of a combobox to the list of values of that combobox.

    Args:
        widget (Combobox): The `ttkbootstrap` widget to add the current value to.

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
