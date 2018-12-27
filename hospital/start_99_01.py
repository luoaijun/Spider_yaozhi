# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests, sys
import pymysql
"""
类说明:获取99健康网的医院信息
Parameters:
    无
Returns:
    无
Modify:
    2017-09-13
"""


class gethosinfo(object):

    def __init__(self):
        self.target = 'https://yyk.99.com.cn'
        self.urls = []  # 存放省链接
        self.allhosurls = []  # 存放所有医院简介链接
        self.gat = ["香港", "澳门", "台湾"]
        self.titles = ["医院别名", "所在地区", "院长姓名", "建院年份", "医院类型", "医院等级", "科室数量", "医护人数", "病床数量", "年门诊量", "是否医保"]

    """
    函数说明:获取各省份链接
    Parameters:
        无
    Returns:
        无
    Modify:
        2018-11-23
    """

    def get_province_url(self):
        req = requests.get(url=self.target)
        html = req.text
        div_bf = BeautifulSoup(html, "html5lib")
        div = div_bf.find_all('div', class_='area-list')
        a_bf = BeautifulSoup(str(div[0]), "html5lib")
        a = a_bf.find_all('a')
        for each in a:
            temp = each.get('href')
            temptitle = each.get('title')
            if temp is None or temptitle in self.gat:
                continue
            prourl = self.target + each.get('href')
            self.get_hosdesc_url(prourl)
            """
            self.urls.append(self.target + each.get('href'))
            print(self.target + each.get('href'))
            """

    """
    函数说明:获取某个省份所有医院简介的连接
    Parameters:
        无
    Returns:
        无
    Modify:
        2018-11-23
    """

    def get_hosdesc_url(self, prourl):
        req = requests.get(url=prourl)
        html = req.text
        div_bf = BeautifulSoup(html, "html5lib")
        div = div_bf.find_all('div', class_='g-warp')
        if len(div):
            a_bf = BeautifulSoup(str(div[0]), "html5lib")
            td = a_bf.find_all('td')
            urls = []
            for each in td:
                a_array = each.find_all('a')
                if len(a_array):
                    a = a_array[0]
                    temp = a.get('href')
                    if temp is None:
                        continue
                    urls.append(self.target + temp + "jianjie.html")
            """
            开始获取数据
            """
            self.getalldata(urls)

    """
    函数说明:根据医院连接获取所有数据
    Parameters:
        无
    Returns:
        无
    Modify:
        2018-11-23
    """

    def getalldata(self, urls):
        """
        遍历所有医院链接，获取数据
        """
        for each in urls:
            req = requests.get(url=each)
            html = req.text
            div_bf = BeautifulSoup(html, "html5lib")
            table = div_bf.find_all('table', class_='present-table')
            a_bf = BeautifulSoup(str(table[0]), "html5lib")
            span = a_bf.find_all('span')
            a = a_bf.find_all('a')

            vals = []
            if len(span):
                for each in span:

                    temp = each.get_text()
                    if temp in self.titles:
                        continue
                    vals.append(temp)
            if len(a):
                for each in a:
                    temp = each.get_text()
                    if temp in self.titles:
                        continue
                    vals.append(temp)
            self.insertallinfo(vals)

    """
    函数说明:插入数据库
    Parameters:
        无
    Returns:
        无
    Modify:
        2018-11-23
    """

    def insertallinfo(self, vals):  # 插入SQL数据库
        # import pyodbc
        # conn = pyodbc.connect('DRIVER={SQL Server};SERVER=cn1001232;DATABASE=TestDB;UID=sa;PWD=zhangming')
        conn = pymysql.connect(host='39.106.53.34',
                               user='root',
                               password="luoaijun",
                               database='pachong',
                               port=3306,
                               charset='utf8')
        # 连接之后需要先建立cursor：
        cursor = conn.cursor()
        try:
            cursor = conn.cursor()
            cursor.execute(
                'insert into HospitalsInfo(HosAliasName,Region,President,BuildYear,HosType,HosLevel,SectionCount,DoctorCount,BedCount,YearOutpatient,IsInsurance) values(?,?,?,?,?,?,?,?,?,?,?)'
                , (vals[0], vals[8], vals[1], vals[2], vals[3], vals[4], vals[9], vals[5], vals[10], vals[6], vals[7]))
            conn.commit()  # 不执行不能插入数据
            print('insert one data')
        except Exception as e:
            print(str(e))
        finally:
            conn.close()


if __name__ == "__main__":
    dl = gethosinfo()
    dl.get_province_url()
    """
    dl.get_hosdesc_url()
    """

