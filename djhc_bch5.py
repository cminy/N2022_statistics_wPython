# DESCRIPTION : 5장 연습문제
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import stemgraphic
import scipy

# 연습문제 1
experiment = np.arange(1, 21)
count = np.array([10, 12, 20, 14, 17, 20, 14, 13, 11,
                  17, 21, 11, 16, 14, 17, 2, 0, 1, 7, 2])
# spray = np.array(['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B',
#                   'B', 'B', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C'])
A = np.tile('A', 8)
B = np.tile('B', 7)
C = np.tile('C', 5)
spray = np.concatenate((A, B, C), axis=0)
df = pd.DataFrame({'experiment': experiment, 'count': count, 'spray': spray})
df.head(5)

# - (a)
df_grade = pd.crosstab(index=df.spray, columns="grade_count")
df_grade
grade = np.array(df.spray.unique())
plt.pie(df_grade['grade_count'], labels=grade, autopct='%.0f%%')
plt.show()

# - (b)(c)
df['count'].mean()
df.groupby('spray').sum()


# 연습문제 2
river = np.array([735, 320, 325, 392, 524, 450, 1459, 135, 465, 600, 330, 336, 280, 315,
                  870, 906, 202, 329, 290, 1000, 600, 505, 1450, 840, 1243, 890, 350, 407, 286, 280])
pd.DataFrame(river).describe()
# - (a) 평균 570.47 중앙값 428.50
# - (b) 표준편차 359.98 사분위수범 321.25 ~ 813.75
# - (c)
np.percentile(river, [15, 45, 80])
# - (d) 히스토그램, (e) 상자그림
plt.figure(figsize=(8, 3))
plt.subplot(121)
sns.distplot(river, kde=False, rug=False)
plt.subplot(122)
sns.boxplot(data=river, orient='v', color='m')


# 연습문제 3
arr = [25, 16, 44, 62, 36, 58, 38]
# - (a)(b)(c)
df_bulb = pd.DataFrame(arr)
df_bulb.describe()
# - (d),(e)
plt.figure(figsize=(8, 3))
plt.subplot(121)
sns.boxplot(data=arr, orient='v', color='orange')
plt.subplot(122)
sns.boxplot(data=arr, orient='h', color='green')
# - (f)
stemgraphic.stem_graphic(arr, scale=10)
# - 누적개수 7, 중앙값은 38, 그렇네..


# 연습문제 4
y = scipy.stats.norm.rvs(loc=0, scale=1, size=30)

n = len(y)
m = np.mean(y)  # - scipy 2.0.0에는 mean, std 등 없어짐
sd = np.std(y)
lower = m - 2 * sd / np.sqrt(n)
upper = m + 2 * sd / np.sqrt(n)

print('{}\n{}\n{}\n{}\n'.format(m, sd, lower, upper))


# 연습문제 5
arr_income = np.array([19, 21, 15, 23, 24, 15, 15, 15, 16, 29, 18,
                       32, 20, 23, 24, 24, 25, 25, 25, 25, 25, 25, 25, 36, 26, 28, 30])
# - (a)(b)
pd.DataFrame(arr_income).describe()
# - (c) 히스토그램
sns.histplot(arr_income)
# - (d)파이그림
cate1 = arr_income[arr_income < 20]
cate2 = arr_income[np.where((arr_income >= 20) & (arr_income < 30))]
cate3 = arr_income[arr_income >= 30]

plt.pie(x=[len(cate1), len(cate2), len(cate3)], labels=[
        '<20', '20~29', '>=30'], autopct='%.0f%%')
plt.show()


# 연습문제 6
data = np.array([2.3, 2.4, 3.1, 2.2, 1.0, 2.3, 2.1, 1.1, 1.2, 0.9, 1.5, 1.1])
# - (a),(b)
pd.DataFrame(data).describe()

