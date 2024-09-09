from JSQL import JSQL

db = JSQL("test.json")

db.create_table(
    "users",
    {
        'id': "int",
        "username": "str",
        "password": "str",
        "email": "str"
    },
    primary_key="id",
    check_if_already_exists=True
)
db.commit()

db.begin_transaction()

#db.add_column("users", "email", "str")

db.insert("users", { "id": 1, "username": "gio123", "password": "Dioporco", "email": "gio@gmail.com"})
db.insert("users", { "id": 2, "username": "mike123", "password": "Dioporco", "email": "mike@gmail.com"})
db.insert("users", { "id": 3, "username": "lollo123", "password": "WGesu", "email": "lollo@gmail.com"})

users = db.select("users", sort_by="id", ascending=False, limit=1, offset=0)
print(users)

db.update("users", { "password": "Cristodio"}, {"email": "mike@gmail.com"})

import time 
time.sleep(3)

db.delete("users", { "id": 3 })

db.commit()
