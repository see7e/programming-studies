/* The ``users`` table stores user information, including their unique ID, username, hashed password
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

-- Step 1: Create the user table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    hashed_password CHAR(64) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE sqlite_sequence(name,seq);
CREATE UNIQUE INDEX username ON users (username);

/* -- Step 2: Implement security procedures
-- 2.1 Hashing Passwords: Use a one-way hash function to store hashed passwords
-- (Replace 'your_preferred_hashing_algorithm' with a suitable hashing algorithm like bcrypt or SHA-256)
CREATE FUNCTION HashPassword(password VARCHAR(100))
RETURNS CHAR(64)
DETERMINISTIC
BEGIN
    RETURN SHA2(password, 256);
END;

-- 2.2 Insert Trigger: Automatically hash passwords before inserting into the table
DELIMITER //
CREATE TRIGGER BeforeUserInsert
BEFORE INSERT ON users
FOR EACH ROW
BEGIN
    SET NEW.hashed_password = HashPassword(NEW.hashed_password);
END;
//
DELIMITER ;

-- 2.3 Update Trigger: Do not allow updating hashed passwords directly
DELIMITER //
CREATE TRIGGER BeforeUserUpdate
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.hashed_password <> OLD.hashed_password THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Password updates are not allowed.';
    END IF;
END;
//
DELIMITER ;

-- 2.4 User Privileges: Grant minimum required privileges to database users
-- Replace 'your_username' with the actual username and 'your_password' with the corresponding password
GRANT SELECT, INSERT ON your_database.users TO 'your_username'@'localhost' IDENTIFIED BY 'your_password';

-- 2.5 Remove default privileges for others (optional)
-- This step revokes unnecessary privileges from public users on the 'users' table
REVOKE ALL PRIVILEGES ON your_database.users FROM PUBLIC;

-- Step 3: (Optional) Use a strong password for your database root user and limit remote access if necessary.

-- Step 4: (Optional) Regularly update and patch the database system for security fixes.

-- Step 5: (Optional) Implement SSL/TLS encryption for client-server communication.

-- Step 6: (Optional) Regularly backup the database to protect against data loss.

-- Note: The exact syntax and functionalities may vary based on the SQL database management system you are using. The provided example is for MySQL.
 */


-- Stocks Management
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


-- Expenses Management
CREATE TABLE expenses (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    expense_year INTEGER NOT NULL,
    expense_month INTEGER NOT NULL,
    expense_day INTEGER NOT NULL,
    type TEXT  NOT NULL,
    desc TEXT  NOT NULL,
    value NUMERIC NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
CREATE INDEX idx_expenses_id ON expenses (expense_id);
