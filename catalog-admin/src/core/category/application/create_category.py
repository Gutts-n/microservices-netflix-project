from dataclasses import dataclass
from uuid import UUID

from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.exceptions import InvalidCategoryDataError
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository

@dataclass
class CreateCategoryResponse:
    id: UUID

@dataclass
class CreateCategoryRequest:
    name: str
    description: str = ''
    is_active: bool = True

class CreateCategory:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def execute(self, request: CreateCategoryRequest) -> CreateCategoryResponse:
        try:
            category = Category(name=request.name, description=request.description, is_active=request.is_active)
            self.repository.save(category)
        except ValueError as err:
            raise InvalidCategoryDataError(err)

        return CreateCategoryResponse(category.id)
