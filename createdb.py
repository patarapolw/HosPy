from passlib.hash import bcrypt
import sqlite3
import os
from common import *

username = 'guest'
password = ''
typeOfUser = 'guest'

h = bcrypt.hash(password)

# verify = bcrypt.verify(password, h)
# print(verify)
# verify = bcrypt.verify('password', h)
# print(verify)

db_path = os.path.join('database','login.db')
with sqlite3.connect(db_path) as con:
	# query = 'CREATE TABLE IF NOT EXISTS login (id INTEGER PRIMARY KEY AUTOINCREMENT\
	# 	, username TEXT\
	# 	, h TEXT\
	# 	);'
	# con.execute(query)

	# query = 'INSERT INTO login (username, h, type) \
	# 	VALUES (? , ?, ?);'
	# con.execute(query, (username, h, typeOfUser))

	# query = 'DELETE FROM login WHERE type=?;'
	# con.execute(query, (typeOfUser, ))

	# query = 'UPDATE login SET h=? \
	# 	WHERE username=?;'
	# con.execute(query, (h, username))

	# query = 'ALTER TABLE login ADD COLUMN type TEXT;'
	# con.execute(query)

	query = 'SELECT * FROM login'
	cursor = con.execute(query)
	common.printText(list(cursor))
