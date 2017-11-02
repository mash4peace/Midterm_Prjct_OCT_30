import sqlite3
def createDB():
    try:
        conn = sqlite3.connect("booksdb.db")
        conn.execute('''CREATE TABLE IF NOT EXISTS books (id INT PRIMAY KEY, name TEXT NOT NULL, cost FLOAT NOT NULL)''')
        print("Database file is created !!! ")
        conn.execute('''CREATE TABLE IF NOT EXISTS  booktypes(id INT, name TEXT, FOREIGN KEY (id) REFERENCES books(id))''')
        conn.execute('''CREATE TABLE  IF NOT EXISTS cart(book_id INT, FOREIGN KEY(book_id) REFERENCES books(id))''')
        conn.commit()
        conn.close()
        print("Three table are created in the database !!!")



    except sqlite3.OperationalError as err:
        print(err)
        print("Database already exists")
def showBooks(type):
    conn= sqlite3.connect("booksdb.db")
    c = conn.cursor()
    c.execute('''SELECT id, name, cost from books WHERE id LIKE ?''', (type,))
    bookLists = list(c.fetchall())
    return bookLists
def createBooks(book):
    conn = sqlite3.connect("booksdb.db")
    c = conn.cursor()
    c.execute('''INSERT INTO books(id, name, cost) VALUES(?,?,?)''', (book))
    conn.commit()
    conn.close()
def createBooksList():
    booksList = []
    booksList.append([1, "Python for dummies", 100.20])
    booksList.append([2, "Learn Python the Hard way", 50.9])
    booksList.append([3, "Python Crash Course", 20.0])

    for book in booksList:
        createBooks(book)




    print("Added in the table")

def deleletRows():
    conn = sqlite3.connect("books_info.db")
    cur = conn.execute('''DELETE FROM books''')
    deleteStatus = (cur.rowcount)
    if deleteStatus == 0:
        print("This books doesnt exist in the database")
    elif deleteStatus == 1:
        print("Row is deleted!")
    conn.commit()
    conn.close()


