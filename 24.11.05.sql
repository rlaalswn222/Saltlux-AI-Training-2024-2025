USE newschema;
select * from customer1 order by balance desc limit 5; #전체에서 balance를 내림차순 정렬하고 5개만 조회

SELECT balance AS bal FROM customer1 ORDER BY bal DESC limit 5; #balance만 조회하고 bal로 별칭을 하고 나서 내림차순 후 5개만 조회

SELECT * FROM customer1 WHERE name like '%LEE%'; # LEE라는 이름을 갖는 사람이 있으면 찾아달라

#LIKE문 특정 문자를 찾을 때 사용
#특정 문자로 시작하는 데이터 문자열%, 특정 문자열을 포함하는 데이터 문자열 %문자열%, 특정 문자열로 끝나는 데이터 %문자열

#이메일 주소가 example 도메일을 갖는 ?

SELECT name FROM customer1 WHERE email like '%@example%';

#국가 별 평균 잔액
SELECT country, AVG(balance)  FROM customer1 group by country;

#연령대별 10대, 20대 고객 수
SELECT floor(age/10)*10 as age_group, count(*) as customer1_count FROM customer1 group by age_group;

#연령대별 평균 잔액
SELECT avg(balance) as age_bal, floor(age/10)*10 as age_group FROM customer1 group by age_group;
 
 #having 절 
 #group by 절에서 생성된 결과 값 중 원하는 조건에 부합하는 데이터만 보고자할때 사용
 
 #고객의 수가 5명 이상인 국가를 조회
SELECT country, count(*) as customer_count #별명 지정은 좀 더 간략하게 하기 위함임
from customer1
group by country
having customer_count >= 5;

#총 잔액이 1000이상인 국가를 조회
SELECT country, sum(balance) as bal_country
FROM customer1
group by country
having bal_country >=1000;

#20대 고객중 평균 잔액이 300이상인 고객 조회
SELECT floor(age/10)*10 as age_group, AVG(balance) as avg_bal
FROM customer1
group by age_group
having age_group = 20 and avg_bal >= 300;

SELECT country, count(*) as customer_count 
FROM customer1
group by country
having customer_count <=10;

#특정 국가에서 잔액이 1000이상인 고객의 수
SELECT country, count(*) as customer_count
FROM customer1
where balance >= 1000
group by country;

#잔액이 가장 높은 고객 조회
SELECT name, balance 
FROM customer1
WHERE balance = (select MAX(balance) FROM customer1);

SELECT balance from customer1
ORDER BY balance DESC limit 1;

#고객을 이메일 도메일 별로 그룹화하고 각 도메인 별 고객 수 조회
SELECT substring_index(email, '@', -1) as domain, count(*) as customer_count
FROM customer1 group by domain;

#가장 최근에 가입한 고객
SELECT * FROM customer1
WHERE created_at = (SELECT max(created_at) FROM customer1)

#국가별로 잔액이 200 이상인 고객 수 조회
SELECT country, count(*) as customers_high_bal
from customer1
where balance >=200
group by country;

-- SELECT country, count(*) from customer1
-- group by country
-- having balance >= 200

select name, age
FROM customer1
WHERE age = (select max(age) from customer1);

#문자열 길이 조회
SELECT name, length(name) as name_length
FROM customer1;

#국가가 USA거나 CANADA인 경우
SELECT * FROM customer1
WHERE country in('usa', 'canada');

#LEFT : 문자열의 왼쪽부터 지정된 수 만큼의 문자를 반환
#고객의 이름을 3글자로 잘라서 조회
SELECT name, left(name, 3)
from customer1;

#CURDATE(): 현재 시간 추출
#가입일이 현재 날짜와 30일 이하 차이 나는 고객 조회
SELECT * FROM customer1 
WHERE datediff(CURDATE(), created_at)<=30;

