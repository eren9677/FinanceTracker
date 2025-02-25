from flask import Flask, render_template, redirect, url_for
from dashboard.routes import dashboard_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# Register the dashboard blueprint with a url_prefix
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

@app.route('/')
def index():
    return redirect(url_for('dashboard.index'))

if __name__ == "__main__":
    app.run(debug=True)