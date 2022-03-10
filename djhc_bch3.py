# DESCRIPTION : 3장 연습문제
# -*- coding: utf-8 -*-


import pandas as pd
from pandas.core.groupby.groupby import DataError
import math as m
from matplotlib import pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# 2번
x = np.arange(0, 6)
y1 = x
y2 = x * x
y3 = np.log(x + 1)
y4 = np.sqrt(x)


plt.figure(figsize=(8, 3))
plt.scatter(x, y1, color="red")
plt.plot(x, y2, color="orange")
plt.plot(x, y3, color="yellow", linestyle='-.')
plt.plot(x, y4, color="green", linestyle='--')
plt.legend(labels=('y1', 'y2', 'y3', 'y4'), loc='upper left')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# 5번
x = np.linspace(-3, 3, 100)
y = (1 / np.sqrt(2 * np.pi)) * np.exp(-x**2 / 2)
plt.figure(figsize=(8, 2))
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.title("Standard Normal Distribution")
plt.legend(["N(0,1)"])
y2 = np.exp(-np.abs(x))
plt.plot(x, y2, color="orange")
plt.show()


# 10번
iris = sns.load_dataset("iris")
iris.head()
iris.mean(axis=0)
iris.groupby("species").mean()

st = iris.groupby(iris.species).mean()
print(st)
st.T.plot.bar(rot=0)
plt.title("variable mean of species")
plt.xlabel("variables")
plt.ylabel("mean")
plt.show()
