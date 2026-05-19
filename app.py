from flask import Flask, render_template, request, redirect
import sqlite3
import os

if not os.path.exists('database.db'):

    conn = sqlite3.connect('database.db')

    with open('cafecode.sql', 'r', encoding='utf-8') as f:
        conn.executescript(f.read())

    conn.commit()
    conn.close()

app = Flask(__name__)

# ================= HOME =================

@app.route('/')
def home():

    conn = sqlite3.connect(r'C:\GroupSQL\database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customers")

    customers = cursor.fetchall()

    conn.close()

    return render_template(
        'index.html',
        customers=customers
    )

# ================= ADD CUSTOMER =================

@app.route('/add_customer', methods=['POST'])
def add_customer():

    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']

    conn = sqlite3.connect(r'C:\GroupSQL\database.db')
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO customers(name, phone, email)
        VALUES (?, ?, ?)
        """,
        (name, phone, email)
    )

    conn.commit()
    conn.close()

    return redirect('/')

# ================= DELETE CUSTOMER =================

@app.route('/delete_customer/<int:id>')
def delete_customer(id):

    conn = sqlite3.connect(r'C:\GroupSQL\database.db')
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM customers WHERE cus_id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect('/')

# ================= EDIT CUSTOMER =================

@app.route('/edit_customer/<int:id>')
def edit_customer(id):

    conn = sqlite3.connect(r'C:\GroupSQL\database.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM customers WHERE cus_id = ?",
        (id,)
    )

    customer = cursor.fetchone()

    conn.close()

    return render_template(
        'edit_customer.html',
        customer=customer
    )

# ================= UPDATE CUSTOMER =================

@app.route('/update_customer/<int:id>', methods=['POST'])
def update_customer(id):

    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']

    conn = sqlite3.connect(r'C:\GroupSQL\database.db')
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

# ================= GAMES PAGE =================

@app.route('/games')
def games():

    conn = sqlite3.connect(r'C:\GroupSQL\database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM games")

    games = cursor.fetchall()

    conn.close()

    return render_template(
        'games.html',
        games=games
    )

# ================= ADD GAME =================

@app.route('/add_game', methods=['POST'])
def add_game():

    game_name = request.form['game_name']
    type = request.form['type']
    size_gb = request.form['size_gb']
    image = request.form['image']

    conn = sqlite3.connect(r'C:\GroupSQL\database.db')
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO games(game_name, type, size_gb, image)
        VALUES (?, ?, ?, ?)
        """,
        (game_name, type, size_gb, image)
    )

    conn.commit()
    conn.close()

    return redirect('/games')

# ================= DELETE GAME =================

@app.route('/delete_game/<int:id>')
def delete_game(id):

    conn = sqlite3.connect(r'C:\GroupSQL\database.db')
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM games WHERE game_id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect('/games')

# ================= EDIT GAME =================

@app.route('/edit_game/<int:id>')
def edit_game(id):

    conn = sqlite3.connect(r'C:\GroupSQL\database.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM games WHERE game_id = ?",
        (id,)
    )

    game = cursor.fetchone()

    conn.close()

    return render_template(
        'edit_game.html',
        game=game
    )

# ================= UPDATE GAME =================

@app.route('/update_game/<int:id>', methods=['POST'])
def update_game(id):

    game_name = request.form['game_name']
    type = request.form['type']
    size_gb = request.form['size_gb']
    image = request.form['image']

    conn = sqlite3.connect(r'C:\GroupSQL\database.db')
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE games
        SET game_name = ?, type = ?, size_gb = ?, image = ?
        WHERE game_id = ?
        """,
        (game_name, type, size_gb, image, id)
    )

    conn.commit()
    conn.close()

    return redirect('/games')

if __name__ == '__main__':
    app.run(debug=True)
