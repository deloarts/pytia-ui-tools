"""
    Constants for this package.
"""

import os

HOSTNAME = str(os.environ.get("COMPUTERNAME"))
USERNAME = str(os.environ.get("USERNAME"))
USERPROFILE = str(os.environ.get("USERPROFILE"))

TEMPLATE_ERROR = "error_mail.html"

GWL_STYLE = -16
WS_CHILD = 0x40000000
WS_SYSMENU = 0x00080000

SWP_FRAMECHANGED = 0x0020
SWP_NOACTIVATE = 0x0010
SWP_NOMOVE = 0x0002
SWP_NOSIZE = 0x0001
