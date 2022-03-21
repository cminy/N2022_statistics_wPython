# DESCRIPTION : Wine Quality Data Set으로 5장 예제문제풀기
# -*- coding: utf-8 -*-

import os
import glob
import pandas as pd
import numpy as np
from wineQ.actd_mergeadd import MergeManager
from matplotlib import pyplot as plt
import seaborn as sns
import stemgraphic
import scipy


# csv파일로 저장된 data set 불러오기
winedf = MergeManager().findmerged('wineAll.csv')
# 와인데이터에서 랜덤으로 30개 뽑아오기
df = winedf.sample(n=30, random_state=20).reset_index(drop=True)
# df_col = sorted(list(df.columns))
# df_col
df.rename(columns={"Unnamed: 0": "_idx"}, inplace=True)
df.head(5)

# 예제 5.1.1 랜덤으로 뽑은 와인데이터에서 와인 종류(레드/화이트)별 카운트하고 막대그래프 그리기
cr = pd.crosstab(index=df['vinoCate'], columns="count")
cr


# 예제 5.1.2 (a)
y_pos = np.arange(len(cr))
x_pos = ['red', 'white']

plt.figure(figsize=(12, 8))
plt.subplot(1, 2, 1)
plt.bar(y_pos, cr['count'], color=['r', 'yellow'], width=0.7, edgecolor='grey')
plt.xticks(y_pos, x_pos, fontsize=12, rotation=45)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
for i in range(0, len(x_pos)):
    plt.text(i, cr['count'][i], '{}'.format(
        cr['count'][i]), fontsize=10, horizontalalignment='center', verticalalignment='bottom')

plt.subplot(1, 2, 2)
#plt.barh(y_pos, cr['count'], color=['red', 'yellow'])
sns.barplot(x=cr['count'], y=x_pos, palette='husl')
plt.yticks(y_pos, x_pos, fontsize=12)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
for i in range(0, len(x_pos)):
    plt.text(cr['count'][i], i, '{}'.format(
        cr['count'][i]), fontsize=10, horizontalalignment='center', verticalalignment='bottom')


# 예제 5.1.3 (a)
plt.style.use('_mpl-gallery-nogrid')
colors = plt.get_cmap('Greys')(np.linspace(0.2, 0.7, len(cr)))
fig, ax = plt.subplots()
ax.pie(cr['count'], labels=x_pos, colors=colors, radius=3, center=(
    4, 4), wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=False)
ax.set(xlim=(0, 8), ylim=(0, 8))
plt.show()

plt.pie(cr['count'], labels=x_pos)
plt.show()

# 예제 5.1.3(b)
# - 레드와인 평점 비교
tempdf = winedf.loc[winedf['vinoCate'] == 'red']
df2 = pd.crosstab(index=tempdf['quality'], columns="count")
df2

plt.rcParams['figure.figsize'] = [12, 10]
wine_Q = np.array(tempdf['quality'].unique())
wine_Qcount = np.array(df2['count'])
y_pos = np.arange(len(wine_Q))

explode = (0.0, 0.4, 0.0, 0.0, 0.0, 0.0)
plt.subplot(1, 3, 1)
plt.pie(wine_Qcount, labels=wine_Q)
plt.subplot(1, 3, 2)
plt.pie(wine_Qcount, labels=wine_Q, explode=explode)
plt.subplot(1, 3, 3)
plt.pie(wine_Qcount, labels=wine_Q, explode=explode,
        colors=colors, shadow=True, startangle=90, autopct='%1.1f%%')
plt.show()


# 예제 5.1.4
plt.grid()
plt.scatter(wine_Q, wine_Qcount, color='b')
plt.ylabel('Count', size=15)
plt.xlabel('Quality', size=15)


# 예제 5.2.1 줄기-잎 그림
# - df에서 'free sulfur dioxide(유리이산화황)'  이용
x = np.array(df['free sulfur dioxide'])
x
stemgraphic.stem_graphic(x, scale=10)


