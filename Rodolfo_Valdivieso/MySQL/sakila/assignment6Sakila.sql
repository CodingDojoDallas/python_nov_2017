#1)
select b.city_id, c.city, a.first_name, a.last_name, a.email, b.address
from customer a join address b on a.address_id = b.address_id
				join city    c on b.city_id = c.city_id
where b.city_id = 312;

#2)
select a.film_id, a.title, a.description, a.release_year, a.rating, a.special_features, c.name as genre
from film a join film_category b on a.film_id     = b.film_id
            join category      c on b.category_id = c.category_id 
where c.name = 'Comedy';

#3)
select c.actor_id, concat(c.first_name, ' ', c.last_name), a.film_id, a.title, a.description, a.release_year
from film a join film_actor b on a.film_id  = b.film_id
			join actor      c on b.actor_id = c.actor_id
where c.actor_id = 5;

#4)
select b.store_id, d.city_id, a.first_name, a.last_name, a.email, c.address
from customer a join store   b on a.store_id   = b.store_id
                join address c on a.address_id = c.address_id
                join city    d on c.city_id    = d.city_id
where b.store_id = 1 and d.city_id in (1, 42, 312, 459);

#5)
select a.title, a.description, a.release_year, a.rating, a.special_features
from film a join film_actor b on a.film_id  = b.film_id
            join actor      c on b.actor_id = c.actor_id
where a.rating = 'G' and a.special_features like '%Behind the Scenes' and c.actor_id = 15;

#6)
select a.film_id, a.title, c.actor_id, concat(c.first_name, ' ', c.last_name) as actor_name
from film a join film_actor b on a.film_id  = b.film_id
            join actor      c on b.actor_id = c.actor_id
where a.film_id=369;


#7)
select a.film_id, a.title, a.description, a.release_year, a.rating, a.special_features, c.name as genre, a.rental_rate
from film a join film_category b on a.film_id     = b.film_id
            join category      c on b.category_id = c.category_id
where c.name = 'Drama' and a.rental_rate = 2.99;


#8)
select e.actor_id, concat(e.first_name, ' ', e.last_name) as actor_name, a.film_id, a.title, a.description, a.release_year, a.rating, a.special_features, c.name as genre
from film a join film_category b on a.film_id     = b.film_id
            join category      c on b.category_id = c.category_id
            join film_actor    d on a.film_id     = d.film_id
            join actor         e on d.actor_id    = e.actor_id
where c.name = 'Action' and e.first_name = 'SANDRA' and e.last_name = 'KILMER';


