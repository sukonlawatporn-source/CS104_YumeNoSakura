from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# ================= HOME =================

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

# ================= ADD CUSTOMER =================

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

# ================= DELETE CUSTOMER =================

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

# ================= EDIT CUSTOMER =================

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

# ================= UPDATE CUSTOMER =================

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

# ================= GAMES PAGE =================

@app.route('/games')
def games():

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM games")

    games = cursor.fetchall()

    conn.close()

    return render_template(
        'games.html',
        games=games
    )

# ================= DELETE GAME =================

@app.route('/delete_game/<int:id>')
def delete_game(id):

    conn = sqlite3.connect('database.db')
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

    conn = sqlite3.connect('database.db')
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

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE games
        SET game_name = ?, type = ?, size_gb = ?
        WHERE game_id = ?
        """,
        (game_name, type, size_gb, id)
    )

    conn.commit()
    conn.close()

    return redirect('/games')

if __name__ == '__main__':
    app.run(debug=True)