import pandas as pd
import copy
import glob
import os
import sys


def ja_regex():
    print("日本語スクリプトの正規表現処理を行います")
    if not os.path.isdir("./ted_script_ja_regex"):
        os.mkdir("./ted_script_ja_regex")


    text_list = glob.glob('./ted_script_ja/*.txt')
    #df = pd.read_csv("./ted-link.csv")
    new_dict ={}

    for text in text_list:
        text1 = text.split("/")[2]
        text_num = text1.split("_")[0]
        ### 文字列数値から整数型数値へ変換
        new_dict[int(text_num)]=text
    ### ソート
    sorted_dict = sorted(new_dict.items(), key=lambda x: x[0])
    for N,file in sorted_dict:
        file1 = file.split("/")[-1]
        print(file1)
        #file_number = file1.split("_")[0]
        #name = df["link"][int(file_number)].split("/")[-1]
        file_ja = open("./ted_script_ja_regex/"+file1,"w")
        #print(name)
        f = open(file,"r")
        f = f.readlines()
        #print(f)
        #f3 = copy.deepcopy(f)
        #f3[0] ="*"*5 + name + "*"*5 +"\n" + f[0]
        for line in f:
            line=line.replace("\t","")
            line=line.replace("<p>","")
            line=line.replace("</p>","")
            file_ja.write(line)
            #print(line.strip())
        file_ja.close()
        #if N == 2:
        #    sys.exit(0)


def en_regex():
    print("英語スクリプトの正規表現処理を行います")
    if not os.path.isdir("./ted_script_en_regex"):
        os.mkdir("./ted_script_en_regex")
    text_list = glob.glob('./ted_script_en/*.txt')
    #df = pd.read_csv("./ted-link.csv")
    new_dict ={}

    for text in text_list:
        text1 = text.split("/")[2]
        text_num = text1.split("_")[0]
        ### 文字列数値から整数型数値へ変換
        new_dict[int(text_num)]=text
    ### ソート
    sorted_dict = sorted(new_dict.items(), key=lambda x: x[0])
    for N,file in sorted_dict:
        file1 = file.split("/")[-1]
        print(file1)
        #file_number = file1.split("_")[0]
        #name = df["link"][int(file_number)].split("/")[-1]
        file_en = open("./ted_script_en_regex/"+file1,"w")
        #print(name)
        f = open(file,"r")
        f = f.readlines()
        #f3 = copy.deepcopy(f)
        #f3[0] ="*"*5 + name + "*"*5 +"\n" + f[0]
        #print(len(f3))
        for line in f:
            line=line.replace("\t","")
            line=line.replace("<p>","")
            line=line.replace("</p>","")
            file_en.write(line)
            #print(line.strip())
        file_en.close()
        #if N == 1:
        #    sys.exit(0)

if __name__ == "__main__":
    en_regex()
    ja_regex()