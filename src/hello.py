# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def main():
    #--- 取得URLの決定
    url = 'https://github.com/librariapj'
    #--- requestsでdom取得
    response = requests.get(url)
    #--- 取得結果の表示
    print(response)
    # print(response.text)
    #--- BS4に取得内容を格納
    soup = BeautifulSoup(response.content, 'html.parser')
    #--- BS4の出力
    # 全文
    #print(soup.prettify())
    # aタグ
    print(soup.find_all("a"))

if __name__ == "__main__":
    main()
