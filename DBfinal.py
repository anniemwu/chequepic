#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

url = 'https://www.pixenli.com/image/bIov3LOW'
url2 = 'https://www.alvinailey.org/sites/default/files/styles/slideshow_image/public/melanie-person.jpg?itok=ocw3xkx_'

base = sqlite3.connect('database.db')

elem = base.cursor()
elem.execute("""
CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     first_name TEXT,
     last_name TEXT,
     age INTERGER,
     picture_url BLOB
)
""")
base.commit()


users = []
     
users.append(("Ben", "Dautel", 22, url))
users.append(("Melany", "Person", 35, url2))
elem.executemany("""
INSERT INTO users(first_name, last_name, age, picture_url) VALUES(?, ?, ?, ?)""", users)

elem.execute("""UPDATE users SET age = ? WHERE id = 2""", (31,))

for id in range(1,3):
    elem.execute("""SELECT id, first_name, last_name, age, picture_url FROM users WHERE id=?""", (id,))
    response = elem.fetchone()
    print(response)
    

