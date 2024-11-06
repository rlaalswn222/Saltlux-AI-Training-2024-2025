
USE sakila;


#where문의 기본 형식
#select [열] from [테이블] where [열] = [조건값]
SELECT * FROM city where country_id = 82;
#city열이 'Sunnyvalue'이면서 country_id열이 103인 ㅇ데이터를 조회하는 쿼리
SELECT * FROM city WHERE city = 'Sunnyvale' and country_id=103;

#country_id 열이 103또는 country_id 열이 86이면서 city열이 'Cheju'
SELECT * From city WHERE country_id = 103 OR (country_id = 86 and city = 'Cheju');

SELECT * FROM city
WHERE country_id in (103, 96)
AND city in('Cheju', 'Sunnyvale', 'Dalles');


SELECT * FROM sakila.customer;
SELECT * FROM address;

SELECT 
	c.customer_id,
    c.store_id,
    c.first_name,
    c.last_name, 
    c.email, 
    c.address_id AS c_address_id,
    c.active,
    c.create_date,
    c.last_update,
    a.address,
    a.district,
    a.postal_code, 
    a.phone
FROM sakila.address a
INNER JOIN sakila.customer c ON c.address_id = a.address_id
WHERE c.first_name = 'ROSA';

#ON문: 조인할 때 조인 조건을 위해 사용
#WHERE문: 조인을 완료할 때 조건에 맞는 데이터값을 가져옴

#Left Outer A 테이블을 기준으로 B에 있지만 A에 없는 것들은 null처리
SELECT
	a.address,
    a.address_id AS a_address_id,
    b.address_id AS b_address_id,
    b.store_id
FROM address AS a
	left outer join store AS b ON a.address_id = b.address_id;

#right join b가 기준
SELECT
	a.address,
    a.address_id AS a_address_id,
    b.address_id AS b_address_id,
    b.store_id
FROM address AS a
	right outer join store AS b ON a.address_id = b.address_id
UNION     #합집합
SELECT
	a.address_id AS a_address_id,
    a.store_id,
    b.address_id AS b_address_id,
    b.address
FROM store AS a
	left outer join address as b on a.address_id = b.address_id;

SELECT
	f.film_id,
	f.title,
    f.special_features,
    c.name
FROM film AS f
	INNER JOIN film_category as fc on f.film_id = fc.film_id
    INNER JOIN category AS c on fc.category_id = c.category_id;
    

#Actor first name이 'CAMERON'이 출연한
#actor_id, last name, 영화의 개수 구하기
SELECT
	a.actor_id,
	a.last_name AS lastname,
   count(f.film_id) AS film_count
FROM actor AS a
	INNER JOIN film_actor as fa on a.actor_id = fa.actor_id
    INNER JOIN film as f on fa.film_id = f.film_id
WHERE a.first_name='CAMERON'
group by a.actor_id, a.last_name;
#-----------------------------


#영화 상영시간이 120분 이상인 영화 카테고리 순으로 정리
SELECT 
	f.length,
    f.title
FROM film AS f
	INNER JOIN film_category AS fc ON f.film_id = fc.film_id
    INNER JOIN category AS c ON fc.category_id = c.category_id
WHERE f.length >=120
ORDER BY c.name;
	

#film_category, film, category테이블을 사용하여 영화 상영 시간이 120분 이상
#상영시간 내림차순, 카테고리 순 오름차순으로 정리
SELECT 
	f.length,
    f.title
FROM film AS f
	INNER JOIN film_category AS fc ON f.film_id = fc.film_id
    INNER JOIN category AS c ON fc.category_id = c.category_id
WHERE f.length >=120
ORDER BY f.length DESC, c.name;


SELECT 
	a.first_name,
    a.actor_id,
    a.last_name,
    count(f.film_id) AS count_film
from film AS f
	INNER JOIN film_actor as fa ON f.film_id = fa.film_id
    INNER JOIN actor as a ON fa.actor_id = a.actor_id
WHERE f.release_year >2005 and a.first_name = 'CAMERON'
group by a.actor_id, a.last_name
HAVING count(f.film_id) >= 3 ;


