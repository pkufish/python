# 导入模块
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import re
import os
import string


# 定义函数
def googleSearch(keywords):
    # 请求URL
    url = "https://lsrm.hinews.cn/xinwen/show-17283.html?" + keywords

    # 设置请求头和UA
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")
    browser = webdriver.Chrome(options=chrome_options)

    browser.get(url)

    # 获取网页源码
    html = browser.page_source

    # 关闭浏览器
    browser.close()

    # 新建soup对象获取html信息
    soup = BeautifulSoup(html, 'html.parser')

    # 获取搜索结果
    results = soup.find_all('p')
    # print(results)

     for result in results:
         print(result)

    # 定义搜索关键词
    keywords = "python"

    # 调用函数
    if __name__ == '__main__':
        googleSearch('1')
