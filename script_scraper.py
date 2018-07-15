# -*- coding: utf-8 -*-
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

def scr_ja():
    ### スクリプト保存用ディレクトリ作成
    if os.path.isdir("./ted_script_ja"):
        os.chdir("./ted_script_ja")
    else:
        os.mkdir("./ted_script_ja")
        os.chdir("./ted_script_ja")

    #for i in range(len(df)):
    for i in range(1133,len(df)):
        print(i)
        time.sleep(2)
        ### 日本語スクリプト抽出
        url = "https://www.ted.com/" + df["link"][i]+"/transcript?language=ja" 
        resp = requests.get(url)
        if resp.status_code == 200:
            f2 = open(str(i)+"_"+df["link"][i].split("/")[-1]+".txt","w")
            res = req.urlopen(url)
            soup = BeautifulSoup(res, 'html.parser')
            li_list = soup.find_all("p")
            li_str = str(li_list[-12])
            if li_str=='<p>Subscribe to receive email notifications\nwhenever new talks are published.</p>':
                for n in range(len(li_list[:-12])):                
                    f2.write(str(li_list[n]))
                    #print(li_list[i])
                count_list1.append(i)
                f_exist_ja.write(str(i)+"\n")
                #sys.exit(0)
            else:
                print("*"*40+"error"+"*"*40)
                count_list2.append(i)
                f_error_ja.write(str(i)+"\n")
                #sys.exit(0)
                pass
        elif resp.status_code == 404:
            count_list3.append(i)
            f_notexist_ja.write(str(i)+"\n")
            
    print("*"*40 + "日本語" + "*"*40)
    print("URLが存在し、抽出したスクリプト数: "+str(len(count_list1)))
    print("URLが存在するが、スクリプトの形式が異なり抽出失敗したスクリプト数: "+str(len(count_list2)))
    print("URLが存在しなく、抽出失敗したスクリプト数: "+ str(len(count_list3)))
    #sys.exit(0)
        

def scr_en():
    ### スクリプト保存用ディレクトリ作成
    if os.path.isdir("./ted_script_en"):
        os.chdir("./ted_script_en")
    else:
        os.mkdir("./ted_script_en")
        os.chdir("./ted_script_en")
    ### 日本語訳分だけ取得したければcount_list1を用いる
    #for i in range(count_list1):
    for i in range(len(df)):
        print(i)
        time.sleep(2)
        ### 英語スクリプト抽出
        url = "https://www.ted.com/" + df["link"][i]+"/transcript" 
        resp = requests.get(url)
        if resp.status_code == 200:
            f_en = open(str(i)+"_"+df["link"][i].split("/")[-1]+".txt","w")
            res = req.urlopen(url)
            soup = BeautifulSoup(res, 'html.parser')
            li_list = soup.find_all("p")
            li_str = str(li_list[-12])
            if li_str=='<p>Subscribe to receive email notifications\nwhenever new talks are published.</p>':
                for n in range(len(li_list[:-12])):                
                    f_en.write(str(li_list[n]))
                count_list4.append(i)
                f_exist_en.write(str(i)+"\n")
                #sys.exit(0)
            else:
                print("*"*40+"error"+"*"*40)
                count_list5.append(i)
                f_error_en.write(str(i)+"\n")
                #sys.exit(0)
                pass
        elif resp.status_code == 404:
            count_list6.append(i)
            f_notexist_en.write(str(i)+"\n")

    print("*"*40 + "英語" + "*"*40)
    print("URLが存在し、抽出したスクリプト数: "+str(len(count_list4)))
    print("URLが存在するが、スクリプトの形式が異なり抽出失敗したスクリプト数: "+str(len(count_list5)))
    print("URLが存在しなく、抽出失敗したスクリプト数: "+ str(len(count_list6)))
    

if __name__ == "__main__":
    df = pd.read_csv("./ted-link.csv")
    f_notexist_ja = open("notexist_number_ja.txt","w")
    f_exist_ja = open("exist_number_ja.txt","w")
    f_error_ja = open("error_ja.txt","w")
    f_notexist_en = open("notexist_number_en.txt","w")
    f_exist_en = open("exist_number_en.txt","w")
    f_error_en = open("error_en.txt","w")
    count_list1 = []
    count_list2 = []
    count_list3 = []
    count_list4 = []
    count_list5 = []
    count_list6 = []
    scr_ja()
    scr_en()
    f_error_ja.close() 
    f_notexist_ja.close()
    f_exist_ja.close()
    f_error_en.close() 
    f_notexist_en.close()
    f_exist_en.close()
