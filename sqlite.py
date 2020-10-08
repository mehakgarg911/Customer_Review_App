import sqlite3
conn = sqlite3.connect('database.db')

print("Opened Successfully")

conn.execute('''CREATE TABLE REVIEWS 
	(NAME TEXT NOT NULL,
	PRODUCT TEXT NOT NULL,
	REVIEW TEXT NOT NULL);''')

print("Table created successfully")

conn.close()