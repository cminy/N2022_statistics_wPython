# DESCRIPTION : Wine Quality Data Set으로 5장 문제풀기
# -*- coding: utf-8 -*-

import os
import glob
import pandas as pd
import numpy as np
from wineQ.actd_mergeadd import MergeManager


# csv파일로 저장된 data set 불러오기
winedf = MergeManager().findmerged('wineAll.csv')
winedf
