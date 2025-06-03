from unittest.mock import MagicMock
from uuid import UUID

import pytest

from src.core.category.domain.errors_messages import NAME_EMPTY_ERROR_MESSAGE
from src.core.category.application.create_category import CreateCategoryRequest, CreateCategoryResponse, InvalidCategoryDataError, CreateCategory
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository


class TestCreateCategory:
    repository = InMemoryCategoryRepository()

    def test_create_category_with_valid_data(self):
        response = CreateCategory(repository=self.repository).execute(
            CreateCategoryRequest(name="name", description="description", is_active=True))

        assert response is not None
        assert isinstance(response, CreateCategoryResponse)
        assert len(self.repository.categories.keys()) == 1
        assert [*self.repository.categories.values()][0].id == response.id