#귝가별 고객의 평균 잔액이 200이상인 국가 조회
SELECT country
FROM (SELECT country, avg(balance) as country_bal 
	FROM customer1
	group by country) as country_bal
WHERE country_bal >=200;

#이름을 소문자로 변경
SELECT lower(name) from customer1;

#전체 평균 잔액보다 잔액이 높은 고객 조회
SELECT name, balance
FROM customer1
WHERE balance > (SELECT AVG(balance) FROM customer1);

#각 고객의 잔약이 해당 국가의 평균 잔액보다 높은 고객을 조회하는 행위
SELECT name, balance FROM customer1 AS C
WHERE balance > 
	(SELECT avg(balance) FROM customer1
	WHERE country = c.country);


#각 국가에서 잔액이 가장 높은 고객을 조회하는 쿼리
SELECT * FROM customer1
WHERE (country, balance) in(
	select country, max(balance) FROM customer1 
	group by country);
    
# 각 국가에서 잔액이 두번째로 높은 고객을 조회하는 쿼리
#row_number() 함수: 동일한 값이라도 고유한 순위를 부여함
#rank() 함수: order by를 포함한 쿼리문에서 특정항목에 대한 순위를 구하는 함수
SELECT country, name, balance 
	FROM(
	SELECT country, name, balance, 
    row_number() over
    (partition by country order by balance desc) as rank1  #partition 독립적으로 만듦
    from customer1)
as ranked_customers 
WHERE rank1 = 2;

INSERT INTO customer1 (customer_id, name, age, email, country, balance, created_at)
values
	(4, 'Alice Johnson', 34, 'alice.johnson@example.com', 'Canada', 320.50, '2024-11-05'),
    (5, 'Bob Lee', 27, 'bob.lee@example.com', 'Australia', 150.25, '2024-11-05'),
    (6, 'Carlos Gomez', 45, 'carlos.gomez@example.com', 'Mexico', 275.30, '2024-11-05'),
    (7, 'Diana Prince', 29, 'diana.prince@example.com', 'USA', 450.00, '2024-11-05'),
    (8, 'Ethan Hunt', 38, 'ethan.hunt@example.com', 'UK', 210.80, '2024-11-05');
    
INSERT INTO customer1 (customer_id, name, age, email, country, balance, created_at)
VALUES
	(9, 'Fiona Chen', 31, 'fiona.chen@example.com', 'China', 520.40, '2024-11-03'),
    (10, 'George Smith', 40, 'george.smith@example.com', 'Germany', 310.60, '2024-10-28'),
    (11, 'Helen Zhao', 28, 'helen.zhao@example.com', 'Japan', 480.20, '2024-09-25'),
    (12, 'Igor Petrov', 33, 'igor.petrov@example.com', 'Russia', 150.90, '2024-08-30'),
    (13, 'Jasmine Patel', 36, 'jasmine.patel@example.com', 'India', 540.70, '2024-06-15'),
    (14, 'Karl Schmidt', 42, 'karl.schmidt@example.com', 'Austria', 120.50, '2024-11-04'),
    (15, 'Lara Croft', 30, 'lara.croft@example.com', 'Brazil', 450.00, '2024-11-02'),
    (16, 'Mohamed Ali', 47, 'mohamed.ali@example.com', 'Egypt', 290.40, '2024-10-10'),
    (17, 'Nina Lopez', 26, 'nina.lopez@example.com', 'Spain', 610.00, '2024-09-01'),
    (18, 'Oscar Diaz', 32, 'oscar.diaz@example.com', 'Argentina', 210.10, '2024-07-20'),
    (19, 'Priya Sharma', 29, 'priya.sharma@example.com', 'India', 180.60, '2024-05-05'),
    (20, 'Quincy Brown', 35, 'quincy.brown@example.com', 'South Africa', 300.75, '2024-03-23'),
    (21, 'Ravi Kumar', 28, 'ravi.kumar@example.com', 'India', 250.40, '2024-02-14'),
    (22, 'Sara Lee', 31, 'sara.lee@example.com', 'South Korea', 330.25, '2024-10-18'),
    (23, 'Tom Hanks', 39, 'tom.hanks@example.com', 'USA', 270.90, '2024-01-10');
    
