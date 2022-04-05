# DESCRIPTION : Wine Quality Data Set으로 6장 연습문제풀기
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
df = MergeManager().findmerged('wineAll.csv')


# FIN.
