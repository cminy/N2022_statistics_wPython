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

# world 데이터 베이스에서 국가코드, 국가이름, 독립년도, 독립년도가 1900년 이후에 독립했으면 1(True)을 출력하는 쿼리를 작성하세요.
qr04 = "select code, name, indepyear, case when indepyear >= 1900 then 1 end as '1900년 이후' from country;"
an04 = pd.read_sql(qr04, db)
an04.head()

# world 데이터 베이스에서 국가코드, 국가이름, 인구수, 기대수명, 인구수가 5천만 이상이고, 기대수명이 70세 이상이면 1(True)을 출력하는 쿼리를 작성하세요.
qr05 = "select code, name, population, lifeexpectancy, case when (population >= 50000000) AND (lifeexpectancy >= 70) then 1 end as 'TRUE' from country;"
an05 = pd.read_sql(qr05, db)
an05.head(3)
an05.sort_values('TRUE')

# ------ 9, 10
qr = "select * from country where continent in ('Asia', 'Africa');"
an = pd.read_sql(qr, db)
an.head(3)
qr = 'select * from country where code like "Z%";'
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

# FIN.