# 예제 5.2.2 상자그림
plt.figure(figsize=(3, 4))
plt.subplot(2, 1, 1)
sns.boxplot(data=x, orient="v", color='m')
plt.ylabel('free sulfur dioxide')
plt.subplot(2, 1, 2)
sns.boxplot(data=x, orient="h", color='g')
plt.show()
# - 다른방식으로 구현 해보기
plt.figure(figsize=(4, 6))
df.plot(kind='box', y='free sulfur dioxide')
# - 중앙값 median(50%)은 30 근처, 최소값은 약 5점 근처, 1사분위수(25%) 20점근처, 3사분위수(75%) 45점근처, 4사분위는 60점근처, 최대값은 100근처


# 예제 5.2.3 (a)(b) 정규분포로부터 50개 난수
y = scipy.stats.norm.rvs(loc=0, scale=1, size=50)
plt.figure(figsize=(7, 4))
plt.subplot(121)
plt.hist(y)
plt.subplot(1, 2, 2)
sns.distplot(y, bins=10)
# - subplot 다른 방식으로 나누기
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharey=False, figsize=(7, 4))
# fig.suptitle("Example 5.2.3", fontsize=15, fontweight='bold')
fig.get_axes()[0].annotate('Example 5.2.3', (0.55, 1.2),
                           xycoords='figure fraction', ha='center', fontsize=15)
ax0.hist(y)
ax0.set(title='5.2.3 (a) histogram')
sns.distplot(y, bins=10)
ax1.set(title='5.2.3 (b) histogram')
ax1.axvline(x=y.mean(), color='b', label='Average',
            linestyle='--', linewidth=1)


# 예제 5.2.7(a)
n = len(y)
m = np.mean(y)  # - scipy 2.0.0에는 mean, std 등 없어짐
sd = np.std(y, ddof=1)
cri = scipy.stats.t.ppf(df=n - 1, q=0.975)  # 신뢰구간 95%니까 0.025씩
lower = m - cri * sd / np.sqrt(n)
upper = m + cri * sd / np.sqrt(n)

fig, ax = plt.subplots(nrows=1, ncols=1, sharey=False, figsize=(7, 4))
ax.set(title='5.2.7 (a) CI 95%')
sns.distplot(y, bins=10)
ax.axvline(x=lower, label='Lower Limit', linewidth=1, color='orange')
plt.text(lower - 2, 0.5,
         'Lower Limit:{:.2f}'.format(lower), fontsize=12, color='orange')
ax.axvline(x=upper, label='Upper Limit', linewidth=1, color='orange')
plt.text(upper + 0.3, 0.5,
         'Upper Limit:{:.2f}'.format(upper), fontsize=12, color='orange')


# 예제 5.2.7(d)
population = scipy.stats.norm(loc=0, scale=1)
time = np.array(np.arange(30))


def calc_sample_mean_ci(size, n_trial):
    sample_mean_arr = np.zeros(n_trial)
    ci_lower_arr = np.zeros(n_trial)
    ci_upper_arr = np.zeros(n_trial)
    int_arr = np.zeros(n_trial)
    for i in range(0, n_trial):
        sample = population.rvs(size=size)
        sample_mean_arr[i] = np.mean(sample)
        sd = np.std(sample, ddof=1) / np.sqrt(size)
        ci_lower_arr[i] = np.mean(sample) - 1.96 * sd
        ci_upper_arr[i] = np.mean(sample) + 1.96 * sd
        int_arr[i] = 1.96 * sd
    return(sample_mean_arr, ci_lower_arr, ci_upper_arr, int_arr)


np.random.seed(1)
m, lo, up, int_l = calc_sample_mean_ci(size=10, n_trial=30)
plt.errorbar(time, m, yerr=int_l, fmt="bo", linewidth=1,
             elinewidth=0.3, ecolor='k', capsize=3, capthick=0.5)
plt.axhline(y=0)

# FIN.
