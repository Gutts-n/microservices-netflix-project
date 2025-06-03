from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository


class TestInMemoryCategoryRepository:
    def test_can_save_entity(self):
        repository = InMemoryCategoryRepository()
        category = Category(name="name", description="123")

        repository.save(category)

        assert len(repository.categories.keys()) == 1
        assert [*repository.categories.values()][0] == category