# - (c)
n = len(data)
m = np.mean(data)
sd = np.std(data, ddof=1)
cri = scipy.stats.t.ppf(df=n - 1, q=0.975)  # 신뢰구간 95%니까 0.025씩
lower = m - cri * sd / np.sqrt(n)
upper = m + cri * sd / np.sqrt(n)
print("t분포이용\nlower:{}\nupper:{}".format(lower, upper))
cri = scipy.stats.norm.ppf(loc=0, scale=1, q=0.975)  # 신뢰구간 95%니까 0.025씩
lower = m - cri * sd / np.sqrt(n)
upper = m + cri * sd / np.sqrt(n)
print("정규분포이용\nlower:{}\nupper:{}".format(lower, upper))

# - (d)
plt.figure(figsize=(4, 7))
sns.boxplot(data=data, orient='v', color='orange')

# - (e)
stemgraphic.stem_graphic(data, scale=1)


# 연습문제 7
smoke = np.array(['y', 'y', 'n', 'n'])
wrinkle = np.array(['y', 'n', 'y', 'n'])
freq = np.array([60, 10, 30, 40])
df = pd.DataFrame({'smoke': smoke, 'wrinkle': wrinkle, 'freq': freq})

# - (a)(b)(c)
df_smoke = df.loc[smoke == 'y', :]
df_smoke
p1 = df_smoke['freq'][0] / df_smoke['freq'].sum()
p1

df_non = df.loc[smoke == 'n', :]
df_non
p2 = df_non['freq'][2] / df_non['freq'].sum()
p2

p1 - p2

# - (d)
arr_wrinkle = np.array(df.wrinkle.unique())
freq1 = np.array([df_smoke['freq'][0], df_smoke['freq'][1]])
freq2 = np.array([df_non['freq'][2], df_non['freq'][3]])

plt.figure(figsize=(8, 4))
plt.subplot(121)
plt.pie(freq1, labels=arr_wrinkle, autopct='%.0f%%')
plt.title("smoke")
plt.subplot(122)
plt.pie(freq2, labels=arr_wrinkle, autopct='%.0f%%')
plt.title("non")


# 연습문제 8
arr_tv = [5.7, 6.7, 6.8, 7.9, 10.6, 11.3, 9.8, 8.4, 8.3,
          9.5, 6.7, 6.9, 9.8, 8.8, 12.1, 10.2, 9.5, 9.4, 9.3, 5.9]

# - (a)(b)(c)
pd.DataFrame(arr_tv).describe()

n = len(arr_tv)
m = np.mean(arr_tv)
sd = np.std(arr_tv, ddof=1)
cri = scipy.stats.norm.ppf(loc=0, scale=1, q=0.975)  # 신뢰구간 95%니까 0.025씩
lower = m - cri * sd / np.sqrt(n)
upper = m + cri * sd / np.sqrt(n)
print("정분포이용\nlower:{}\nupper:{}".format(lower, upper))
# - interval 이용
scipy.stats.t.interval(alpha=0.95, df=len(arr_tv) - 1,
                       loc=np.mean(arr_tv), scale=scipy.stats.sem(arr_tv))
# - (d)(e)
plt.figure(figsize=(8, 3))
plt.subplot(121)
sns.boxplot(data=arr_tv, orient='v', color='orange')
plt.subplot(122)
sns.histplot(data=arr_tv, color='green', kde=True)


# 연습문제 9 >> 8번이랑 똑같음.
# 연습문제 10
print("찬성비율: {}, 반대비율: {}".format(80 / 200, 120 / 200))

# 연습문제 11
arr_time = [5.6, 7.8, 6.5, 7.2, 6.9, 7.3, 5.8, 7.5, 8.2, 7.8]
# - (a)(c)
pd.DataFrame(arr_time).describe()

# - (b)
n = len(arr_time)
m = np.mean(arr_time)
sd = np.std(arr_time, ddof=1)
cri = scipy.stats.norm.ppf(loc=0, scale=1, q=0.975)
lower = m - cri * sd / np.sqrt(n)
upper = m + cri * sd / np.sqrt(n)
print("정분포이용\nlower:{}\nupper:{}".format(lower, upper))

# - (d)
plt.figure(figsize=(5, 7))
sns.boxplot(data=arr_time, orient='v', color='orange')

# - (e) Z점수구하기
z = (arr_time - np.mean(arr_time)) / np.std(arr_time, ddof=1)
z


# FIN.
