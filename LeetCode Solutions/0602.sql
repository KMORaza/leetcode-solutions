WITH FriendCounts AS (
    SELECT
        user_id,
        COUNT(*) AS friend_count
    FROM (
        SELECT requester_id AS user_id FROM RequestAccepted
        UNION ALL
        SELECT accepter_id AS user_id FROM RequestAccepted
    ) AS AllFriends
    GROUP BY user_id
),
MaxFriends AS (
    SELECT
        MAX(friend_count) AS max_friend_count
    FROM FriendCounts
)
SELECT
    user_id AS id,
    friend_count AS num
FROM FriendCounts
WHERE friend_count = (SELECT max_friend_count FROM MaxFriends);
