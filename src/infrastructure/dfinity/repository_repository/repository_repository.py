from typing import Optional

from domain.repository import RepositoryRepository, Repository


class RepositoryRepositoryImpl(RepositoryRepository):
    def create(self, repository: Repository) -> Optional[Repository]:
        pass

    def find_by_id(self, id: str) -> Optional[Repository]:
        pass

    def find_by_isbn(self, isbn: str) -> Optional[Repository]:
        pass

    def update(self, repository: Repository) -> Optional[Repository]:
        pass

    def delete_by_id(self, id: str):
        pass
