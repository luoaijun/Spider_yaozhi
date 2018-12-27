from pyquery import PyQuery as pq
import requests
from multiprocessing import Pool
import pymongo
import pymysql
import urllib.request, urllib.parse
import pyodbc
from bs4 import BeautifulSoup

# -*- coding: UTF-8 -*-

# MongoDB 数据库连接信息
client = pymongo.MongoClient('39.106.53.34')
db = client['hospital']
# Mysql 数据库连接信息
mysqlConn = pymysql.connect(host='39.106.53.34',
                            user='root',
                            password="luoaijun",
                            database='pachong',
                            port=3306,
                            charset='utf8')
# SQLServer 连接信息
# conn = pyodbc.connect('DRIVER={SQL Server};SERVER=cn1001232;DATABASE=TestDB;UID=sa;PWD=zhangming')

errorCount = 0  # 失败次数
failCount = 0  # 爬取失败次数
successCount = 0  # 保存成功次数

target = 'https://db.yaozh.com/hmap/'
urls = []  # 存放省链接
allhosurls = []  # 存放所有医院简介链接
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36",
}
titles = ["医院名称	", "医院等级", "医院类型",
          "省", "市", "县", "医院地址", "建院年份", "负责人", "经营方式", "门诊量(日)", "医院科室", "邮箱", "邮编", "医院网址"]


def get_page(i):
    try:
        url = target + str(i) + '.html'
        doc = pq(requests.get(url, headers=HEADERS).text)
        mysql_parse_page(url)
    except Exception:
        print('Mysql: 爬取第', i, '页失败')


def mysql_parse_page(url):
    req = requests.get(url,headers=HEADERS)
    html = req.text
    soup = BeautifulSoup(html, "html5lib")  # 1
    table = soup.findall(name='table', attrs={'class':"table"})  # 2
    a_bf = BeautifulSoup(str(table[0]), "html5lib") #3
    th = a_bf.find_all(name='th')
    td = a_bf.find_all(name='td')
    vals = []
    if len(th):
        for each in th:
            temp = each.get_text()
            if temp in titles:
                continue
            vals.append(temp)
    if len(td):
        for each in td:
            temp = each.get_text()
            if temp in titles:
                continue
            vals.append(temp)


# save_mysql(vals)


def save_mongo(dic):
    global errorCount
    global successCount
    if db['hospital_detail_01'].insert(dic):
        successCount += 1
    else:
        errorCount += 1


def save_mysql(vals):
    # 连接之后需要先建立cursor：
    cursor = mysqlConn.cursor()
    try:
        cursor = mysqlConn.cursor()
        cursor.execute(
            'insert into HospitalsInfo(HosAliasName,Region,President,BuildYear,HosType,HosLevel,SectionCount,DoctorCount,BedCount,YearOutpatient,IsInsurance) values(?,?,?,?,?,?,?,?,?,?,?)'
            , (vals[0], vals[8], vals[1], vals[2], vals[3], vals[4], vals[9], vals[5], vals[10], vals[6], vals[7]))
        mysqlConn.commit()  # 不执行不能插入数据
        print('insert one data')
    except Exception as e:
        print(str(e))
    finally:
        mysqlConn.close()


def main(i):
    get_page(i)


if __name__ == '__main__':
    # global errorCount ,failCount ,successCount
    pool = Pool()
    pool.map(main, [i for i in range(1, 2)])
    #   print('爬取结束：\n总共失败' + errorCount + '次\n总共成功' + successCount + '次\n爬取失败' + failCount + '次')
    pool.close()
    pool.join()
