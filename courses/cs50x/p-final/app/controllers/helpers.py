import csv
import datetime
import pytz
import requests
import subprocess
import urllib
import uuid
import json

from flask import redirect, render_template, session
from functools import wraps

# 400 Bad Request
# 401 Unauthorized
# 402 Payment Required
# 403 Forbidden
# 404 Not Found
# 405 Method Not Allowed
# 406 Not Acceptable
# 408 Request Timeout
# 409 Conflict
# 410 Gone
# 500 Internal Server Error
# 501 Not Implemented
# 502 Bad Gateway
# 503 Service Unavailable
# 504 Gateway Timeout

# DEFINITIONS
type_list = ["", "Food", "Education", "Leisure Activities", "Health", "Transport"]

msg = {
    'titl': '',
    'desc': '',
    'cbtn': '',
    'stts': ''
}


# ADITIONAL FUNCTIONS
def apology(message, code=400):
    """Render message as an apology to user."""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def lookup(symbol):
    """Look up quote for symbol."""

    # Prepare API request
    symbol = symbol.upper()
    end = datetime.datetime.now(pytz.timezone("US/Eastern"))
    start = end - datetime.timedelta(days=7)

    # Yahoo Finance API
    url = (
        f"https://query1.finance.yahoo.com/v7/finance/download/{urllib.parse.quote_plus(symbol)}"
        f"?period1={int(start.timestamp())}"
        f"&period2={int(end.timestamp())}"
        f"&interval=1d&events=history&includeAdjustedClose=true"
    )

    # Query API
    try:
        response = requests.get(
            url,
            cookies={"session": str(uuid.uuid4())},
            headers={"User-Agent": "python-requests", "Accept": "*/*"},
        )
        response.raise_for_status()
        print(response)  # debug

        # CSV header: Date,Open,High,Low,Close,Adj Close,Volume
        quotes = list(csv.DictReader(response.content.decode("utf-8").splitlines()))
        quotes.reverse()
        price = round(float(quotes[0]["Adj Close"]), 2)
        return {"name": symbol, "price": price, "symbol": symbol}
    except (requests.RequestException, ValueError, KeyError, IndexError):
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"


def check_stock(db, symbol, name):
    # Check stock in register
    stock = db.execute("SELECT * FROM stocks WHERE symbol = ?;", symbol)

    if not stock:
        # If stock not registred, insert a new record
        db.execute("INSERT INTO stocks (symbol, name) VALUES (?, ?);", symbol, name)


class Expense:
    def __init__(self, year, month, day, type, desc, exvalue):
        self.year = year
        self.month = month
        self.day = day
        self.type = type
        self.desc = desc
        self.exvalue = exvalue

    def dataValidation(self):
        return all(
            getattr(self, field) is not None and getattr(self, field) != ''
            for field in ['year', 'month', 'day', 'type', 'desc', 'exvalue']
        )
        

""" class Db:
    def record(self, e):
        expense = Expense(
            year=e.year,
            month=e.month,
            day=e.day,
            type=e.type,
            desc=e.desc,
            exvalue=e.exvalue
        )
        db.session.add(expense)
        db.session.commit()

    def getAll(self):
        return Expense.query.all()

    def search(self, fields):
        query = Expense.query.filter_by(**fields.__dict__)
        return query.all()

    def remove(self, id):
        expense = Expense.query.get(id)
        if expense:
            db.session.delete(expense)
            db.session.commit() """