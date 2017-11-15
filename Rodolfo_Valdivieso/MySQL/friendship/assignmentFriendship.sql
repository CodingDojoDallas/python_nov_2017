
#INSERTING ROW INTO users
insert into users (first_name, last_name, created_at) values
            ('Chris'  ,'Baker'   ,now()),
			('Jessica','Davidson',now()),
			('Diana'  ,'Smith'   ,now()),
			('James'  ,'Johnson' ,now());
            
insert into friendships (user_id, friend_id, created_at) values
            ( 1 , 2  ,now()),
			( 1 , 4  ,now()),
			( 3 , 1  ,now()),
            ( 4 , 1  ,now()),
            ( 2 , 1  ,now());
            
insert into friendships (user_id, friend_id, created_at) values ( 1 , 3  ,now());
            
            
select a.first_name, a.last_name, c.first_name as fiend_first_name, c.last_name as friend_last_name
from users a join friendships b on a.id        = b.user_id
			 join users       c on b.friend_id = c.id
order by a.first_name;

