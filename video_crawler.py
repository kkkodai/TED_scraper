# coding: UTF-8
import urllib
from bs4 import BeautifulSoup
import time

# 変数準備
url = "https://www.ted.com/talks?page="
total_page = 77  ## 20180423で77まである
count =0
# csvファイル新規作成
file = open('./ted-link_video.csv','a')
file.write("#,link\n")

# スクレイビング開始
for page_num in range(total_page,78):

    # URLにアクセス、取得したページ内容をBeautifulsoupに格納し解析準備
    html = urllib.request.urlopen(url+str(page_num))
    soup = BeautifulSoup(html, "html.parser")
    
    # 進捗確認のため現ページ数を表示
    print(page_num)

    # 過剰アクセスを防ぐため5秒休憩
    time.sleep(5)
    
    # プレゼンへのリンクを取得
    for link in soup.find_all(class_=" ga-link"):
        count = count + 1
    
        #1プレゼン当たり画像とタイトル計2個のリンクがあるため重複を防ぐ
        if count % 2 == 0:
            file.write(str(count/2)+","+link.get('href')+","+"\n")
        
file.close()