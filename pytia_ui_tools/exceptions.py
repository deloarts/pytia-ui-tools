"""
    Module that holds all custom pytia-ui-tools exceptions.
"""

import sys
import traceback

from pytia_ui_tools.log import log


class PytiaUiToolsBaseError(Exception):
    """Base class for all pytia-ui-tools exceptions. Logs exceptions as error messages"""

    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        if traceback.extract_tb(sys.exc_info()[2]):
            log.exception(msg)
        else:
            log.error(msg)


class PytiaUiToolsOutsideWorkspaceError(PytiaUiToolsBaseError):
    """Exception for documents outside of the workspace."""
