import sqlite3
import math
def addBookToCart(book):
    conn = sqlite3.connect("booksdb.db")
    c = conn.cursor()
    c.execute('''INSERT INTO cart (book_id) VALUES (?)''', (book,))
    conn.commit()
    conn.close()

def cartItems():
    conn = sqlite3.connect("booksdb.db")
    c = conn.cursor()
    c.execute('''SELECT book_id FROM cart''')
    cart_Book_ID = c.fetchall()
    book_cart = []
    for book in cart_Book_ID :
        c.execute('''SELECT name, cost, books.id from books INNER JOIN cart ON cart.book_id= books.id WHERE books.id = ?''', (book))
        books = c.fetchall()
       # book_cart.append(books)
        book_cart += books
    return book_cart

def cartList():
    conn = sqlite3.connect("booksdb.db")
    c = conn.cursor()
    c.execute('''SELECT book_id from cart ''')
    cartBookID = c.fetchall()
    cartLists = []
    for book in cartBookID:
        cartLists.append(book[0])
    return cartLists
def clearCart():
    conn = sqlite3.connect("booksdb.db")
    c = conn.cursor()
    c.execute("DELETE FROM cart")
    conn.commit()
    conn.close()
def removeCartItem(book):
    conn = sqlite3.connect("booksdb.db")
    c = conn.cursor()
    c.execute("DELETE FROM cart WHERE book_id = ?", (book,))

    conn.commit()
    conn.close()


def insertUser(username, password):
    conn = sqlite3.connect('booksdb.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO users(username, password ) VALUES (?,?)''', (username, password))
    conn.commit()
    conn.close()

def retreiveUsers():
    con = sqlite3.connect('booksdb.db')
    cur = con.cursor()
    cur.execute('''SELECT username, password FROM users''')
    users= cur.fetchall()
    con.close()
    return users


def userExists(uname):
    username= uname
    conn = sqlite3.connect('booksdb.db')
    c = conn.cursor()
    c.execute('''SELECT username FROM users WHERE username = ?''', (username,))
    data = c.fetchall()
    if len(data) == 0:
        return False
    else:
        print(username + "found in the database!")
        conn.close()
        return True




def getPassword(uname):
    uname = uname
    con = sqlite3.connect('booksdb.db')
    c = con.cursor()
    c.execute('''SELECT password FROM users WHERE username = ?''', (uname,))
    data = c.fetchall()
    d = data[0]
    con.close()
    return d[0]


def cartPriceTotal():
    conn = sqlite3.connect("booksdb.db")
    c = conn.cursor()
    c.execute('''SELECT cost from books INNER JOIN cart on cart.book_id = books.id''')
    costs = c.fetchall()
    totalcost = 0
    for cost in costs:
        cost= (cost[0])
        totalcost += cost

    return totalcost
