#customer 테이블에서 10일 이상의 영화를 대여한 고객들의 first_name, last_name을 조회
USE sakila;
SELECT
    c.first_name,
    c.last_name
FROM customer AS c
    INNER JOIN rental AS r ON c.customer_id = r.customer_id
WHERE DATEDIFF(r.return_date, r.rental_date) >= 10;

#customer테이블에서 이름에 'a'가 포함된 고객들의 first_name, last_name의 고객을 조회하시오
SELECT
	first_name, last_name
FROM customer
WHERE first_name or last_name like '%a%';

SELECT * from category;

#film 테이블에서 'Action'장르의 영화 중, 2006년에 개봉한 영화의 title과 release_year 조회
SELECT
	f. title, f. release_year
FROM film AS f
	INNER JOIN film_category AS fc ON f.film_id = fc.film_id
    INNER JOIN category AS c ON fc.category_id = c.category_id
WHERE c.name = 'Action' and f.release_year = 2006;

#film 테이블에서 'Comedy'장르의 영화 중 rating이 'PG'인 영화의 title과 release_year를 조회하시오
SELECT
		f. title, f. release_year, f.rating
FROM film AS f
	INNER JOIN film_category AS fc ON f.film_id = fc.film_id
    INNER JOIN category AS c ON fc.category_id = c.category_id
WHERE c.name = 'Comedy' and f.rating = 'PG';