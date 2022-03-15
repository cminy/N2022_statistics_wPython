# DESCRIPTION : Wine Quality Data Set 합치기
# -*- coding: utf-8 -*-

import os
import glob
import pandas as pd
import numpy as np


# data폴더 내의 모든 csv 파일 목록 불러오기
csvList = glob.glob("./cminydata/*.csv")
wineAll = pd.DataFrame([])
filename = []

if (len(csvList) == 2):
    print('sssss')
    # vinoCate 컬럼 추가 후 white 와 red csv 합치기
    # - 나중에 클래스 분리하자
    for each_csv in csvList:
        filename = each_csv.split('/')[-1]
        if filename.endswith('red.csv'):
            vinoCate = "red"
            print(vinoCate)
        else:
            vinoCate = "white"
        df = pd.read_csv(each_csv, sep=';')
        df['vinoCate'] = vinoCate
        wineAll = pd.concat([wineAll, df])

    # csv 파일로 저장
    wineAll.to_csv("./cminydata/wineAll.csv")

winedf = pd.read_csv('./cminydata/wineAll.csv')

# 기술통계
winedf.describe()

# 와인 품질 데이터
winedf.groupby("vinoCate")["quality"].value_counts(normalize=True)
