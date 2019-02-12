import sqlite3

db = sqlite3.connect("contacts.sqlite")
new_email = 'anand@update.com'
phone = input("Please enter the phone number ")
# update_sql = "update contacts set email = {} where phone = {}".format(new_email, phone)
update_sql = "update contacts set email = ? where phone = ?"
print(update_sql)
update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))
print("{} rows updated".format(update_cursor.rowcount))


for name, phone, email in db.execute("select * from contacts"):
    print(name)
    print(phone)
    print(email)
    print("_" * 40)

db.commit()

db.close()