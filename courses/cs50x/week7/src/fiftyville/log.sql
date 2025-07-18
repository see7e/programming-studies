-- Keep a log of any SQL queries you execute as you solve the mystery.

-- view the size of the reports
SELECT COUNT(*) FROM crime_scene_reports;

-- view the entire reports
SELECT * FROM crime_scene_reports;

-- view reports on July 28, 2021 and on Humphrey Street
SELECT * FROM crime_scene_reports
WHERE day = 28 AND month = 7 AND year = 2021;

/*
+-----+------+-------+-----+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| id  | year | month | day |     street      |                                                                                                       description                                                                                                        |
+-----+------+-------+-----+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 293 | 2021 | 7     | 28  | Axmark Road     | Vandalism took place at 12:04. No known witnesses.                                                                                                                                                                       |
| 294 | 2021 | 7     | 28  | Boyce Avenue    | Shoplifting took place at 03:01. Two people witnessed the event.                                                                                                                                                         |
| 295 | 2021 | 7     | 28  | Humphrey Street | Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |
| 296 | 2021 | 7     | 28  | Widenius Street | Money laundering took place at 20:30. No known witnesses.                                                                                                                                                                |
| 297 | 2021 | 7     | 28  | Humphrey Street | Littering took place at 16:36. No known witnesses.                                                                                                                                                                       |
+-----+------+-------+-----+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+*/

-- find the bakery
SELECT * FROM interviews WHERE transcript LIKE '%bakery%';
/*
+-----+---------+------+-------+-----+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| id  |  name   | year | month | day |                                                                                                                                                     transcript                                                                                                                                                      |
+-----+---------+------+-------+-----+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 161 | Ruth    | 2021 | 7     | 28  | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
| 162 | Eugene  | 2021 | 7     | 28  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
| 163 | Raymond | 2021 | 7     | 28  | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |
| 192 | Kiana   | 2021 | 5     | 17  | I saw Richard take a bite out of his pastry at the bakery before his pastry was stolen from him.                                                                                                                                                                                                                    |
+-----+---------+------+-------+-----+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+*/

/* LEADS:
- bakery parking lot
- ATM on Leggett Street
- earliest flight out of Fiftyville tomorrow */


-- bakery
SELECT * FROM bakery_security_logs
WHERE day = 28 AND month = 7 AND year = 2021
AND hour = 10 AND minute <= 25
AND activity = 'exit';
/*
+-----+------+-------+-----+------+--------+----------+---------------+
| id  | year | month | day | hour | minute | activity | license_plate |
+-----+------+-------+-----+------+--------+----------+---------------+
| 260 | 2021 | 7     | 28  | 10   | 16     | exit     | 5P2BI95       |
| 261 | 2021 | 7     | 28  | 10   | 18     | exit     | 94KL13X       |
| 262 | 2021 | 7     | 28  | 10   | 18     | exit     | 6P58WS2       |
| 263 | 2021 | 7     | 28  | 10   | 19     | exit     | 4328GD8       |
| 264 | 2021 | 7     | 28  | 10   | 20     | exit     | G412CB7       |
| 265 | 2021 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       |
| 266 | 2021 | 7     | 28  | 10   | 23     | exit     | 322W7JE       |
| 267 | 2021 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       |
+-----+------+-------+-----+------+--------+----------+---------------+

check plate owners*/

-- ATM
SELECT * FROM atm_transactions
WHERE day = 28 AND month = 7 AND year = 2021
AND atm_location = 'Leggett Street'
AND transaction_type = 'withdraw';
/*
+-----+----------------+------+-------+-----+----------------+------------------+--------+
| id  | account_number | year | month | day |  atm_location  | transaction_type | amount |
+-----+----------------+------+-------+-----+----------------+------------------+--------+
| 246 | 28500762       | 2021 | 7     | 28  | Leggett Street | withdraw         | 48     |
| 264 | 28296815       | 2021 | 7     | 28  | Leggett Street | withdraw         | 20     |
| 266 | 76054385       | 2021 | 7     | 28  | Leggett Street | withdraw         | 60     |
| 267 | 49610011       | 2021 | 7     | 28  | Leggett Street | withdraw         | 50     |
| 269 | 16153065       | 2021 | 7     | 28  | Leggett Street | withdraw         | 80     |
| 288 | 25506511       | 2021 | 7     | 28  | Leggett Street | withdraw         | 20     |
| 313 | 81061156       | 2021 | 7     | 28  | Leggett Street | withdraw         | 30     |
| 336 | 26013199       | 2021 | 7     | 28  | Leggett Street | withdraw         | 35     |
+-----+----------------+------+-------+-----+----------------+------------------+--------+

check acc_nbr owners*/

-- cross acc_nbr owners w/ plate owners
SELECT people.*, logs.hour, logs.minute FROM people
JOIN (
    SELECT license_plate, hour, minute
    FROM bakery_security_logs
    WHERE day = 28 AND month = 7 AND year = 2021
    AND hour = 10 AND minute <= 25
    AND activity = 'exit'
) AS logs ON people.license_plate = logs.license_plate
WHERE people.id IN (
    SELECT person_id FROM bank_accounts
    WHERE account_number IN (
        SELECT account_number FROM atm_transactions
        WHERE day = 28 AND month = 7 AND year = 2021
        AND atm_location = 'Leggett Street'
        AND transaction_type = 'withdraw'
    )
)
ORDER BY logs.minute;

