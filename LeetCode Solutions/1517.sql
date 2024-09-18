SELECT user_id, name, mail
FROM Users
WHERE mail LIKE '%@leetcode.com'
  AND LENGTH(mail) - LENGTH(REPLACE(mail, '@', '')) = 1
  AND LEFT(mail, 1) REGEXP '^[a-zA-Z]'
  AND SUBSTRING_INDEX(mail, '@', 1) REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*$';
