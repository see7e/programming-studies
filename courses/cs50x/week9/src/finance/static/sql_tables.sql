/*-- Default ``users`` table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL, hash TEXT NOT NULL,
    cash NUMERIC NOT NULL DEFAULT 10000.00
);
CREATE TABLE sqlite_sequence(name,seq);
CREATE UNIQUE INDEX username ON users (username);
*/

CREATE TABLE stocks (
    stock_id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT NOT NULL,
    name TEXT NOT NULL
);
CREATE INDEX idx_symbol ON stocks (symbol);

CREATE TABLE hold (
    hold_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    stock_id INTEGER NOT NULL,
    shares INTEGER NOT NULL DEFAULT 0,
    price NUMERIC NOT NULL,
    total NUMERIC NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (stock_id) REFERENCES stocks (stock_id)
);
CREATE INDEX idx_user_id ON hold (user_id);
CREATE INDEX idx_stock_id ON hold (stock_id);


CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    stock_id INTEGER NOT NULL,
    shares INTEGER NOT NULL,
    price NUMERIC NOT NULL,
    transaction_type TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (stock_id) REFERENCES stocks (stock_id)
);
CREATE INDEX idx_transaction_id ON transactions (transaction_id);


/*
The ``users`` table stores user information, including their unique ID, username, hashed password
(``hash``), and available cash balance (``cash``).

The ``stocks`` table stores information about stocks that users own. It includes a unique ``stock_id``,
the user's ``username``, the stock ``symbol``, the number of shares owned (``shares``), and the current
stock ``price``.

The ``hold`` table is a junction table that links users and their stocks. It includes a unique
``hold_id``, the ``user_id``, the ``stock_id``, the number of shares held (``shares``), and the total
value of the stock (``total``). This table is used to track the relationship between users and the stocks
they own.

The ``transactions`` table stores historical transaction data for each user. It includes a unique
``transaction_id``, the ``user_id``, the stock ``symbol``, the number of shares involved in the
transaction (``shares``), the stock price at the time of the transaction (``price``), the
``transaction_type`` (e.g., "BUY" or "SELL"), and a ``timestamp`` to record when the transaction
occurred.

Note that the above SQL code assumes that you are using SQLite as the database engine. If you are
using a different database system, you may need to adjust the SQL code accordingly. After running
this SQL code, the database will be set up with the required tables, and you can proceed to use the
application as described in the provided code.
*/

SELECT stocks.symbol, stocks.name, stocks.price, hold.shares, hold.total FROM hold
    JOIN users ON hold.user_id = users.id
    JOIN stocks ON hold.stock_id = stocks.stock_id
    WHERE users.id = 1;


SELECT stocks.symbol, stocks.name, stocks.price, hold.shares, hold.total FROM hold
    JOIN users ON hold.user_id = users.id
    JOIN stocks ON hold.stock_id = stocks.stock_id
    WHERE users.id = 1;