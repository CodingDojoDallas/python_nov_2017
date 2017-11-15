#1)
select a.name, b.language, b.percentage
from countries a join languages b on a.id = b.country_id
where b.language = 'Slovene'
order by b.percentage desc;

#2)
select a.name, count(*) as number_of_cities
from countries a join cities b on a.id = b.country_id
group by a.name
order by number_of_cities desc;



#3)
select b.name, b.population
from countries a join cities b on a.id = b.country_id
where a.name = 'Mexico' and b.population > 500000
order by b.population desc;



#4)
select a.name, b.language, b.percentage
from countries a join languages b on a.id = b.country_id
where b.percentage > 89
order by b.percentage desc;


#5)
select a.name, a.surface_area, a.population
from countries a 
where a.surface_area < 501 and a.population > 100000;


#6)
select a.name, a.government_form, a.capital, a.life_expectancy
from countries a 
where a.capital > 200 and life_expectancy > 75 and government_form = 'Constitutional Monarchy';

#7)
select a.name, b.name, b.district, b.population
from countries a join cities b on a.id = b.country_id
where a.name = 'Argentina' and b.district = 'Buenos Aires' and b.population > 500000;


#8)
select a.region, count(*) as countries
from countries a
group by a.region
order by countries desc;