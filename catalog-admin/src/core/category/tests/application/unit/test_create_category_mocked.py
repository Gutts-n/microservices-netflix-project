from unittest.mock import MagicMock

import pytest

from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.exceptions import InvalidCategoryDataError
from src.core.category.domain.errors_messages import NAME_EMPTY_ERROR_MESSAGE
from src.core.category.application.create_category import CreateCategoryRequest, CreateCategoryResponse, CreateCategory


class TestCreateCategory:
    repository_mock = MagicMock(CategoryRepository)

    def test_create_category_with_valid_data(self):
        category = CreateCategory(repository=self.repository_mock).execute(
            CreateCategoryRequest(name="name", description="description", is_active=True))

        assert category is not None
        assert isinstance(category, CreateCategoryResponse)
        assert self.repository_mock.save.called is True

    def test_create_category_with_invalid_data(self):
        with pytest.raises(InvalidCategoryDataError, match=NAME_EMPTY_ERROR_MESSAGE) as exc_info:
            CreateCategory(repository=self.repository_mock).execute(
                CreateCategoryRequest(name=None))

        assert exc_info.type == InvalidCategoryDataError
        assert str(exc_info.value) == NAME_EMPTY_ERROR_MESSAGE
