import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER
)
''')


#k = 10
#for i in range(1, 11):
#    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"newuser{i}", "example2@gmail.com", f"{k}", "1000"))
#    k += 10


#for i in range(1, 11, 2):
#    cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, i))


#for i in range(1, 11, 3):
#    cursor.execute('DELETE FROM Users WHERE id = ?', (i,))


cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
users = cursor.fetchall()
my_table = ['Имя: ', ' | Почта: ', ' | Возраст: ', ' | Баланс: ']

for user in users:
    for i in range(len(user)):
        print(my_table[i], end='')
        print(user[i], end='')
    print()


connection.commit()
connection.close()
