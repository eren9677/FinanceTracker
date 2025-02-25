class Expense:
    _expenses = []

    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

    def save(self):
        Expense._expenses.append(self)

    @classmethod
    def retrieve(cls):
        return cls._expenses