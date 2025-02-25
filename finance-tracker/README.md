# README.md

# Personal Finance Tracker

This project is a personal finance tracker that allows users to log expenses, categorize spending, and visualize trends using a web-based dashboard. The application also includes an AI feature that suggests ways to save money based on spending patterns.

## Features

- Log expenses and categorize them
- Visualize spending trends with Matplotlib
- AI suggestions for saving money based on spending patterns

## Project Structure

```
finance-tracker
├── src
│   ├── app.py                # Main entry point of the application
│   ├── dashboard              # Dashboard module
│   │   ├── __init__.py
│   │   └── routes.py         # Routes for the web-based dashboard
│   ├── models                 # Data models
│   │   ├── __init__.py
│   │   ├── expense.py        # Expense model
│   │   └── category.py       # Category model
│   ├── services               # Business logic and analysis
│   │   ├── __init__.py
│   │   ├── analysis.py       # Functions for analyzing spending patterns
│   │   └── ml_predictions.py  # Machine learning functions for saving suggestions
│   ├── static
│   │   └── styles.css        # CSS styles for the web dashboard
│   └── templates             # HTML templates
│       ├── base.html
│       ├── dashboard.html
│       └── expenses.html
├── tests                     # Unit tests
│   ├── __init__.py
│   ├── test_models.py
│   └── test_services.py
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd finance-tracker
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/app.py
   ```

4. Access the dashboard at `http://localhost:5000`.

## Usage

- Log your expenses and categorize them for better tracking.
- Use the dashboard to visualize your spending trends.
- Get AI-driven suggestions to help you save money based on your spending patterns.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.