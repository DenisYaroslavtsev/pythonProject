import sqlite3


def initiate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    cursor.execute("CREATE INDEX IF NOT EXISTS idx_id ON Products(id)")
    for i in range(1, 5):
        cursor.execute("INSERT INTO Products(title, description, price) VALUES(?, ?, ?)",
                       (f'Продукт №{i}', f'Продукт для организма №{i}', f'{i * 500}руб.'))

    connection.commit()
    connection.close()

    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')

    cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users(email)")

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    connection.close()
    return products


def add_users(username, email, age):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, 1000)", (username, email, age))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("SELECT 1 FROM Users WHERE username = ?", (username,))
    count_users = cursor.fetchone()
    connection.commit()
    connection.close()
    return bool(count_users)
