import unittest
from src.services.analysis import analyze_expenses
from src.services.ml_predictions import suggest_savings
from src.models.expense import Expense

class TestServices(unittest.TestCase):

    def setUp(self):
        self.expenses = [
            Expense(amount=100, category='Food', date='2023-01-01'),
            Expense(amount=50, category='Transport', date='2023-01-02'),
            Expense(amount=200, category='Entertainment', date='2023-01-03'),
        ]

    def test_analyze_expenses(self):
        analysis_result = analyze_expenses(self.expenses)
        self.assertIsInstance(analysis_result, dict)
        self.assertIn('total_spent', analysis_result)
        self.assertIn('category_breakdown', analysis_result)

    def test_suggest_savings(self):
        suggestions = suggest_savings(self.expenses)
        self.assertIsInstance(suggestions, list)
        self.assertGreater(len(suggestions), 0)

if __name__ == '__main__':
    unittest.main()