"""
    Module for the Workspace class.
"""


import os
from pathlib import Path

import yaml
from pytia_ui_tools.exceptions import PytiaUiToolsOutsideWorkspaceError
from pytia_ui_tools.log import log
from pytia_ui_tools.models.workspace import WorkspaceModel


class Workspace:
    """Handler for workspaces."""

    def __init__(self, path: str, filename: str, allow_outside_workspace: bool) -> None:
        """
        Inits the workspace handler class.

        Args:
            path (str): The path from which to search for the workspace file (upwards).
            filename (str): The workspace filename to search for.
            allow_outside_workspace (bool): Raises an exception if the workspace file cannot be \
                found.
        """
        self._model: WorkspaceModel
        self._path = path
        self._filename = filename
        self._allow_outside_workspace = allow_outside_workspace
        self._available = False

    def read_yaml(self) -> WorkspaceModel:
        """Reads the yaml workspace file."""
        for parent in Path(self._path).parents:
            if os.path.isfile((ws_file := Path(parent, self._filename))):
                with open(ws_file, "r") as f:
                    try:
                        self._model = WorkspaceModel.create(yaml.safe_load(f))
                        self._available = True
                        log.info(f"Loaded content from workspace file {f.name!r} ")
                        return self._model
                    except yaml.YAMLError as e:
                        raise Exception(f"Failed reading workspace file: {e}") from e

        if self._allow_outside_workspace:
            log.info("Couldn't find workspace file, applying default configuration.")
            self._model = WorkspaceModel()
            return self._model

        raise PytiaUiToolsOutsideWorkspaceError(
            "The current document is not part of a workspace. "
            "Please save the document inside a valid workspace."
        )

    @property
    def elements(self) -> WorkspaceModel:
        """Returns the elements of the workspace file."""
        return self._model

    @property
    def available(self) -> bool:
        """Returns wether the workspace file is available or not."""
        return self._available
