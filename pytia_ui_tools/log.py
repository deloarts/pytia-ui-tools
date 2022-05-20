"""
    Logging module that connects to the **pytia** logger.
"""

import logging

from pytia_ui_tools.const import HOSTNAME, USERNAME


class Log:
    """Class for logging to the **pytia** logger."""

    def __init__(self) -> None:
        """
        Inits the logger at level DEBUG.

        Formats the logger the same way as the pytia logger.
        """
        self.logger = logging.getLogger("pytia")
        self.format = logging.Formatter(
            f"%(asctime)s\t%(name)s\t%(levelname)s\t{HOSTNAME}\t{USERNAME}\t%(message)s"
        )
        self.logger.setLevel(logging.DEBUG)

    def debug(self, message: str) -> None:
        """
        Logs an **debug** message from an exception to the pytia logger.

        Args:
            message (str): The message to log.
        """
        self.logger.debug(msg=message)

    def info(self, message: str) -> None:
        """
        Logs an **info** message from an exception to the pytia logger.

        Args:
            message (str): The message to log.
        """
        self.logger.info(msg=message)

    def warning(self, message: str) -> None:
        """
        Logs an **warning** message from an exception to the pytia logger.

        Args:
            message (str): The message to log.
        """
        self.logger.warning(msg=message)

    def error(self, message: str) -> None:
        """
        Logs an **error** message from an exception to the pytia logger.

        Args:
            message (str): The message to log.
        """
        self.logger.error(msg=message)

    def exception(self, message: str) -> None:
        """
        Logs an **exception** message from an exception to the pytia logger.

        Args:
            message (str): The message to log.
        """
        self.logger.exception(msg=message)


log = Log()
