import pytest

from src.core.category.domain.category import Category
from uuid import UUID

from src.core.category.domain.errors_messages import NAME_EMPTY_ERROR_MESSAGE, NAME_LONGER_THAN_255_ERROR_MESSAGE


class TestCategory:
    def test_name_is_required(self):
        with pytest.raises(TypeError):
            Category()

    def test_name_must_have_less_than_255_characters(self):
        with pytest.raises(ValueError, match=NAME_LONGER_THAN_255_ERROR_MESSAGE):
            Category(name="a" * 256)

    def test_category_must_be_created_with_id_as_uuid(self):
        category = Category(name="name")
        assert isinstance(category.id, UUID)

    def test_created_category_with_default_values(self):
        category = Category(name="name")
        assert category.name == "name"
        assert category.description == ""
        assert category.is_active is True

    def test_category_is_created_as_active_by_default(self):
        category = Category(name="name")
        assert category.is_active is True

    def test_category_is_created_with_provided_values(self):
        category = Category("name", "123", "description",  False)
        assert category.is_active is False
        assert category.name == "name"
        assert category.description == "description"
        assert category.id == "123"

    def test_category_is_printed_correctly(self):
        category = Category("name", "123", "description", False)
        assert category.__str__(
        ) == f"{category.name} - {category.description} ({category.is_active})"

    def test_category_represented_correctly(self):
        category = Category("name", "123", "description", False)
        assert category.__repr__(
        ) == f"<Category {category.name} - {category.description} ({category.is_active})"

    def test_cannot_create_category_with_empty_value(self):
        with pytest.raises(ValueError, match=NAME_EMPTY_ERROR_MESSAGE):
            Category(name=None)


class TestUpdateCategory:
    def test_update_category_with_name_and_description(self):
        category = Category(name="name", description="123")
        category.update_category("new name", "new desc")

        assert category.name == 'new name'
        assert category.description == 'new desc'

    def test_update_category_with_invalid_name_raises_exception(self):
        category = Category(name="name", description="123")
        with pytest.raises(ValueError, match=NAME_LONGER_THAN_255_ERROR_MESSAGE):
            category.update_category("a" * 256, "new desc")

    def test_cannot_update_category_with_empty_value(self):
        category = Category(name="name", description="123")
        with pytest.raises(ValueError, match=NAME_EMPTY_ERROR_MESSAGE):
            category.update_category(None, "123")


class TestActivate:
    def test_activate_inactive_category(self):
        category = Category(name="name", description="123", is_active=False)

        assert category.is_active is False

        category.activate()

        assert category.is_active is True

    def test_activate_active_category(self):
        category = Category(name="name", description="123", is_active=True)

        assert category.is_active is True

        category.activate()

        assert category.is_active is True
        
    def test_inactivate_active_category(self):
        category = Category(name="name", description="123", is_active=True)

        assert category.is_active is True

        category.inactivate()

        assert category.is_active is False
        
    def test_inactivate_inactive_category(self):
        category = Category(name="name", description="123", is_active=False)

        assert category.is_active is False

        category.inactivate()

        assert category.is_active is False

class TestEquality:
    def test_when_categories_have_same_id_they_are_equals(self):
        category_1 = Category(name="123", id = "123")
        category_2 = Category(name="123", id = "123")

        assert category_1 == category_2

    def test_equality_different_classes(self):
        class Dummy:
            pass
        category_1 = Category(name="123", id = "123")
        dummy = Dummy()
        dummy.id = "123"

        assert category_1 != dummy