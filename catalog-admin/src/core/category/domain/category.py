from dataclasses import dataclass, field
import uuid

from src.core.category.domain.errors_messages import NAME_EMPTY_ERROR_MESSAGE, NAME_LONGER_THAN_255_ERROR_MESSAGE


@dataclass
class Category:
    name: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    description: str = ""
    is_active: bool = True

    def __post_init__(self):
        self.validate()

    def validate(self):
        if not self.name:
            raise ValueError(NAME_EMPTY_ERROR_MESSAGE)

        if len(self.name) > 255:
            raise ValueError(NAME_LONGER_THAN_255_ERROR_MESSAGE)

    def activate(self):
        self.is_active = True

        self.validate()

    def inactivate(self):
        self.is_active = False

        self.validate()

    def update_category(self, name, description):
        self.description = description
        self.name = name

        self.validate()

    def __str__(self):
        return f"{self.name} - {self.description} ({self.is_active})"

    def __repr__(self):
        return f"<Category {self.name} - {self.description} ({self.is_active})"

    def __eq__(self, other):
        if not isinstance(other, Category):
            return False

        return self.id == other.id
