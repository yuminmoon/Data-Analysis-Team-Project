# -*- coding:utf-8 -*-
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from http.client import HTTPSConnection
from bs4 import BeautifulSoup
from konlpy.tag._okt import Okt
from hanspell import spell_checker
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
from urllib.parse import quote
# https://map.naver.com/v5/search/%EC%A0%9C%EC%A3%BC%EB%8F%84%20%EB%A7%9B%EC%A7%91?c=14060546.9964590,3952164.0916793,9,0,0,0,dh
wc = {}
o = Okt()
q = quote("제주도 맛집")
con = HTTPSConnection("map.naver.com")
# for p in range(1, 11):
con.request("GET", "/v5/search/%s?c=14060546.9964590,3952164.0916793,9,0,0,0,dh" %q)
rb = con.getresponse().read()
print(rb.decode())
recipe = BeautifulSoup(rb, 'html.parser', from_encoding='utf-8')
recipes = recipe.select("span._3Yilt")
    
for r in recipes:
    txt = r.text  
    # print(txt)
    # try:
        # txt = o.normalize(txt)
        # txt = spell_checker.check(txt).checked
        # txt = o.pos(txt, stem=True)
        # for t, p in txt:
            # if p == 'Noun' or p == 'Verb':
                # if t != '요리':
                    # if t in wc:
                        # wc[t] += 1
                    # else:
                        # wc[t] = 1
    # except:
        # pass
 
con.close()
# print(wc)
#
# w, c = [], []
# for k, v in wc.items():
    # if k != None:
        # w.append(k)
        # c.append(v)
        #
# df = pd.DataFrame()
# df['w'] = w
# df['c'] = c
# df = df.sort_values(by='c', ascending=False)
# df = df.head(20)
# print(df)
#
# fontFile = "C:/Windows/Fonts/malgun.ttf"
# fontName = fm.FontProperties(fname=fontFile, size=50).get_name()
# plt.rc("font", family=fontName)
#
# sns.barplot(x='w',  y='c', data=df)
# # plt.pie(df['c'], autopct='%d', labels=df['w'])
# plt.title('단어별 등장횟수')
# plt.show()