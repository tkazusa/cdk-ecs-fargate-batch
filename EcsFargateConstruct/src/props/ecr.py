from dataclasses import dataclass

from .base import Base


@dataclass(frozen=True)
class RepositoryFromName(Base):
    id: str
    repository_name: str
