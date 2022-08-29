"""
    QR Code utility.
"""

import os
from datetime import datetime
from pathlib import Path
from tempfile import gettempdir
from typing import Optional

from pytia_ui_tools.exceptions import PytiaUiToolsFileTypeError
from pytia_ui_tools.log import log
from qrcode import QRCode


class QR:
    """Utility class for qr codes."""

    def __init__(self) -> None:
        """Inits the qr code class."""
        self.qr = QRCode()
        self.path: Path

    def generate(self, data: str | dict) -> None:
        """
        Creates a qr code object with the given data.

        Args:
            data (str | dict): The data to embed into the qr code.
        """
        if isinstance(data, dict):
            data = str(data)
        self.qr.add_data(data)
        self.qr.make(fit=True)
        log.info(f"Generated QR code with data: {data!r}")

    def save(self, path: Optional[Path] = None) -> Path:
        """
        Saves the qr code as png image file.

        Args:
            path (Optional[Path], optional): The save path for the png file. Defaults to None. \
                If None, the qr code will be saved in the temp directory.

        Raises:
            PytiaUiToolsFileTypeError: Raised if the provided path is not a png file.

        Returns:
            Path: The path where the qr code has been saved.
        """
        if path is None:
            path = Path(
                gettempdir(), f"qr_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
            )

        if ".png" not in (str_path := str(path)):
            raise PytiaUiToolsFileTypeError(
                f"The provided qr path is not a png file: {str_path}"
            )

        os.makedirs(path.parent, exist_ok=True)

        img = self.qr.make_image(fill_color="black", back_color="white")
        img.save(path)
        log.info(f"Saved QR code png to {str(path)!r}")

        return path
