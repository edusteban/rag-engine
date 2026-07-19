from dataclasses import dataclass


@dataclass
class VectorstoreChanges:
    to_add: set[str]
    to_delete: set[str]
    to_update: set[str]