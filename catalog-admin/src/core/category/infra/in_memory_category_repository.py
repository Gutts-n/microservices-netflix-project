from src.core.category.application.category_repository import CategoryRepository


class InMemoryCategoryRepository(CategoryRepository):
    def __init__(self, categories = {}):
        self.categories = categories or {}
    
    def save(self, category):
        self.categories[category.id] = category