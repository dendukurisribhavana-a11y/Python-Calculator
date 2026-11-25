import sqlite3

def create_database():
    connection = sqlite3.connect("calculator.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            calculation TEXT,
            result TEXT
        )
    """)

    connection.commit()
    connection.close()


def save_history(calculation, result):
    connection = sqlite3.connect("calculator.db")

    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO history (calculation, result) VALUES (?, ?)",
        (calculation, str(result))
    )

    connection.commit()
    connection.close()


def get_history():
    connection = sqlite3.connect("calculator.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM history")

    records = cursor.fetchall()

    connection.close()

    return records
