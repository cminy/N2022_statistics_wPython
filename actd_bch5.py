# DESCRIPTION : Wine Quality Data Set으로 5장 문제풀기
# -*- coding: utf-8 -*-

import os
import glob
import pandas as pd
import numpy as np
from wineQ.actd_mergeadd import MergeManager

MergeManager().findmerged('wineAll.csv')

# merged = 'wineAll.csv'
# mergedfile = glob.glob("./**/" + merged)
# print(mergedfile)
# winedf = pd.read_csv(mergedfile[0])
# winedf
