WITH UserMovieCount AS (
    SELECT
        u.name AS user_name,
        COUNT(DISTINCT mr.movie_id) AS movie_count
    FROM
        Users u
    JOIN
        MovieRating mr
    ON
        u.user_id = mr.user_id
    GROUP BY
        u.name
),
TopUser AS (
    SELECT
        user_name
    FROM
        UserMovieCount
    ORDER BY
        movie_count DESC,
        user_name ASC
    LIMIT 1
),
MovieAvgRating AS (
    SELECT
        m.title AS movie_title,
        AVG(mr.rating) AS avg_rating
    FROM
        Movies m
    JOIN
        MovieRating mr
    ON
        m.movie_id = mr.movie_id
    WHERE
        mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY
        m.title
),
TopMovie AS (
    SELECT
        movie_title
    FROM
        MovieAvgRating
    ORDER BY
        avg_rating DESC,
        movie_title ASC
    LIMIT 1
)
SELECT
    (SELECT user_name FROM TopUser) AS results
UNION ALL
SELECT
    (SELECT movie_title FROM TopMovie) AS results;
