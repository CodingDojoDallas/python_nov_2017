/*Q1 What query would you run to get all the customers inside city_id = 312? 
Your query should return customer first name, last name, email, and address.*/
SELECT city.city_id ,city.city ,customer.first_name,customer.last_name,customer.email,address.address
FROM city JOIN address ON city.city_id = address.city_id 
JOIN customer ON address.address_id = customer.address_id
WHERE city.city_id = 312;

/*Q2 What query would you run to get all comedy films? Your query should return film title, 
description, release year, rating, special features, and genre (category).*/
SELECT film.film_id,film.title,film.description,film.release_year,film.rating,film.special_features,category.name
FROM film JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id = film_category.category_id
WHERE category.name = 'Comedy';

/*Q3 What query would you run to get all the films joined by actor_id=5? 
Your query should return the actor id, actor name, film title, description, and release year.*/
SELECT actor.actor_id,CONCAT(actor.first_name,'',actor.last_name) AS actor_name ,film.film_id,film.title,film.description,film.release_year
FROM film JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE actor.actor_id = 5;

/*Q4 What query would you run to get all the customers in store_id = 1 and inside these 
cities (1, 42, 312 and 459)? Your query should return customer first name, last name, email,and address.*/ 
SELECT store.store_id, city.city_id,customer.first_name,customer.last_name,customer.email,address.address
FROM customer JOIN store ON store.store_id = customer.store_id
JOIN address ON address.address_id = customer.address_id
JOIN city ON city.city_id = address.city_id
WHERE customer.store_id = 1 AND city.city_id in (1, 42, 312, 459);

/*Q5  What query would you run to get all the films with a "rating = G" and "special feature = behind 
the scenes", joined by actor_id = 15? Your query should return the film title, description, release year, 
rating, and special feature. Hint: You may use LIKE function in getting the 'behind the scenes' part.*/
SELECT film.title ,film.description,film.release_year,film.rating,film.special_features
FROM film JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE actor.actor_id = 15 AND film.rating = 'G' AND film.special_features like '%behind the scenes%';

/*Q6 What query would you run to get all the actors that joined in the film_id = 3c69? 
Your query should return the film_id, title, actor_id, and actor_name.*/
SELECT film.film_id ,film.title,actor.actor_id,CONCAT(actor.first_name,' ' ,actor.last_name) AS actor_name
FROM film JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE film.film_id = 369;

/*Q7 What query would you run to get all drama films with a rental rate of 2.99? 
Your query should return film title, description, release year, rating, special features, 
and genre (category).*/
SELECT film.film_id,film.title,film.description,film.release_year,film.rating,film.special_features,category.name AS genre,film.rental_rate
FROM film JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id = film_category.category_id
WHERE category.name ='Drama' AND film.rental_rate = 2.99;

/*Q8* What query would you run to get all the action films which are joined by SANDRA KILMER? 
Your query should return film title, description, release year, rating, special features, genre (category),
and actor's first name and last name.*/
SELECT actor.actor_id,CONCAT(actor.first_name,' ' , actor.last_name)AS actor_name ,film.film_id,film.title,film.description,film.release_year,film.rating,film.special_features,category.name AS genre
FROM film JOIN film_category ON film.film_id= film_category.film_id JOIN category ON category.category_id = film_category.category_id
JOIN film_actor ON film.film_id = film_actor.film_id JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE category.name ='Action' AND actor.first_name = 'SANDRA' AND actor.last_name ='KILMER';
 