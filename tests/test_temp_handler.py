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


def test_make_screenshot():
    from pytia_ui_tools.handlers.temp_handler import TempHandler

    scr_default_path = gettempdir() + "\\screenshot.png"
    scr_named_path = gettempdir() + "\\test_screenshot.png"

    temp_handler = TempHandler()
    temp_handler.make_screenshot()
    temp_handler.make_screenshot(filename="test_screenshot.png")

    assert os.path.exists(scr_default_path)
    assert os.path.exists(scr_named_path)
    os.remove(scr_default_path)
    os.remove(scr_named_path)
