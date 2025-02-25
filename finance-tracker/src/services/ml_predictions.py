import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class MLModel:
    def __init__(self, data):
        self.data = data
        self.model = LinearRegression()

    def prepare_data(self):
        X = self.data[['amount', 'category_encoded']]  # Example features
        y = self.data['savings']  # Target variable
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self):
        X_train, X_test, y_train, y_test = self.prepare_data()
        self.model.fit(X_train, y_train)
        return self.model.score(X_test, y_test)

    def predict_savings(self, expense):
        expense_encoded = self.encode_category(expense['category'])  # Implement this method
        prediction = self.model.predict(np.array([[expense['amount'], expense_encoded]]))
        return prediction[0]

    def encode_category(self, category):
        # Placeholder for category encoding logic
        return 0  # Replace with actual encoding logic