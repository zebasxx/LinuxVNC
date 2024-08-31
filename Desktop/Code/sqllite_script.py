import sqlite3

# Path to your SQLite database
db_path = 'example.db'

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Example: Create a table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
''')

# Example: Insert a new record into the table
def insert_user(name, age):
    cursor.execute('''
    INSERT INTO users (name, age)
    VALUES (?, ?)
    ''', (name, age))
    conn.commit()

# Example: Read records from the table
def fetch_users():
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Example: Update a record in the table
def update_user(user_id, new_name, new_age):
    cursor.execute('''
    UPDATE users
    SET name = ?, age = ?
    WHERE id = ?
    ''', (new_name, new_age, user_id))
    conn.commit()

# Example: Delete a record from the table
def delete_user(user_id):
    cursor.execute('''
    DELETE FROM users WHERE id = ?
    ''', (user_id,))
    conn.commit()

# Example usage
insert_user('Alice', 30)
insert_user('Bob', 25)

print("Users before update:")
fetch_users()

update_user(1, 'Alice Cooper', 31)

print("Users after update:")
fetch_users()

delete_user(2)

print("Users after deletion:")
fetch_users()

# Close the connection when done
conn.close()
