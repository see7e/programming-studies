import os, sys

from cs50 import SQL # inside CS50x enviorment

# Flask
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp

# Security
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash

# Modules
from app.controllers.helpers import (
    apology, login_required, lookup, usd, check_stock, 
    Expense, type_list, msg
)

# Configure application
from app import app

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
""" SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY """
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///yourfinance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""

    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Routes
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form.get("email")
        return render_template("register.html", email=email)
    else:
        return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """This function handles user login. It first clears any existing user ``session``.

    -   If the ``request`` method is POST, it checks if the ``username`` and ``password`` were
        provided. If not, it returns an apology message.
    -   It then queries the database to find the user with the given ``username`` and verifies the
        ``password`` using the ``check_password_hash()`` function from ``werkzeug.security``.
    -   If the login is successful, the user's ID is stored in the ``session``, and then redirects
        to the home page.
        If the login fails, an apology message is displayed.
    """

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users\
            WHERE username = ?;",
            request.form.get("username"),
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        """ADICIONAR SINCRONIZAÇÃO DE DADOS"""
        return render_template("login.html")


@app.route("/logout")
def logout():
    """This function logs the user out and redirects them to the login form."""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """This function handles user registration.

    -   If the request method is ``POST``, it takes the ``username``, ``password``, and ``confirmation``
        ``confirmation`` from the form data.
    -   It checks if all the necessary fields are provided, if the ``password`` and ``confirmation``
        match, and if the ``username`` is not already taken (by querying the database).
    -   If the registration is successful, it creates a new user in the database with the hashed
        ``password`` and redirects the user to the home page.
    -   If any of the checks fail, an apology message is displayed.
    -   If the request method is GET, it renders the ``register.html`` template, where the user can
        input their registration details.
    """
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Must provide username")
        elif not password:
            return apology("Must provide password")
        elif password != confirmation:
            return apology("Password doesn't match")

        # Check if username already exists
        rows = db.execute("SELECT * FROM users WHERE username = ?;", username)
        if rows:
            return apology("Username already exists")

        # Creates the hash for the password
        hashed_password = generate_password_hash(password)
        
        # Insert new user into the database
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?);", username, hashed_password)

        # Go to Home
        return redirect("/")

    else:
        return render_template("register.html")


# Udemy routes
@app.route("/new", methods=['GET', 'POST'])
@login_required
def new_expenses():
    if request.method == "POST":
        user_id = session["user_id"]

        year = request.form.get('year')
        month = request.form.get('month')
        day = request.form.get('day')
        type = request.form.get('type')
        desc = request.form.get('desc')
        exvalue = request.form.get('exvalue')
        
        #expense = Expense(year, month, day, type, desc, exvalue)
        #if expense.dataValidation():
        try:
            # CREATE
            db.execute("INSERT INTO expenses ( \
                            user_id, expense_year, expense_month, expense_day, type, desc, value \
                    ) \
                        VALUES (?, ?, ?, ?, ?, ?, ?);",
                        user_id, int(year), int(month), int(day), type, desc, int(exvalue))

            msg['titl'] = 'Recording Success'
            msg['desc'] = 'Expense saved with success!'
            msg['mbtn'] = 'Close'
            msg['stts'] = 'success'
            return render_template("new.html", types=type_list, msg=msg)
        
        except TypeError:
            msg['titl'] = 'Recording error'
            msg['desc'] = 'There are mandatory fields that have not been filled in.'
            msg['mbtn'] = 'Go back and fix'
            msg['stts'] = 'error'
            return render_template("new.html", types=type_list, msg=msg)
    else:
        return render_template("new.html", types=type_list)


@app.route("/list", methods=['GET', 'POST'])
@login_required
def list_expenses():
    if request.method == "POST":
            user_id = session["user_id"]

            year = request.form.get('year')
            month = request.form.get('month')
            day = request.form.get('day')
            type = request.form.get('type')
            desc = request.form.get('desc')
            exvalue = request.form.get('exvalue')

            # RETRIEVE
            rows = db.execute("SELECT * FROM expenses \
                                WHERE( \
                                    user_id = ? OR \
                                    expense_year = ? OR \
                                    expense_month = ? OR \
                                    expense_day = ? OR \
                                    type = ? OR \
                                    desc = ? OR \
                                    value = ? \
                                );",
                                user_id, year, month, day, type, desc, exvalue)

            return render_template("list.html", types=type_list, msg=msg, data=rows)

            # UPDATE
            # DELETE
    else:
        user_id = session["user_id"]
        rows = db.execute("SELECT * FROM expenses WHERE user_id = ?;", user_id)
        return render_template("list.html", types=type_list, data=rows)


