import sqlite3

db = sqlite3.connect("contacts.sqlite")

db.execute("create table if not exists contacts (name text, phone integer, email text)")
db.execute("insert into contacts(name, phone, email) values ('anand', 8088908090, 'vikramanand.jha@gmail.com')")
db.execute("insert into contacts values ('sonam', 9087998676, 'sonamm.jha@gmail.com')")

cursor = db.cursor()
cursor.execute("select * from contacts")

# print(cursor.fetchall())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("_" * 40)

# for name, phone, email in cursor:
#     print(name)
#     print(phone)
#     print(email)
#     print("_" * 40)

cursor.close()

db.close()