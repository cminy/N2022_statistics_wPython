# DESCRIPTION : Wine Quality Data Set 변수 EDA
# -*- coding: utf-8 -*-

from wineQ.actd_mergeadd import MergeManager
from warnings import simplefilter
import pandas as pd
import numpy as np
import seaborn as sns
import scipy
import matplotlib
from matplotlib import pyplot as plt


# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)
# csv파일로 저장된 data set 불러오기
df = MergeManager().findmerged('wineAll.csv')
# - idx 제거
winedf = df.drop(['Unnamed: 0'], axis=1)
# - vinoCate 숫자로 수정
winedf['vinoCate'] = winedf['vinoCate'].apply(lambda x: 1 if x == 'red' else 0)
winedf.head(3)
winedf.describe()


def wineplot(wine_var):
    # 각 변수에 대해 히스토그램,박스차트를 그려본다
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.title('{} hist/ked plot'.format(wine_var))
    sns.distplot(winedf[wine_var])
    plt.subplot(1, 2, 2)
    plt.title('{} box plot'.format(wine_var))
    sns.boxplot(winedf[wine_var])


for i in winedf.columns:
    wineplot(i)


# 상관행렬
winedf.columns
c_arr = winedf.columns[0:12]
c_arr


winedf[c_arr].corr()
plt.figure(figsize=(10, 10))
sns.heatmap(winedf[c_arr].corr(), cmap='RdYlBu_r', annot=True, square=True)

# heatmap 삼각형으로 보여주기
fig, ax = plt.subplots(figsize=(10, 10))
# - 위쪽 삼각형에 true, 아래쪽에 false로 설정하여 표시하지 않을 부분 마스크 지정
mask = np.zeros_like(winedf[c_arr].corr(), dtype=bool)
mask[np.triu_indices_from(mask)] = True
sns.heatmap(winedf[c_arr].corr(), cmap='RdYlBu_r',
            annot=True, mask=mask, linewidth=.5)
plt.show()


# 독립변수와 종속변수 분할
x = winedf.drop(['quality', 'vinoCate'], axis=1)
y = winedf['quality']

plt.figure(figsize=(15, 15))
for n, column in enumerate(x.columns):
    plt.subplot(4, 3, n + 1)
    sns.stripplot(x=y, y=x[column], size=4)


# FIN.
