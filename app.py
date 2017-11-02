from flask import Flask, render_template, flash, redirect, request
import database, dbFunctions

app = Flask(__name__)


@app.route('/')
def home():
    pythonBookLists = database.showBooks("%")
    cartItem = dbFunctions.cartItems()

    return render_template("home.html",pythonBookList = pythonBookLists)
@app.route("/save", methods=["Post"])
def saveSearch():
    bookName = request.form['bookNames']
    dbFunctions.addBookToCart(bookName)
    dbFunctions.cartItems()
    cartItems =dbFunctions.cartItems()
    books = list(cartItems)
    book_price =[book[1] for book in books]
    #print(book_price)
    total = sum(book_price)
    #import pprint
    #pp = pprint.PrettyPrinter(indent= 4)
   # pp.pprint(book_price)



    return render_template("book_ordered.html",cartItems = cartItems , total = total)
@app.route("/remove", methods=["Post"])
def removeCartItem():
    deletedBook =request.form("removeBookItem")
    #print(deletedBook)
    dbFunctions.removeCartItem(deletedBook)
    return redirect ("/")
@app.route("/delete", methods=['POST'])
def clearCart():
    dbFunctions.clearCart()
    return redirect("/")
@app.route("/checkout", methods=["POST"])
def checkout():
    return render_template("customerInfo.html")
@app.route("//sumbit", methods=["POST"])
def finish():
    #submit = request.form("submit")
    flash("Thanks , you have completed the order")
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug= True)
