"""
    Module for the TempHandler class.
"""

import atexit
import os
from pathlib import Path
from tempfile import gettempdir
from typing import List, Optional

import pyscreenshot
from pytia_ui_tools.log import log


class TempHandler:
    """Handler class for temporary files."""

    def __init__(self) -> None:
        """
        Inits the temp handler.
        """
        self.tempdir = gettempdir()
        self.files_to_delete: List[Path] = []

        atexit.register(self._delete_files)

    def _delete_files(self) -> None:
        """
        Deletes files of the class list files_to_delete.
        """
        for path in self.files_to_delete:
            if os.path.exists(path):
                os.remove(path)
                log.info(f"Deleted tempfile {path!r}")

    def delete_tempfile(self, filename: str) -> None:
        """
        Deletes the file from the tempfolder.

        Args:
            filename (str): The file inside the tempfolder.
        """
        path = Path(self.tempdir, filename)
        if os.path.exists(path):
            os.remove(path)
            log.info(f"Deleted tempfile {str(path)!r}")

    def make_screenshot(self, filename: str = "screenshot.png") -> Optional[Path]:
        """
        Takes a screenshot of the error and returns the save path.

        Args:
            filename (Path): The filename (with file extension) of the screenshot PNG.

        Returns:
            Optional[Path]: The save path. None if no screenshot has been taken.
        """
        path = Path(gettempdir(), filename)
        screenshot = pyscreenshot.grab()
        if screenshot:
            screenshot.save(path)
            log.info(f"Saved screenshot to {path!r}")
            self.files_to_delete.append(path)
            return path
        return None


temphandler = TempHandler()
