#1)
select date_format(charged_datetime, '%M') as month, sum(amount)
from billing
where charged_datetime between '2012-03-01' and '2012-03-31';
#2)
select client_id, sum(amount) as revenue
from billing
where client_id = 2;

#3)
select domain_name, client_id
from sites
where client_id = 10;


#4)
select client_id, count(*) as number_of_leads, date_format(created_datetime, '%M') as month_created, year(created_datetime) as year_created
from sites
where client_id = 1 
group by client_id, date_format(created_datetime, '%M'), year(created_datetime);

select client_id, count(*) as number_of_leads, date_format(created_datetime, '%M') as month_created, year(created_datetime) as year_created
from sites
where client_id = 20
group by client_id, date_format(created_datetime, '%M'), year(created_datetime);

#5)
select a.domain_name, count(*) as number_of_leads, date_format(registered_datetime, '%M %e %Y') as date_generated
from sites a join leads b on a.site_id = b.site_id
where registered_datetime between '2011-01-01' and '2011-02-15'
group by a.domain_name;

#6)
select concat(a.first_name, ' ', a.last_name) as client_name, count(*) as number_of_leads
from clients a join sites b on a.client_id = b.client_id
               join leads c on b.site_id   = c.site_id
where c.registered_datetime between '2011-01-01' and '2011-12-31'
group by a.first_name, a.last_name;


#7)
select concat(a.first_name, ' ', a.last_name) as client_name, count(*) as number_of_leads, date_format(registered_datetime, '%M')
from clients a join sites b on a.client_id = b.client_id
               join leads c on b.site_id   = c.site_id
where c.registered_datetime between '2011-01-01' and '2011-06-30'
group by a.first_name, a.last_name, month(c.registered_datetime);


#8)
select concat(a.first_name, ' ', a.last_name) as client_name, b.domain_name , count(*) as number_of_leads, date_format(registered_datetime, '%M')
from clients a join sites b on a.client_id = b.client_id
               join leads c on b.site_id   = c.site_id
where c.registered_datetime between '2011-01-01' and '2011-12-31'
group by a.first_name, a.last_name, b.domain_name 
order by client_name;

select concat(a.first_name, ' ', a.last_name) as client_name, b.domain_name , count(*) as number_of_leads, date_format(registered_datetime, '%M')
from clients a join sites b on a.client_id = b.client_id
               join leads c on b.site_id   = c.site_id
group by b.domain_name 
order by client_name;



#9)
select concat(a.first_name, ' ', a.last_name) as client_name, sum(b.amount) as Total_revenue, date_format(b.charged_datetime, '%M') as month_charged, year(b.charged_datetime) as year_charged
from clients a join billing b on a.client_id = b.client_id
group by client_name, date_format(b.charged_datetime, '%M %Y')
order by a.client_id, month(b.charged_datetime), year(b.charged_datetime);



#10)
select concat(a.first_name, ' ', a.last_name) as client_name, group_concat(b.domain_name, ' / ') as sites
from clients a left join sites b on a.client_id = b.client_id
group by a.client_id
order by a.client_id;
