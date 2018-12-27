import pymongo
import pymysql
import pyodbc
import urllib
import urllib.request
from user import userDao
from pyquery import PyQuery as pq
import requests
from multiprocessing import Pool
import urllib.request, urllib.parse
from bs4 import BeautifulSoup
from hospital_yaozhi.common import Bean

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36",
}
TITLES = ["医院名称	",
          "医院别名	",
          "医院等级",
          "医院类型",
          "省",
          "市",
          "县",
          "医院地址",
          "建院年份",
          "负责人",
          "经营方式",
          "门诊量(日)",
          "医院科室",
          "邮箱",
          "邮编",
          "医院网址"]

# MongoDB 数据库连接信息
client = pymongo.MongoClient('39.106.53.34')
MONGDB = client['hospital']
# Mysql 数据库连接信息
MYSQLCONN = pymysql.connect(host='39.106.53.34',
                            user='root',
                            password="luoaijun",
                            database='pachong',
                            port=3306,
                            charset='utf8')
# SQLServer 连接信息
#SQLSERVERCONN = pyodbc.connect('DRIVER={SQL Server};SERVER=cn1001232;DATABASE=TestDB;UID=sa;PWD=zhangming')
