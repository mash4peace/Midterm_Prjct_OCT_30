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


