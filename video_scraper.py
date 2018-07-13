import requests
import os
import random
import urllib.request as req
from bs4 import BeautifulSoup
import csv
import pandas as pd
import re
import time
import sys

df = pd.read_csv("./ted-link.csv")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("参照するcsvのURLは以下になります")
print(df["link"][:])
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
### 動画保存用ディレクトリ作成
if os.path.isdir("./ted_videos"):
    os.chdir("./ted_videos")
else:
    os.mkdir("./ted_videos")
    os.chdir("./ted_videos")

### 抽出できなかったcsvのdf["link"][count1]を保存するテキストファイル
text_df = open("../unscraped_df[link][count1].txt","w")

### 変数準備
### 全体
count1 = 0
### スクレイピングに成功した数
count2 = 0
### スクレイピングに失敗した数
count3 = 0
for i in range(len(df)):
    time.sleep(5)
    url = "https://www.ted.com/" + df["link"][i]
    res = req.urlopen(url)
    soup = BeautifulSoup(res, 'html.parser')
    li_list = soup.find_all('script')
    li_list = str(li_list)
    ### 2018年5月までは下記の正規表現で動画が取れたが現在では不可(2018/7月)
    #match = re.search("{\"64k\"(.*)\"},\"180k\"",li_list)
    match = re.search("{\"low\":(.*)\",\"medium\"",li_list)
    if match !=None:
        script1 = match.group()
        ### 以前は[5]だった
        #video_URL = script1.split("\"")[5]
        video_URL = script1.split("\"")[3]
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("video_URL: "+video_URL)
        res = requests.get(video_URL)
        filename = df["link"][i].split("/")[2]
        with open(str(i) + "_" + filename + ".mp4","wb") as f:   
            f.write(res.content)
            count1 = count1 + 1
            count2 = count2 + 1
            print("Video crawled.")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
            #sys.exit(0)
    else:
        text_df.write("de[\"link\"]["+str(count1)+"]"+"\n")
        count1 = count1 + 1
        count3 = count3 + 1
        print("失敗.")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
        #sys.exit(0)
text_df.close()  

print("videos crawled!!: " + str(count2) + "videos.")
print("Number of Unscraped videos: " + str(count3) + "videos.")
