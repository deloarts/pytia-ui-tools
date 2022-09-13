"""
    Submodule for the workspace model class.
"""

from __future__ import annotations

from dataclasses import dataclass, field, fields
from typing import List, Optional


@dataclass
class WorkspaceModel:
    """Workspace model data class."""

    title: Optional[str] = field(default=None)
    active: Optional[bool] = field(default=True)
    customer: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)
    machine: Optional[str] = field(default=None)
    projects: Optional[List[str]] = field(default_factory=lambda: [])
    responsible: Optional[str] = field(default=None)
    delegate: Optional[str] = field(default=None)
    editors: Optional[List[str]] = field(default_factory=lambda: [])
    bom_name: Optional[str] = field(default=None)
    bom_folder: Optional[str] = field(default=None)
    docket_folder: Optional[str] = field(default=None)
    drawing_folder: Optional[str] = field(default=None)
    stp_folder: Optional[str] = field(default=None)
    stl_folder: Optional[str] = field(default=None)

    @classmethod
    def create(cls, data: dict) -> WorkspaceModel:
        """
        Creates a WorkspaceModel by the given dict. Keys that are not in the dataclass
        will be ignored.
        """
        return WorkspaceModel(
            **{k: v for k, v in data.items() if k in {f.name for f in fields(cls)}}
        )
