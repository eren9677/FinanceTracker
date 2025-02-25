import unittest
from src.models.expense import Expense
from src.models.category import Category

class TestExpenseModel(unittest.TestCase):
    def setUp(self):
        self.category = Category(name="Food")
        self.expense = Expense(amount=50.0, category=self.category, date="2023-10-01")

    def test_expense_creation(self):
        self.assertEqual(self.expense.amount, 50.0)
        self.assertEqual(self.expense.category.name, "Food")
        self.assertEqual(self.expense.date, "2023-10-01")

    def test_expense_string_representation(self):
        self.assertEqual(str(self.expense), "Expense(amount=50.0, category=Food, date=2023-10-01)")

class TestCategoryModel(unittest.TestCase):
    def setUp(self):
        self.category = Category(name="Transport")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Transport")

    def test_category_string_representation(self):
        self.assertEqual(str(self.category), "Category(name=Transport)")

if __name__ == '__main__':
    unittest.main()