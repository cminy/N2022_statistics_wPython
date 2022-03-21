# DESCRIPTION : Wine Quality Data Set 합치기
# -*- coding: utf-8 -*-

import os
import glob
import pandas as pd
import numpy as np


class MergeManager:
    def findmerged(self, merged):
        mergedfile = glob.glob("./**/" + merged, recursive=True)
        df = pd.DataFrame([])
        if len(mergedfile) == 1:
            df = pd.read_csv(mergedfile[0])
            return df
        elif len(mergedfile) < 1:
            self.mergeandcate(merged)
            df = pd.read_csv("./cminydata/" + merged)
            return df

    def mergeandcate(self, merged):
        wineAll = pd.DataFrame([])
        # data폴더 내의 모든 csv 파일 목록 불러오기
        csvList = glob.glob("./cminydata/*.csv")
        csvList.sort(reverse=True)
        # vinoCate 추가 후 merge
        for each_csv in csvList:
            filename = each_csv.split('/')[-1]
            if filename.endswith('red.csv'):
                vinoCate = "red"
            elif filename.endswith('white.csv'):
                vinoCate = "white"
            df_temp = pd.read_csv(each_csv, sep=';')
            df_temp = df_temp.reset_index(drop=True)
            df_temp['vinoCate'] = vinoCate
            wineAll = pd.concat([wineAll, df_temp])
        # csv 파일로 저장
        # wineAll.insert(0, 'idx', range(0, len(wineAll)))
        # wineAll = wineAll.reset_index(drop=True, inplace=True)
        wineAll.to_csv("./cminydata/" + merged)
