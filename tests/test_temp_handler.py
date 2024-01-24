import os
from tempfile import gettempdir

filename = "pytia_ui_tools_test.txt"
path = gettempdir() + "\\" + filename


def test_import():
    from pytia_ui_tools.handlers.temp_handler import TempHandler


def test_delete_tempfile():
    from pytia_ui_tools.handlers.temp_handler import TempHandler

    with open(path, "w") as f:
        f.write("test")

    temp_handler = TempHandler()
    temp_handler.delete_tempfile(filename=filename)

    assert os.path.exists(path) == False
