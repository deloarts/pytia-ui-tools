"""
    Module for the MailHandler class.
"""

import os
from pathlib import Path
from tkinter import messagebox as tkmsg
from typing import List, Optional

import jinja2
from win32com.client import CDispatch, Dispatch
from win32com.server.exception import COMException

from pytia_ui_tools.const import HOSTNAME, TEMPLATE_ERROR, USERNAME
from pytia_ui_tools.log import log


class MailHandler:
    """Class for handling mails via the local MS Outlook app."""

    def __init__(
        self, standard_receiver: str, app_title: str, app_version: str, logfile: Path
    ) -> None:
        """
        Inits the mail handler for sending mails through the local MS Outlook app.

        Args:
            standard_receiver (str): The mail address of the sys admin.
            app_title (str): The title of your tkinter GUI.
            app_version (str): The version of the tkinter GUI.
            logfile (Path): The path to the current logfile of your GUI.
        """
        self.app_title = app_title
        self.app_version = app_version
        self.logfile = logfile
        self.standard_receiver = standard_receiver

    @staticmethod
    def _get_dispatch() -> Optional[CDispatch]:
        """
        Connects to the outlook application dispatcher. Returns None if Outlook is not installed \
            on this system.

        Returns:
            Optional[CDispatch]: The dispatch from MS Outlook.
        """
        try:
            app = Dispatch("outlook.application")
            return app  # type: ignore
        except COMException as e:
            log.warning(f"Outlook is not installed on this system: {e}")
            return None
        except Exception as e:  # pylint: disable=broad-except
            log.error(f"Failed connecting to MS Outlook: {e}")
            return None

    @staticmethod
    def _render_template(template: str, **kwargs) -> str:
        """
        Renders the given template file with the given arguments. Templates file must exist in the \
            *templates* folder.

        Args:
            template (str): The filename of the template.

        Returns:
            str: Rendered template as string.
        """
        loader = jinja2.PackageLoader("pytia_ui_tools", "templates")
        env = jinja2.Environment(loader=loader)
        return env.get_template(template).render(**kwargs)

    def outlook_available(self) -> bool:
        """
        Checks if MS Outlook is available on the system.

        Returns:
            bool: True when MS Outlook is available on the machine, False otherwise.
        """
        return bool(self._get_dispatch())

    def send_mail(
        self,
        receiver: str,
        subject: str,
        body: Optional[str] = None,
        attachments: Optional[List[str]] = None,
    ) -> None:
        """
        Sends a mail using the local Outlook app.

        Shows an error message if the Outlook app is not available.

        Args:
            receiver (str): The receivers mail address.
            subject (str): Mail subject.
            body (Optional[str], optional): Mail body as html. Defaults to None.
            attachments (Optional[List[str]], optional): List of paths to the attachments. \
                Defaults to None.
        """

        if outlook := self._get_dispatch():
            try:
                mail = outlook.CreateItem(0)
                mail.To = receiver
                mail.Subject = subject
                mail.HTMLBody = body
                if attachments:
                    for attachment in attachments:
                        mail.Attachments.Add(attachment)
                mail.Send()
                log.info(f"Sent mail to {receiver} ({subject}).")
            except Exception as e:  # pylint: disable=broad-except
                msg = f"Cannot send mail to {receiver}:\n\n{e}"
                log.error(msg)
                tkmsg.showerror(
                    title=self.app_title,
                    message=msg,
                )
        else:
            msg = "Cannot send mail. Outlook not reachable."
            log.error(msg)
            tkmsg.showerror(
                title=self.app_title,
                message=msg,
            )

    def send_error_mail(
        self, error_value: str, screenshot_path: Optional[Path] = None
    ) -> None:
        """
        Sends a mail from an error with the logfile using the local MS Outlook installation to the \
            standard receiver.

        Args:
            error_value (str): The error value (or description).
            screenshot_path (Optional[str], optional): The path to the screenshot file.
            Defaults to None.
        """
        if os.path.exists(self.logfile):
            log.info(f"Sending error mail to {self.standard_receiver}.")

            subject = f"{self.app_title} | ERROR | {USERNAME} | {HOSTNAME}"
            body = self._render_template(
                template=TEMPLATE_ERROR,
                title=self.app_title,
                username=USERNAME,
                hostname=HOSTNAME,
                version=self.app_version,
                error=error_value,
            )
            attachments = [str(self.logfile)]
            if screenshot_path is not None:
                attachments.append(str(screenshot_path))

            self.send_mail(
                receiver=self.standard_receiver,
                subject=subject,
                body=body,
                attachments=attachments,
            )
        else:
            msg = f"Cannot send error-mail to {self.standard_receiver}: Logfile is missing."
            log.error(msg)
            tkmsg.showerror(
                title=self.app_title,
                message=msg,
            )