# CS50 routes
@app.route("/portifolio")
@login_required
def portifolio():
    """This function is used to display the user's portfolio of stocks.

    It retrieves information about the stocks the user holds from the database and calculates the
    total value of each stock (``shares`` * ``price``) and the total value of the entire portfolio
    (sum of individual stock values + ``cash``).

    The function returns the rendered ``portfolio.html`` template, passing the necessary data to be
    displayed in the table.
    """
    # User identification
    user_id = session["user_id"]

    # Verify current stock value and update each accumulated value

    # Fetch user's portfolio data from the database
    data = db.execute(
        "SELECT s.symbol, s.name, h.shares, h.price, h.total FROM hold h \
        JOIN stocks s ON h.stock_id = s.stock_id \
        WHERE h.user_id = ?;",
        user_id,
    )

    # Fetch user's cash balance from the database
    cash = db.execute("SELECT cash FROM users WHERE id = ?;", user_id)[0]["cash"]

    # Calculate the current total value of the portfolio
    current = cash + sum(row["total"] for row in data)

    return render_template("portifolio.html", rows=data, cash=cash, total_value=current)


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """This function is used to get a stock quote for a given ``symbol``.

    -   If the request method is ``POST``, it takes the ``symbol`` from the form data, calls the
        ``lookup()`` function (which is missing from the provided code but is likely a function that
        fetches stock data from an external source based on the ``symbol``), and returns the stock
        data in ``JSON`` format using ``jsonify``.
    -   If the request method is GET, it renders the ``quote.html`` template, where the user can
        input a stock ``symbol``.

    Aditionaly it's important to handle potential errors that may arise when looking up stock data
    using the ``lookup()`` function.
    """

    if request.method == "POST":
        symbol = request.form.get("symbol")
        # timespan = int(request.form.get('timespan', 7))  # Default to 7 days if not provided by the user
        stock_data = lookup(symbol)

        if not stock_data:
            return apology("Stock data not found")

        # Extract required values from stock_data JSON
        name = stock_data["name"]
        price = stock_data["price"]
        symbol = stock_data["symbol"]
        # historical_data = stock_data["historical_data"]

        # Check stock in register
        check_stock(db, symbol, name)

        # Format the price as USD
        formatted_price = usd(price)

        # Update the <p> tag in the template with the stock information
        stock_info = f"A share of {name} ({symbol}) costs {formatted_price}."
        # return render_template("quote.html", stock_info=stock_info, historical_data=historical_data)
        return render_template("quote.html", stock_info=stock_info)

    else:
        return render_template("quote.html")


