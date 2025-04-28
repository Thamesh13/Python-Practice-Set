from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime
import os

app = Flask(__name__, instance_relative_config=True)

db_path = os.path.join(app.instance_path, 'expenses.db')
os.makedirs(app.instance_path, exist_ok=True)

def init_db():
    with sqlite3.connect(db_path) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT,
            date_created TEXT NOT NULL
        )''')

def categorize(title):
    title = title.lower()
    if any(word in title for word in ['grocery', 'market', 'supermarket']):
        return 'groceries'
    elif any(word in title for word in ['electricity', 'water', 'internet']):
        return 'bills'
    return 'other'

@app.route('/')
def index():
    with sqlite3.connect(db_path) as conn:
        expenses = conn.execute('SELECT * FROM expenses ORDER BY date_created DESC').fetchall()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    amount = float(request.form['amount'])
    category = categorize(title)
    date_created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with sqlite3.connect(db_path) as conn:
        conn.execute('INSERT INTO expenses (title, amount, category, date_created) VALUES (?, ?, ?, ?)',
                     (title, amount, category, date_created))
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
