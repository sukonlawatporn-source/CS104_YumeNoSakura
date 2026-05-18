from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customers")

    customers = cursor.fetchall()

    conn.close()

    return render_template(
        'index.html',
        customers=customers
    )

@app.route('/add', methods=['POST'])
def add_customer():

    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO customers (name, phone, email) VALUES (?, ?, ?)",
        (name, phone, email)
    )

    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/delete/<int:id>')
def delete_customer(id):

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM customers WHERE cus_id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/edit/<int:id>')
def edit_customer(id):

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM customers WHERE cus_id = ?",
        (id,)
    )

    customer = cursor.fetchone()

    conn.close()

    return render_template(
        'edit.html',
        customer=customer
    )

@app.route('/update/<int:id>', methods=['POST'])
def update_customer(id):

    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE customers
        SET name = ?, phone = ?, email = ?
        WHERE cus_id = ?
        """,
        (name, phone, email, id)
    )

    conn.commit()
    conn.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)