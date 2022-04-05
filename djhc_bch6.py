# DESCRIPTION : Wine Quality Data Set으로 6장 연습문제풀기
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns
import scipy
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)


# 1번
q1_df = pd.read_csv("./cminydata/table6.5_fracture.csv")
q1_df.head()

# - (a) 빈도표
pd.crosstab(index=q1_df['gender'], columns=q1_df['fracture'])

# - (b)(c) blood 평균
q1_df.groupby('gender').mean().loc[:, 'blood']
q1_df.groupby('fracture').mean().loc[:, 'blood']

# - (d)(e) 상관계수
age = q1_df['age']
blood = q1_df['blood']

scipy.stats.pearsonr(age, blood)
scipy.stats.spearmanr(age, blood)

# - (f)(g) 박스차트
fracture = q1_df['fracture']
gender = q1_df['gender'].apply(lambda x: 'male' if x == 1 else 'female')
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.title('fracture / blood')
sns.boxplot(x=fracture, y=blood)
plt.subplot(2, 2, 2)
plt.title('gender / blood')
sns.boxplot(x=gender, y=blood)
plt.show()

# - (h)(i) 산점도
plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
sns.scatterplot(x=age, y=blood, hue=fracture, style=fracture)
plt.subplot(2, 1, 2)
sns.scatterplot(x=age, y=blood, hue=gender, style=gender)
plt.show()


# 2번
q2_df = pd.read_csv("./cminydata/table6.6_president_election.csv")
q2_df.head()

# - (a)(c) 빈도표
pd.pivot_table(data=q2_df, values='freq', aggfunc='sum',
               index='ism', columns='candidate', margins=True)

# - (b) 비율표
q2_df['rate'] = q2_df['freq'] / sum(q2_df['freq'])
q2_df.head(2)
pd.pivot_table(data=q2_df, values='rate', aggfunc='sum',
               index='ism', columns='candidate', margins=True)

# - (d) 막대그래프
q2_bar = pd.pivot_table(data=q2_df, values='freq',
                        index='candidate', columns='ism')
q2_bar.plot(kind='bar', stacked=True)

# 3번
x = [147, 158, 131, 142, 180]
y = [122, 128, 125, 123, 115]

# - (a)(b)
scipy.stats.pearsonr(x, y)[0]
scipy.stats.spearmanr(x, y)[0]
# >>> 약한 음의 상관관계

# - (c)
plt.figure(figsize=(12, 8))
plt.subplot(211)
plt.title('husband')
sns.boxplot(x)
plt.subplot(212)
plt.title('wife')
sns.boxplot(y)
plt.show()


# 4번
freq = [40, 30, 35, 20, 20, 30, 45, 40]
q4_df = pd.DataFrame({
    'grade': [1, 2, 3, 4, 1, 2, 3, 4],
    'present': ['Y', 'Y', 'Y', 'Y', 'N', 'N', 'N', 'N'],
    'freq': freq
})
q4_df

# - (a) 학년별 참석/불참석 비율
q4_cross = pd.pivot_table(data=q4_df, values='freq', aggfunc='sum',
                          index='present', columns='grade', margins=True)
q4_cross
rate_arr = []
q4_cross.columns

for i in range(0, len(freq)):
    if i < 4:
        rate_arr.append(freq[i] / q4_cross[(i + 1)]['All'])
    else:
        rate_arr.append(freq[i] / q4_cross[(i - 3)]['All'])

rate_arr

q4_df['p_rate'] = rate_arr
q4_df

qrate_cross = pd.pivot_table(
    data=q4_df, values='p_rate', index='present', columns='grade')
qrate_cross

qrate_cross.plot(kind='bar', stacked=True)


# - (b) 전체 비율
q4_df['rate'] = q4_df['freq'] / sum(q4_df['freq'])
rate_cross = pd.pivot_table(
    data=q4_df, values='rate', index='present', columns='grade')
rate_cross

rate_cross.plot(kind='bar', stacked=True)


# 5번
q5_df = pd.read_csv('./cminydata/table6.7_diabetes.csv')
q5_df.head(3)
# - (a)(b)
scipy.stats.pearsonr(q5_df['Y1'], q5_df['Y2'])[0]
scipy.stats.pearsonr(q5_df['X1'], q5_df['Y2'])[0]
# >>> 상관관계 없네..
# - (c) 유의성 검정
scipy.stats.pearsonr(q5_df['X1'], q5_df['Y2'])[1]
# >>> p-value가 0.948이니까 귀무가설(H0) 기각 못함. >>> 상관계수 0이 아니라고 할 수 없다.

# - (d)
q5_df['count'] = q5_df['Y2'].apply(lambda x: 1 if x >= 90 else 0)
q5_arr = [q5_df['count'].sum(), q5_df['Y2'].count() - q5_df['count'].sum()]
q5_arr

plt.pie(q5_arr, labels=['>=90', '<90'])

# - (e)(f) 산점도
plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
sns.scatterplot(data=q5_df, x='Y1', y='Y2')
plt.subplot(2, 1, 2)
sns.scatterplot(data=q5_df, x='X1', y='Y2')
plt.show()

# - (g) 상관계수
q5_df.columns
c_arr = q5_df.columns[1:6]
c_arr
# - heatmap으로 알아보기
plt.figure(figsize=(10, 10))
sns.heatmap(q5_df[c_arr].corr(), cmap='RdYlBu_r', annot=True, square=True)
# >>> X2, X3 상관계쑤가 제일 높음 (0.28)
# - 다른방법
df = q5_df[c_arr].corr()
df
df.describe()
df2 = df.replace(1.000000, 0)
df2
df2.describe()

# 6번
elder = [86, 71, 77, 68, 91, 72, 60]
younger = [88, 77, 76, 64, 96, 72, 65]
print("- pearson:", scipy.stats.pearsonr(elder, younger)[0])
print("- spearman:", scipy.stats.spearmanr(elder, younger)[0])
print("- kendall:", scipy.stats.kendalltau(elder, younger)[0])
# >>> 상관관계가 높은편.

# FIN.