#특정 국가에서 평균 잔액이 전체 평균 잔액보다 높은 국가 목록 조회
SELECT country FROM customer1
GROUP BY country
HAVING avg(balance) > (SELECT avg(balance) FROM customer1);

#RANK()함수 : 특정 항복에 대한 순위를 구하는 함수
#각 고객의 잔액이 고객 목록에서 몇 번째로 높은지 순위를 매기는 쿼리
SELECT name, balance,
	RANK() over (
    ORDER BY balance DESC) AS balance_rank
FROM customer1;

#RANK() 활용해서 2번째로 높은 순위 뽑는 쿼리
SELECT name, balance,
	RANK() over (
    ORDER BY balance DESC) AS balance_rank_2
FROM customer1 limit 1, 1;

#선생님 답
SELECT name, balance
FROM (
	SELECT name, balance,
		RANK() OVER (
        order by balance DESC) AS balance_rank_2
	FROM customer1) as ranked_customers
WHERE balance_rank_2 = 2;

#각 국가별로 나이가 가장 많은 고객의 이름과 나이를 조회하는 쿼리
SELECT name, age FROM customer1
WHERE (country, age) in 
(SELECT country, max(age) FROM customer1
GROUP BY country);

SELECT c.country, c.name, c.age FROM customer1 c
join(
	SELECT country, max(age) AS max_age
    FROM customer1
    GROUP BY country
) AS max_ages on c.country = max_ages.country and c.age = max_ages.max_age;

# 각 고객의 총 잔액 대비 비율을 계산하는 쿼리
SELECT name, balance,
	ROUND(balance/sum(balance) over()*100, 2) as balance_percentage
from customer1;

#over(): 윈도우 함수(행과 행간 비교, 연산, 정의하기 위한 함수)
#데이터를 특정 범위 내에서 분석할 수 있게 해주는 형태

#고객 목록에서 각 고객의 잔액이 전체 평균에서 얼마나 벗어났는지 계산하는 쿼리
SELECT name, balance,
	(balance - avg(balance) over()) as div_from_avg
FROM customer1;

#고객별 나이가 평균 나이 이상인 경우 '성인' 미만인 경우 '청소년'으로 분류하는 쿼리
#CASE(=if) WHEN 조건 THEN 조건일 때의 문구 ELSE 조건을 벗어날때의 문구 END
SELECT name, age, 
	CASE
		WHEN age >=(SELECT avg(age) FROM customer1) THEN '성인'
		ELSE '청소년' END as age_group
FROM customer1;

SELECT name, age,
	CASE
		WHEN age >=(SELECT avg(age) FROM customer1) THEN '성인'
        WHEN age >=13 THEN'청소년'
        ELSE '어린이'
	END AS age_group
FROM customer1;

#LAG(): 여러 행을 되돌아보고 현재 행에서 해당 행의 데이터에 엑세스 할 수 있는 윈도우함수
#각 고객의 이전 고객과의 잔액 차이를 계산하는 쿼리
SELECT name, balance, 
	LAG(balance) OVER (ORDER BY customer_id) AS previous_balance,
	balance - LAG(balance) OVER (ORDER BY customer_id) AS balance_diff
FROM customer1;

#고객 목록에서 현재 고객의 잔액이 최근 3명의 고객의 평균 잔액보다 높은지 여부를 확인
SELECT name, balance, 
	CASE	
		WHEN balance > avg(balance) OVER
			(ORDER BY customer_id 
            rows between 2 preceding and current row)
            THEN 'Abone Average'
            ELSE 'BELOW AVERAGE' END AS balance_comparison
FROM customer1;
