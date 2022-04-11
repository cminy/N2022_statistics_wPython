from mysql.connector import Error
import mysql.connector
import pymysql
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


db = mysql.connector.connect(
    host="127.0.0.1", port=3306, user="root", passwd="mk246900", auth_plugin='mysql_native_password', db="world", charset="utf8")
curs = db.cursor()


# --------- 6p
# world 데이터 베이스에서 각 국가의 국가코드, 국가이름, 인구밀도(1m2당 인구수)를 출력하는 쿼리를 작성하세요.
qr01 = 'SHOW TABLES;'
pd.read_sql(qr01, db)
qr01 = 'DESC country;'
pd.read_sql(qr01, db)
qr01 = 'select*from country;'
test = pd.read_sql(qr01, db)
test.head(3)
qr01 = 'select code, name, population/surfacearea as "인구밀도" from country;'
an01 = pd.read_sql(qr01, db)
an01.head(3)

# world 데이터 베이스에서 각 국가의 국가코드, 국가이름, 1인당 GNP를 출력하는 쿼리를 작성
qr02 = 'select code, name, gnp/population as "1인당GNP" from country;'
an02 = pd.read_sql(qr02, db)
an02.head(3)

# ------ 7p
# world 데이터 베이스에서 국가코드, 국가이름, 대륙, asia 대륙이면 1(True)을 출력하는 쿼리
qr03 = "select case when continent = 'Asia' then 1 end as '아시아', code, name, continent from country;"
an03 = pd.read_sql(qr03, db)
an03.head()

qr03 = """select continent = 'Asia'as is_asia, code, name, continent from country;"""
an03 = pd.read_sql(qr03, db)
an03.head()

# world 데이터 베이스에서 국가코드, 국가이름, 독립년도, 독립년도가 1900년 이후에 독립했으면 1(True)을 출력하는 쿼리를 작성하세요.
qr04 = "select code, name, indepyear, case when indepyear >= 1900 then 1 end as '1900년 이후' from country;"
an04 = pd.read_sql(qr04, db)
an04.head()

qr04 = "select code, name, indepyear, indepyear >= 1900 as '1900년 이후' from country;"
an04 = pd.read_sql(qr04, db)
an04.head()

# world 데이터 베이스에서 국가코드, 국가이름, 인구수, 기대수명, 인구수가 5천만 이상이고, 기대수명이 70세 이상이면 1(True)을 출력하는 쿼리를 작성하세요.
qr05 = "select code, name, population, lifeexpectancy, case when (population >= 5000*10000) AND (lifeexpectancy >= 70) then 1 end as 'TRUE' from country;"
an05 = pd.read_sql(qr05, db)
an05.head(3)
an05.sort_values('TRUE')

qr05 = "select code, name, population, lifeexpectancy, (population >= 5000*10000) AND (lifeexpectancy >= 70) as 'TRUE' from country;"
an05 = pd.read_sql(qr05, db)
an05.head(3)

# ------ 9, 10
qr = "select * from country where continent in ('Asia', 'Africa');"
an = pd.read_sql(qr, db)
an.head(3)
qr = 'select * from country where code like "Z%";'
an = pd.read_sql(qr, db)
an.tail(3)

# africa 대륙에서 인구수가 2천만이상인 국가출력
qr = '''select code, name, population from country
where (continent = 'Africa') and (population >= 2000*10000);
'''
an = pd.read_sql(qr, db)
an.head(3)

# between연산자
qr = '''select code, name, population from country
where population between 2000*10000 and 5000*10000;
'''
an = pd.read_sql(qr, db)
an.head(3)

# ------ 11
# 국가 코드를 알파벳 순으로 정렬하고 같은 국가 코드를 가지면 인구순으로 내림차순으로 정렬
qr = 'select * from city order by countrycode ASC, population DESC;'
an = pd.read_sql(qr, db)
an.head(10)

# 인구가 많은 상위 6위 ~ 8위의 3개 국가 데이터를 출력
qr = 'select * from country order by population DESC limit 3 offset 5;'
an = pd.read_sql(qr, db)
an.head()

qr = 'select * from country order by population DESC limit 5,3;'  # 5개 스킵하고 3개 출력
an = pd.read_sql(qr, db)
an.head()


# --- 마무리 Quiz
# Q1 : 한국의 도시 중에서 인구가 100만이 넘는 도시를 인구수 순으로 내림차순 출력 (국가코드, 도시이름, 도시 인구수)
qr = 'DESC city;'
pd.read_sql(qr, db)

qr = '''
select countrycode, name, population
from city
where (countrycode = 'KOR') AND (population >= 100*10000)
order by population DESC;
'''
an = pd.read_sql(qr, db)
an.head()

# Q2 : 1940년 ~ 1950년 사이에 독립한 국가들 중에 GNP가 10만이 넘는 국가를 GNP 내림차순 출력 (국가코드, 국가이름, 대륙, GNP)
qr = '''
select code, name, continent, GNP, indepyear
from country
where (indepyear between 1940 and 1950) AND (GNP >= 10*10000)
order by gnp DESC;
'''
an = pd.read_sql(qr, db)
an

# Q3 : 영화설명에 drama가 포함되고 관람등급이 R인 영화에서 상영시간이 가장 긴 5개의 영화 내림차순으로 출력
# film_id, title, description, rating, length
qr = 'USE sakila;'
curs.execute(qr)
qr = 'select database();'
an = pd.read_sql(qr, db)
an
qr = 'select * from film;'
an = pd.read_sql(qr, db)
an.head(1)
qr = '''
    select film_id, title, description, rating, length
    from film
    where (description like "%drama%") AND (rating = 'R')
    order by length DESC
    limit 5;
'''
an = pd.read_sql(qr, db)
an
# FIN.
