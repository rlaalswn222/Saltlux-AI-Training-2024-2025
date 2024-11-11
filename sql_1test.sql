# 1. customer 테이블에서 10일 이상의 영화를 대여한 고객들의 first_name, last_name을 조회
USE sakila;
SELECT
    c.first_name,
    c.last_name
FROM customer AS c 
    INNER JOIN rental AS r ON c.customer_id = r.customer_id #customer_id키로 내부조인
WHERE DATEDIFF(r.return_date, r.rental_date) >= 10; #rental테이블의 대여 날짜와 반납 날짜를 비교하는 DATEDIFF 함수 사용

# 2. customer테이블에서 이름에 'a'가 포함된 고객들의 first_name, last_name의 고객을 조회하시오
SELECT
	first_name, last_name
FROM customer
WHERE first_name or last_name like '%a%'; #first_name이나 last_name에 a가 포함

SELECT * from category; #category 테이블 내용 확인용

# 3. film 테이블에서 'Action'장르의 영화 중, 2006년에 개봉한 영화의 title과 release_year 조회
#'Action'이라는 장르는 category테이블에 있고, film과 category을 이어줄 key가 각자 테이블에 없기 때문에 film_category테이블까지 조인을 해줘야함
SELECT
	f. title, f. release_year
FROM film AS f
	INNER JOIN film_category AS fc ON f.film_id = fc.film_id #film 테이블의 film_id와 film_category의 film_id로 내부 조인
    INNER JOIN category AS c ON fc.category_id = c.category_id #category의 category_id와 film_category의 category_id로 내부조인
WHERE c.name = 'Action' and f.release_year = 2006; #category테이블에서 name이 action인 것과 realease_year 둘다 조건ㅇ을 만족해야함

# 4. film 테이블에서 'Comedy'장르의 영화 중 rating이 'PG'인 영화의 title과 release_year를 조회하시오
#조인 구문은 위의 문제와 동일. 생략
SELECT
		f. title, f. release_year, f.rating
FROM film AS f
	INNER JOIN film_category AS fc ON f.film_id = fc.film_id
    INNER JOIN category AS c ON fc.category_id = c.category_id
WHERE c.name = 'Comedy' and f.rating = 'PG'; # category테이블 에서 name이 comedy인 것과 film 테이블에서 rating이 PG인 것 두개의 조건 둘다 만족해야함