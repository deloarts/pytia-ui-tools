"""
    Module for the ErrorHandler class.
"""

import sys
from tkinter import messagebox as tkmsg
from typing import Callable
from typing import List
from typing import Optional

from pytia_ui_tools.handlers.mail_handler import MailHandler
from pytia_ui_tools.handlers.temp_handler import temphandler
from pytia_ui_tools.log import log


class ErrorHandler:
    """Class for handling tk exception callbacks."""

    def __init__(
        self,
        mail_handler: MailHandler,
        warning_exceptions: Optional[List[Callable]] = None,
    ) -> None:
        """
        Inits the ErrorHandler. Connects to the **pytia** logger.

        Args:
            mail_handler (MailHandler): The beforehand instantiated mail handler.
            warning_exceptions (Optional[List[Callable]], optional): A list of Exceptions that \
                won't raise an error msg. Defaults to None.
        """
        self.mail_handler = mail_handler
        self.warning_exceptions = warning_exceptions

    def exceptions_callback(self, exc, val, _) -> None:
        """
        Logs exceptions to the **pytia** logger, sends an email to the standard receiver with the \
            logfile content and terminates the app.

        Use as tkinter exceptions callback.
        """
        log.exception(f"Exceptions callback: {val}")
        if exc in self.warning_exceptions:
            tkmsg.showwarning(
                title=self.mail_handler.app_title,
                message=f"{val}\n\nClick OK to terminate.",
            )
        else:
            if self.mail_handler.outlook_available():
                result = tkmsg.askquestion(
                    title=self.mail_handler.app_title,
                    message=(
                        f"An error occurred:\n\n{val}\n\n"
                        f"Do you want to send the log file of this error to your administrator?"
                    ),
                    icon="error",
                )
                if result == "yes":
                    self.mail_handler.send_error_mail(val)
            else:
                tkmsg.showerror(
                    title=self.mail_handler.app_title,
                    message=f"An error occurred:\n\n{val}\n\nClick OK to terminate.",
                )

        sys.exit()

    def show_log(self):
        """
        Shows the current log file content.

        .. warning::
            This method is not implemented yet.
        """
        tkmsg.showwarning(
            title=self.mail_handler.app_title,
            message="Cannot show the current log.",
        )
