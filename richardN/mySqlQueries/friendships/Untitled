INSERT INTO users (first_name, last_name, created_at, updated_at)
VALUES ('Chris','Baker', NOW(), NOW() );

INSERT INTO users (first_name, last_name, created_at, updated_at)
VALUES ('Dianna','Smith', NOW(), NOW() );

INSERT INTO users (first_name, last_name, created_at, updated_at)
VALUES ('James','Johnson', NOW(), NOW() );

INSERT INTO users (first_name, last_name, created_at, updated_at)
VALUES ('Jessica','Davidson', NOW(), NOW() );

INSERT INTO friendships (users_id, friend_id)
VALUES(1,4);

INSERT INTO friendships (users_id, friend_id)
VALUES(2,1);

INSERT INTO friendships (users_id, friend_id)
VALUES(3,4);


SELECT users.first_name, users.last_name, users1.first_name AS friend_first_name, users1.last_name AS friend_last_name FROM users
LEFT JOIN friendships ON  users.id = friendships.users_id
LEFT JOIN users AS users1 ON friendships.friend_id = users1.id
ORDER BY friend_last_name;
