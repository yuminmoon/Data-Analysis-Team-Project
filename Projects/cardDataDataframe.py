# -*- coding:utf-8 -*-
import pandas as pd

cdDF = pd.read_csv("d:/yumin/jejuData/cardData1.csv", encoding='euc-kr', 
names=['년월','시도명','지역구분','읍면동명','업종코드','업종명','이용자구분','관광구분','연령대','성별','이용금액','매장수','업종명대분류','데이터기준일자']) 
print(cdDF)
# print(cdDF.info())