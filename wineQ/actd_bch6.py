# DESCRIPTION : Wine Quality Data Set으로 6장 예제풀기
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from wineQ.actd_mergeadd import MergeManager
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns
import scipy
from warnings import simplefilter


simplefilter(action='ignore', category=FutureWarning)


# csv파일로 저장된 data set 불러오기
winedf = MergeManager().findmerged('wineAll.csv')

# 예제 6.1.1(a) 범주형데이터의 이원분할표
tempdf = pd.DataFrame({'idx': winedf['Unnamed: 0'],
                       'class': winedf['vinoCate'],
                       'pH_Filter': winedf['pH'].apply(lambda x: 'strong' if x >= winedf['pH'].median() else 'weak')
                       })  # 산성도 평균으로 필터나눔
tempdf.head(5)
tempdf.describe(include='object')
cr = pd.crosstab(index=tempdf['class'], columns=tempdf['pH_Filter'])
cr['strong']
cr['weak']

q1_tb = pd.DataFrame({'pH_': ['strong', 'strong', 'weak', 'weak'],
                      'class': ['red', 'white', 'red', 'white'],
                      'count': [cr['strong'][0], cr['strong'][1], cr['weak'][0], cr['weak'][1]]
                      })
q1_tb


# 6.1.1(b) 주변도수분포
cross = pd.pivot_table(data=q1_tb, values="count", aggfunc="sum",
                       index="class", columns="pH_", margins=True)
cross


# 6.1.1(c) 카이제곱검정
obs = np.array([[1211, 388], [2056, 2842]])
scipy.stats.chi2_contingency(cross, correction=True)

scipy.stats.chi2_contingency(cross, correction=False)

# 6.1.1(d) 결합분포
pd.pivot_table(q1_tb, index=["class", "pH_"], values="count")

# 6.1.2
q1_temp = cross.drop('All', axis=1)
q1_cross = q1_temp.drop('All', axis=0)
q1_cross
q1_cross.plot(kind="bar", stacked=True)
q1_cross.plot(kind="bar", stacked=False)


# 6.1.2(b)
nico_df = pd.read_csv("./cminydata/table6.2_nicotin.csv")
nico_df

nico_df.shape

grouped = nico_df.groupby(['nicotin', 'stopsmoke'])
grouped.size()

nico_tab = pd.crosstab(index=nico_df['nicotin'], columns=nico_df['stopsmoke'])
nico_tab


# 6.2(a)
# - 와인품질데이터에서 fixed acidity(산도)와 pH 관계 알아봐야지
winedf.head(2)
q2_tb = pd.DataFrame({'fixed acidity': winedf['fixed acidity'],
                      'pH': winedf['pH']})
q2_tb

q2_tb.describe()

# - 산도와 수소이온농도의 상관계수와 상관성에 대한 유의성검정
scipy.stats.pearsonr(q2_tb['fixed acidity'], q2_tb['pH'])
abs(scipy.stats.pearsonr(q2_tb['fixed acidity'], q2_tb['pH'])[0])
# >>> 두 변수는 음의 상관관계가 있고, 관계성은 매우 낮다...


# 6.2(b)
x = q2_tb['fixed acidity']
y = q2_tb['pH']
r1, p1 = scipy.stats.pearsonr(x, y)
print(r1, p1)
r2, p2 = scipy.stats.spearmanr(x, y)
print(r2, p2)
r3, p3 = scipy.stats.kendalltau(x, y)
print(r3, p3)

# - 산점도
%matplotlib inline
matplotlib.style.use('ggplot')
plt.scatter(q2_tb['fixed acidity'], q2_tb['pH'])
plt.xlabel('Fixed Acidity')
plt.ylabel('pH')


# 6.2(c)
q2_tb.boxplot()

# 6.2(d)
sns.distplot(q2_tb['fixed acidity'], label='Fixed Acidity')
sns.distplot(q2_tb['pH'], label='pH')
plt.legend(title='group')

# 6.2(e)
sns.jointplot(x='fixed acidity', y='pH', data=q2_tb, color="orange")

# 6.2(f)
sns.jointplot(x='fixed acidity', y='pH', data=q2_tb, kind='reg', color="green")

# 6.2(g)(h)(i)(j)
# - 와인품질데이터 이용
winedf.columns

x = winedf['volatile acidity']
y = winedf['pH']
scipy.stats.pearsonr(x, y)

sns.jointplot(x=x, y=y, data=winedf, color='skyblue')


plt.scatter(x, y, s=winedf['fixed acidity'], c=winedf['vinoCate'], marker='o')
plt.xlabel("Volatile Acidity")
plt.ylabel("pH")


sns.scatterplot(x='volatile acidity', y='pH', marker='o',
                hue='fixed acidity', style='vinoCate', data=winedf)

# FIN.
