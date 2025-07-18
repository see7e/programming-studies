--  names of all people who starred in a movie in which Kevin Bacon also starred

SELECT DISTINCT p.name FROM people AS p
JOIN stars AS s1 ON p.id = s1.person_id
JOIN movies AS m1 ON s1.movie_id = m1.id
JOIN stars AS s2 ON m1.id = s2.movie_id
JOIN people AS p2 ON s2.person_id = p2.id
WHERE p2.name = 'Kevin Bacon';