/*
+--------+-------+----------------+-----------------+---------------+------+--------+
|   id   | name  |  phone_number  | passport_number | license_plate | hour | minute |
+--------+-------+----------------+-----------------+---------------+------+--------+
| 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       | 10   | 18     |
| 467400 | Luca  | (389) 555-5198 | 8496433585      | 4328GD8       | 10   | 19     |
| 396669 | Iman  | (829) 555-5269 | 7049073643      | L93JTIZ       | 10   | 21     |
| 514354 | Diana | (770) 555-1861 | 3592750733      | 322W7JE       | 10   | 23     |
+--------+-------+----------------+-----------------+---------------+------+--------+*/

-- phonecalls
SELECT * FROM phone_calls
WHERE day = 28 AND month = 7 AND year = 2021

AND caller is '(367) 555-5533'; -- Bruce
/*
+-----+----------------+----------------+------+-------+-----+----------+
| id  |     caller     |    receiver    | year | month | day | duration |
+-----+----------------+----------------+------+-------+-----+----------+
| 233 | (367) 555-5533 | (375) 555-8161 | 2021 | 7     | 28  | 45       |
| 236 | (367) 555-5533 | (344) 555-9601 | 2021 | 7     | 28  | 120      |
| 245 | (367) 555-5533 | (022) 555-4052 | 2021 | 7     | 28  | 241      |
| 285 | (367) 555-5533 | (704) 555-5790 | 2021 | 7     | 28  | 75       |
+-----+----------------+----------------+------+-------+-----+----------+*/
AND caller is '(389) 555-5198'; -- Luca
/**/
AND caller is '(829) 555-5269'; -- Iman
/**/
AND caller is '(770) 555-1861'; -- Diana
/*
+-----+----------------+----------------+------+-------+-----+----------+
| id  |     caller     |    receiver    | year | month | day | duration |
+-----+----------------+----------------+------+-------+-----+----------+
| 255 | (770) 555-1861 | (725) 555-3243 | 2021 | 7     | 28  | 49       |
+-----+----------------+----------------+------+-------+-----+----------+*/

-- SUSPECTS
SELECT people.*, logs.hour, logs.minute FROM people
JOIN (
    SELECT license_plate, hour, minute FROM bakery_security_logs
    WHERE day = 28 AND month = 7 AND year = 2021
    AND hour = 10 AND minute <= 25
    AND activity = 'exit'
) AS logs ON people.license_plate = logs.license_plate
WHERE people.id IN (
    SELECT person_id FROM bank_accounts
    WHERE account_number IN (
        SELECT account_number FROM atm_transactions
        WHERE day = 28 AND month = 7 AND year = 2021
        AND atm_location = 'Leggett Street'
        AND transaction_type = 'withdraw'
    )
)
AND people.phone_number IN (
    SELECT caller FROM phone_calls
    WHERE day = 28 AND month = 7 AND year = 2021
)
ORDER BY logs.minute;
/*
+--------+-------+----------------+-----------------+---------------+------+--------+
|   id   | name  |  phone_number  | passport_number | license_plate | hour | minute |
+--------+-------+----------------+-----------------+---------------+------+--------+
| 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       | 10   | 18     |
| 514354 | Diana | (770) 555-1861 | 3592750733      | 322W7JE       | 10   | 23     |
+--------+-------+----------------+-----------------+---------------+------+--------+*/


-- Fiftyville airport info

SELECT * FROM airports WHERE city = 'Fiftyville';
/*
+----+--------------+-----------------------------+------------+
| id | abbreviation |          full_name          |    city    |
+----+--------------+-----------------------------+------------+
| 8  | CSF          | Fiftyville Regional Airport | Fiftyville |
+----+--------------+-----------------------------+------------+*/

-- Find flights from CSF on 29-07-21
SELECT * FROM flights
WHERE day = 29 AND month = 7 AND year = 2021
AND origin_airport_id = 8
ORDER BY hour
LIMIT 1;
/*
+----+-------------------+------------------------+------+-------+-----+------+--------+
| id | origin_airport_id | destination_airport_id | year | month | day | hour | minute |
+----+-------------------+------------------------+------+-------+-----+------+--------+
| 36 | 8                 | 4                      | 2021 | 7     | 29  | 8    | 20     |
+----+-------------------+------------------------+------+-------+-----+------+--------+*/

-- find passgengers in flights - THIEF
SELECT people.name, passengers.seat FROM people
JOIN (
    SELECT passport_number, seat FROM passengers
    WHERE flight_id IN (
        SELECT id
        FROM flights
        WHERE day = 29 AND month = 7 AND year = 2021
        AND origin_airport_id = 8
        AND hour = 8
    )
) AS passengers ON people.passport_number = passengers.passport_number;
/*
+--------+------+
|  name  | seat |
+--------+------+
| Doris  | 2A   |
| Sofia  | 3B   |
| Bruce  | 4A   |<#
| Edward | 5C   |
| Kelsey | 6C   |
| Taylor | 6D   |
| Kenny  | 7A   |
| Luca   | 7B   |
+--------+------+*/

-- match the numbers of the past calls - ACCOMPLICE
SELECT name FROM people
WHERE phone_number IN (
    SELECT receiver FROM phone_calls
    WHERE day = 28 AND month = 7 AND year = 2021
    AND duration < 60
    AND caller is '(367) 555-5533' -- Bruce
);
/* bruce
+---------+
|  name   |
+---------+
| Robin   |
+---------+*/

-- find the city
SELECT city FROM airports
WHERE id IN (
    SELECT destination_airport_id FROM flights
    WHERE day = 29 AND month = 7 AND year = 2021
    AND origin_airport_id = 8
    ORDER BY hour
    LIMIT 1
);
/*
+---------------+
|     city      |
+---------------+
| New York City |
+---------------+*/