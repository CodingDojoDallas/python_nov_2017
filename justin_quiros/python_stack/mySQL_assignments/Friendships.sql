SELECT * FROM users
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as user2 ON users.id = friendships.user_id

