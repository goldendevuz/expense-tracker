from enum import Enum


class Action(str, Enum):
    """Enum for defining supported actions in the task manager."""
    ADD: str = "add"
    DELETE: str = "delete"
    LIST: str = "list"
    SUMMARY: str = "summary"