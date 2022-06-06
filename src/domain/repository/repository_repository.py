from abc import ABC, abstractmethod
from typing import List, Optional

from domain.repository.repository import Repository


class RepositoryRepository(ABC):
    """RepositoryRepository defines a repository interface for Repository entity."""

    @abstractmethod
    def create(self, repository: Repository) -> Optional[Repository]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[Repository]:
        raise NotImplementedError

    @abstractmethod
    def find_by_isbn(self, isbn: str) -> Optional[Repository]:
        raise NotImplementedError

    @abstractmethod
    def update(self, repository: Repository) -> Optional[Repository]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: str):
        raise NotImplementedError