@app.route("/history")
@login_required
def history():
    """This function show the history of the user's ``transactions``.

    It fetches the transaction history from the database for the currently logged-in user and
    renders the ``history.html`` template, passing the ``transactions`` data to display in the
    template.
    """

    # Fetch the user's transaction history from the database
    user_id = session["user_id"]
    transactions = db.execute("SELECT * FROM transactions WHERE user_id = ?;", user_id)

    return render_template("history.html", transactions=transactions)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """This function allows the user to buy ``shares`` of a stock.

    -   If the ``request`` method is ``POST``, it fetches the ``symbol`` and number of ``shares``
        from the form data and calls the lookup function (which is missing from the provided code)
        to get the stock data.
    -   It checks if the stock data is available and if the number of ``shares`` is positive. If any
        of these conditions fail, an apology message is displayed.
    -   If the data is valid, it calls the ``order()`` function (which is missing from the provided
        code but likely handles the order placement logic) with the "buy" action and the stock data.
    -   It then fetches the user's data from the database, calculates the ``cost`` of the
        transaction,and checks if the user has enough cash to complete the transaction. If not, an
        apology message is displayed.
    -   If the user has enough cash, the transaction is executed: the user's cash is updated, and
        the number of ``stocks`` owned by the user is adjusted in the database.

    Finally, the user is redirected to the home page. If the ``request`` method is GET, it renders
    the "buy.html" template, where the user can input the stock ``symbol`` and number of ``shares``
    they want to buy.
    """

    if request.method == "POST":
        # Stock symbol
        symbol = request.form.get("symbol")
        # Shares
        try:
            shares = int(request.form.get("shares"))
        except (TypeError, ValueError):
            return apology("You cannot buy fractions shares")

        # API info
        stock_data = lookup(symbol)
        try:
            name = stock_data["name"]
            symbol = stock_data["symbol"]
            price = stock_data["price"]
        except TypeError:
            return apology("You must specify a valid stock ticket")

        # Check stock in register
        check_stock(db, symbol, name)
        stock_id = db.execute("SELECT stock_id FROM stocks WHERE symbol = ?;", symbol)[
            0
        ]["stock_id"]

        if not stock_data:
            return apology("Stock data not found")
        elif shares < 1:
            return apology("Should try a positive number of shares")
        else:
            # Calculate the total cost of the purchase
            cost = price * shares

            # Fetch user's cash balance from the database
            user_id = session["user_id"]
            user = db.execute("SELECT cash FROM users WHERE id = ?;", user_id)
            cash = user[0]["cash"]

            # Check if the user has enough cash for the purchase
            if cost > cash:
                return apology("Not enough money for this transaction")
            else:
                # Check if the user already holds this stock
                stock = db.execute(
                    "SELECT * FROM hold WHERE user_id = ? AND stock_id = ?;",
                    user_id,
                    stock_id,
                )

                # Update the user's portfolio in the 'hold' table
                if not stock:
                    # If the user does not hold this stock, insert a new record
                    db.execute(
                        "INSERT INTO hold (user_id, stock_id, shares, price, total) VALUES (?, ?, ?, ?, ?);",
                        user_id,
                        stock_id,
                        shares,
                        price,
                        cost
                    )
                else:
                    # If the user already holds this stock, update the existing record
                    total_shares = stock[0]["shares"] + shares
                    total_cost = stock[0]["total"] + cost
                    db.execute(
                        "UPDATE hold SET shares = ?, total = ? WHERE user_id = ? AND stock_id = ?;",
                        total_shares,
                        total_cost,
                        user_id,
                        stock_id
                    )

                # Deduct the cost from the user's cash
                remaining_cash = cash - cost
                db.execute(
                    "UPDATE users SET cash = ? WHERE id = ?;", remaining_cash, user_id
                )

                # Insert the transaction record into the 'transactions' table
                db.execute(
                    "INSERT INTO transactions (user_id, stock_id, shares, price, transaction_type) \
                    VALUES (?, ?, ?, ?, ?);",
                    user_id,
                    stock_id,
                    shares,
                    price,
                    "BUY"
                )

                # Redirect to the homepage after the successful purchase
                return redirect("/portifolio")
    else:  # for GET method
        return render_template("buy.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """This function is intended to allow the user to sell shares of a stock.

    The above implementation allows the user to sell shares of a stock. If the request method is
    ``POST``, it fetches the stock ``symbol`` and the number of ``shares_to_sell`` from the form
    data. It then verifies the stock data, checks if the user has enough ``shares_to_sell``, and
    calculates the ``amount_received`` from selling the shares. The user's cash balance and stock
    holdings are then updated in the database, and the transaction is added to the history. Finally,
    a success message is flashed, and the user is redirected to the home page.

    If the request method is ``GET``, the implementation fetches the symbols of the ``stocks`` the
    user owns (with positive share holdings) from the database and renders the "sell.html" template,
    passing the symbols data to display in the dropdown for selecting the stock ``symbol`` to sell.
    """

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares_to_sell = int(request.form.get("shares"))

        # API info
        stock_data = lookup(symbol)
        name = stock_data["name"]
        price = stock_data["price"]
        symbol = stock_data["symbol"]

        # Check stock in register
        check_stock(db, symbol, name)
        stock_id = db.execute("SELECT stock_id FROM stocks WHERE symbol = ?;", symbol)[
            0
        ]["stock_id"]

        if not stock_data:
            return apology("Stock data not found")
        elif shares_to_sell < 1:
            return apology("Should try a positive number of shares")

        # Fetch user's portfolio information from the 'hold' table
        user_id = session["user_id"]
        stock_holding = db.execute(
            "SELECT * FROM hold WHERE user_id = ? AND stock_id = ?;", user_id, stock_id
        )

        if not stock_holding or stock_holding[0]["shares"] < shares_to_sell:
            return apology("Not enough shares to sell")

        # Calculate the total value of the shares to sell
        total_value = stock_data["price"] * shares_to_sell

        # Update the user's cash balance
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?;", user_id)[0][
            "cash"
        ]
        updated_cash = user_cash + total_value
        db.execute("UPDATE users SET cash = ? WHERE id = ?;", updated_cash, user_id)

        # Update the user's portfolio in the 'hold' table
        updated_shares = stock_holding[0]["shares"] - shares_to_sell
        updated_total = stock_data["price"] * updated_shares
        db.execute(
            "UPDATE hold SET shares = ?, total = ? WHERE user_id = ? AND stock_id = ?;",
            updated_shares,
            updated_total,
            user_id,
            stock_id,
        )

        # Insert the transaction record into the 'transactions' table
        db.execute(
            "INSERT INTO transactions (user_id, stock_id, shares, price, transaction_type) \
            VALUES (?, ?, ?, ?, ?);",
            user_id,
            stock_id,
            -shares_to_sell,
            stock_data["price"],
            "SELL"
        )

        # Redirect to the homepage after the successful sell
        return redirect("/portifolio")

    else:  # for GET method
        # Fetch user's portfolio data from the 'hold' table
        user_id = session["user_id"]
        data = db.execute(
            "SELECT s.symbol, s.name, h.shares FROM hold h \
            JOIN stocks s ON h.stock_id = s.stock_id \
            WHERE h.user_id = ?;",
            user_id
        )

        return render_template("sell.html", portfolio_data=data)
