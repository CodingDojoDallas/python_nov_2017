select first_name, last_name, email, address
from customer
join address on customer.customer_id = address.address_id
where city_id = 312;

select title, description, release_year, rating, special_features, category.name as genre
from film
join film_category on film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id
where category.name = "comedy";

select actor.actor_id, concat_ws(" ",actor.first_name, actor.last_name) as actor_name, title, description, release_year
from film
join film_actor on film.film_id = film_actor.film_id
join actor on film_actor.actor_id = actor.actor_id
where actor.actor_id = 5;

select  first_name, last_name, email, address
from customer
join address on customer.address_id = address.address_id
join city on address.city_id = city.city_id
where store_id = 1 and city.city_id in (1, 42, 312, 459);

select title, description, release_year, rating, special_features
from film
join film_actor on film.film_id = film_actor.film_id
join actor on film_actor.actor_id = actor.actor_id
Where rating = "G" and actor.actor_id = 15 and special_features LIKE "%Behind the Scenes%";

select actor.actor_id, concat(actor.first_name, " ", actor.last_name), actor.last_update
from film
join film_actor on film.film_id = film_actor.film_id
join actor on film_actor.actor_id = actor.actor_id
where film.film_id = 369;

select title, description, release_year, rating, special_features, category.name as genre, rental_rate
from film
join film_category on film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id
where category.name = "Drama" and rental_rate = 2.99;

select actor.actor_id, concat(actor.first_name, " ", actor.last_name) as actor_name, film.film_id, title, description, release_year, rating, special_features, category.name as genre
from film
join film_actor on film.film_id = film_actor.film_id
join actor on film_actor.actor_id = actor.actor_id
join film_category on film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id
where actor.first_name = "Sandra" and actor.last_name = "Kilmer" and category.name = "Action";