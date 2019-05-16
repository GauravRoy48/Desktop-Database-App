##################################################################################
# Creator     : Gaurav Roy
# Date        : 16 May 2019
# File        : backend.py
#
# Description : The backend uses Sqlite3 to access the bookstore database and 
#               perform functions asked by main.py.
##################################################################################

import sqlite3

# Function to connect to the books.db database. If books.db doesn't exist, it gets created.
def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()
    
# Function to insert a new element into the database.
def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")    
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL, ?, ?, ?, ?)",(title, author, year, isbn))
    conn.commit()
    conn.close()
    
# Function to view all elements.
def view():
    conn = sqlite3.connect("books.db")    
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

# Function to search for an element based on either title, author, year or ISBN.
def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")    
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

# Function to delete the selected element from the list.
def delete(id):
    conn = sqlite3.connect("books.db")    
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

# Function to update the selected element from the list.
def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")    
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn, id))
    conn.commit()
    conn.close()
        

connect()