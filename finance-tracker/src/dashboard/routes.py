from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from models.expense import Expense
from models.category import Category

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
def index():
    return render_template('dashboard.html')

@dashboard_bp.route('/expenses')
def expenses():
    expenses = Expense.retrieve()
    return render_template('expenses.html', expenses=expenses)

@dashboard_bp.route('/log-expense', methods=['GET', 'POST'])
def log_expense():
    if request.method == 'POST':
        amount = request.form['amount']
        category_name = request.form['category']
        date = request.form['date']
        
        category = Category(name=category_name)
        expense = Expense(amount=amount, category=category, date=date)
        expense.save()
        
        return redirect(url_for('dashboard.expenses'))
    
    return render_template('expenses.html', expenses=Expense.retrieve())