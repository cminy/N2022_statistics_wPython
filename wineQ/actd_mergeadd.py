# DESCRIPTION : Wine Quality Data Set 합치기
# -*- coding: utf-8 -*-

import os
import glob
import pandas as pd
import numpy as np


class MergeManager:
    def findmerged(self, merged):
        mergedfile = glob.glob("./**/" + merged, recursive=True)
        winedf = pd.DataFrame([])
        if len(mergedfile) == 1:
            winedf = pd.read_csv(mergedfile[0])
            return winedf
        elif len(mergedfile) < 1:
            self.mergeandcate(merged)

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
            df = pd.read_csv(each_csv, sep=';')
            df['vinoCate'] = vinoCate
            wineAll = pd.concat([wineAll, df])
        # 인덱스 새로 붙이고 csv 파일로 저장
        wineAll.insert(0, 'idx', range(0, len(wineAll)))
        wineAll.to_csv("./cminydata/wineAll.csv")
        self.findmerged(merged)
