from pytia_ui_tools import __version__

from tests import tests_log, ts


def test_import():
    from pytia_ui_tools.handlers.mail_handler import MailHandler


def test_outlook():
    """
    Tests if the MS Outlook app responds. Requires Outlook to be installed.
    Make sure that all contents of the test.settings.json file are correct.
    """
    from pytia_ui_tools.handlers.mail_handler import MailHandler

    mail_handler = MailHandler(
        standard_receiver=ts.mail,
        app_title="Pytia-UI-Tools TEST",
        app_version=__version__,
        logfile=tests_log,
    )
    assert mail_handler.outlook_available()


def test_send_mail_html():
    """
    Tests if a mail can be sent via the local MS Outlook app.
    Requires Outlook to be installed.
    Make sure that all contents of the test.settings.json file are correct.
    """
    from pytia_ui_tools.handlers.mail_handler import MailHandler

    mail_handler = MailHandler(
        standard_receiver=ts.mail,
        app_title="PYTIA-UI-Tools TEST",
        app_version=__version__,
        logfile=tests_log,
    )
    mail_handler.send_mail(
        receiver=ts.mail,
        subject="TEST",
        body="<h1>HTML Body Test</h1>",
        attachments=[tests_log],
    )


def test_send_error_mail():
    """
    Tests if an errormail can be sent via the local MS Outlook app.
    Requires Outlook to be installed.
    Make sure that all contents of the test.settings.json file are correct.
    """
    from pytia_ui_tools.handlers.mail_handler import MailHandler

    mail_handler = MailHandler(
        standard_receiver=ts.mail,
        app_title="PYTIA-UI-Tools TEST",
        app_version=__version__,
        logfile=tests_log,
    )
    mail_handler.send_error_mail("Test Error")
