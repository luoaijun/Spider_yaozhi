from pyquery import PyQuery as pq
import requests
from multiprocessing import Pool
import pymongo
import pymysql
import pyodbc

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
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=cn1001232;DATABASE=TestDB;UID=sa;PWD=zhangming')

errorCount = 0  # 失败次数
failCount = 0  # 爬取失败次数
successCount = 0  # 保存成功次数


def get_page(i):
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
        }
        url = 'https://db.yaozh.com/hmap/' + str(i) + '.html'
        doc = pq(requests.get(url, headers=headers).text)
        parse_page(doc)
    except Exception:
        print('爬取第', i, '页失败')


def parse_page(doc):
    global failCount
    try:
        items = doc('body > div.main > div.body.detail-main.no-side > div.table-wrapper > table > tbody').items()
        item_name = []
        item_detail = []
        for item in items:
            item_name.append(item.find('.detail-table-th').text())
            item_detail.append(item.find('.toFindImg').text())
            item_detail.append(' ')
            item_name.append(' ')
        new_item_name = list(str(item_name).split(' '))
        new_item_detail = list(str(item_detail).split(' '))
        dic = dict(zip(new_item_name, new_item_detail))
        save_mongo(dic)

    except Exception:
        failCount += 1


def save_mongo(dic):
    global errorCount
    global successCount
    if db['hospital_detail'].insert(dic):
        successCount += 1
    else:
        errorCount += 1





def main(i):
    get_page(i)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i for i in range(1, 73174)])
    print('爬取结束：\n总共失败' + errorCount + '次\n总共成功' + successCount + '次\n爬取失败' + failCount + '次')
    pool.close()
    pool.join()
