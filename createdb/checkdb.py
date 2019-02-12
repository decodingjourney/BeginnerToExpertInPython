import sqlite3

conn = sqlite3.connect("contacts.sqlite")

for row in conn.execute("select * from contacts"):
    print(row)

name = input("please enter the name")

sql_statement = "select * from contacts where name = ?"
sql_cursor = conn.cursor()
for name, phone, email in sql_cursor.execute(sql_statement, (name,)):
    print(name)
    print(phone)
    print(email)
    print("_" * 40)

conn.close()