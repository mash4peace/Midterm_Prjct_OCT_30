from flask import Flask, render_template, flash, redirect, request, session, url_for
import os
import database, dbFunctions

app = Flask(__name__)

#Here is the home page
@app.route('/')
def home():
    #Loading books in the brwoser
    pythonBookLists = database.showBooks("%")
    #Calling dbFunction to get carItems function
    total = dbFunctions.cartPriceTotal()
    cartItem = dbFunctions.cartItems()
    #Retutns the templates
    return render_template("home.html",pythonBookList = pythonBookLists,cartItems = cartItem , total = total)
#Save Searching for the user in session
@app.route("/save", methods=["Post"])
def saveSearch():
    #bookName is in the html
    bookName = request.form['bookNames']
    dbFunctions.addBookToCart(bookName)
    dbFunctions.cartItems()
    cartItems =dbFunctions.cartItems()
    books = list(cartItems)
    book_price =[book[1] for book in books]
    #print(book_price)
    total = sum(book_price) #Making a total total
    #import pprint
    #pp = pprint.PrettyPrinter(indent= 4)
   # pp.pprint(book_price)



    #return render_template("book_ordered.html",cartItems = cartItems , total = total)
    return redirect("/")
   # return re("/", cartItems = cartItems, total = total)
#Remove cart by cartID
@app.route("/remove", methods=["Post"])
def removeCartItem():
    deletedBook =request.form("removeBookItem")
    #print(deletedBook)
    dbFunctions.removeCartItem(deletedBook)
    delAbook = dbFunctions.removeCartItem(deletedBook)
    book = list(delAbook)
    print(book)

    return redirect ("/",removeBookItem= deletedBook )
#Clearing all items in the cart
@app.route("/delete", methods=['POST'] )
def clearCart():
    dbFunctions.clearCart()
    return redirect("/")
#Checkout route
@app.route("/checkout", methods=["POST"])
def checkout():
    return render_template("customerInfo.html")
@app.route("//sumbit", methods=["POST"])
def finish():
    #submit = request.form("submit")
    flash("Thanks , you have completed the order")
    return render_template("home.html")
"""
def user():

    if 'username' in session:
        username = session['username']
        if request.method== 'POST':
           return render_template('order.html')

    return render_template('user.html')
@app.route("/customer", methods=['GET', 'POST'])
def index():
    if 'username' in session:
        return redirect(url_for('user'))
    else:
        message = None

        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            # if enterd username exists
            if dbFunctions.userExists(username) == True:
                if dbFunctions.getPassword(username) == password:
                    session['username'] = username
                    return render_template("order.html")
                else:
                    message = "INVALID PASSWORD"

                    return render_template('index.html')
        else:
            message = "user doesnt exist"
            return render_template('index.html', message= message)


    return render_template('user.html', message = message)
@app.route('/registration', methods=['GET', "POST"])
def registeraion():
    messages = []
    if request.method== 'POST':
        username = request.form['username']
        password= request.form['password']

        if len(username)<4:
            messages.append("Invalid username. Username must be between at leat 4 characters in length!")
        if len(username)>20:
            messages.append("Invalid Username. Your username is too long , Please use 20 characters maximum ")

        if len(password) < 4:
            messages.append("Invalid Password. Username must be between at leat 4 characters in length!")
        if len(password) > 20:
            messages.append("Invalid Password. Your username is too long , Please use 20 characters maximum ")
        if len(messages)!= 0:
            return render_template('registeration.html', messages = messages)

        if dbFunctions.userExists(username) == True:
            messages.append("Username already exists!!")
            return render_template('registeration.html', messages = messages)
        else:
            dbFunctions.insertUser(username, password)
            session['username'] = username
            return redirect(url_for('user'))
    else:
        return render_template('registeration.html', messages = messages)


"""

if __name__ == '__main__':
    app.secret_key= os.urandom(13)
    app.run(debug= True)
