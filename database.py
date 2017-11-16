import sqlite3
#Creating a database and three tables
def createDB():
    try:
        conn = sqlite3.connect("booksdb.db")
        conn.execute('''CREATE TABLE IF NOT EXISTS books (id INT PRIMAY KEY, name TEXT NOT NULL, cost FLOAT NOT NULL)''')
        print("Database file is created !!! ")
       # conn.execute('''DROP TABLE books''')
        #conn.execute('''CREATE TABLE IF NOT EXISTS  booktypes(id INT, name TEXT, FOREIGN KEY (id) REFERENCES books(id))''')
        conn.execute('''CREATE TABLE  IF NOT EXISTS cart(book_id INT, FOREIGN KEY(book_id) REFERENCES books(id))''')
        #conn.execute("DROP TABLE users")
        conn.execute('Create Table If not EXISTS users (id INTEGER  PRIMARY Key Autoincrement , name Text NOT NULL ,email text NOT NULL ,password Text NOT NULL)')

        conn.commit()
        conn.close()
        print("Three table are created in the database !!!")



    except sqlite3.OperationalError as err:
        print(err)
        print("Database already exists")
#Showing books in the browser
def showBooks(type):
    conn= sqlite3.connect("booksdb.db")
    c = conn.cursor()
    c.execute('''SELECT id, name, cost from books WHERE id LIKE ?''', (type,))
    bookLists = list(c.fetchall())
    return bookLists
#Creating a book object and inserting in the table
def createBooks(book):
    conn = sqlite3.connect("booksdb.db")
    c = conn.cursor()
    c.execute('''INSERT INTO books(id, name, cost) VALUES(?,?,?)''', (book))
    conn.commit()
    conn.close()
#Creating book list and inserting in the books(table)
def createBooksList():
    booksList = []
    booksList.append((1, "Python for dummies", 100.20))
    booksList.append((2, "Learn Python the Hard way", 50.9))
    booksList.append((3, "Python Crash Course", 20.0))
    #Iteration to add each book in creatBooks(book) a function
    for book in booksList:
        createBooks(book)




    print("Added in the table")
#Deling rows
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

def showEntries():
    conn = sqlite3.connect('booksdb.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM users''')
    print(c.fetchall())

# createDB()
# createBooksList()
