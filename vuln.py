import sqlite3

# Создаем базу данных и таблицу для примера
connection = sqlite3.connect(':memory:')
cursor = connection.cursor()
cursor.execute('CREATE TABLE users (username TEXT, password TEXT)')
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")
connection.commit()

# Уязвимый код
def login(username, password):
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        return "Login successful!"
    else:
        return "Login failed!"

# Пример использования
user_input_username = input("Enter username: ")
user_input_password = input("Enter password: ")
print(login(user_input_username, user_input_password))

# Закрываем соединение
connection.close()
