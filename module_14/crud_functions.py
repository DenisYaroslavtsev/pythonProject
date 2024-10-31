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


def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    connection.close()
    return products
