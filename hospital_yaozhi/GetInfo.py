import urllib
import urllib.request
import urllib.request, urllib.parse
from bs4 import BeautifulSoup
from hospital_yaozhi.common import Bean, Dao
from hospital_yaozhi.db import MongoDbIn,MysqlIn,SqlServerIn
# -*- coding: UTF-8 -*-

errorCount = 0  # 失败次数
failCount = 0  # 爬取失败次数
successCount = 0  # 保存成功次数

target = 'https://db.yaozh.com/hmap/'

class GetUserListByBS4():

    def __init__(self):
        self.user = userDao.User()
        '''
        Constructor
        '''

    def get(self, url, coding):
        req = urllib.request.Request(url)
        req.add_header('user-agent',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36')
        response = urllib.request.urlopen(req)
        htmls = response.read()
        htm = htmls.decode(coding, 'utf-8')
        return htm

    def start(self):
        for i in range(80000, 81101):

            dao = Dao.Hospital()
            html = hospitalGet.get(target + str(i) + ".html", "utf-8")
            soup = BeautifulSoup(html, "html5lib")
            table = soup.find(name='table',class_="table")
            tableSoup = table
            if table:
                hospital = tableSoup.find_all(name='tr')
                if hospital:
                    for each in hospital:
                        hospitalTitle = each.find(name='th').get_text()
                        hospitalDetail = each.find(name='span').get_text().strip()
                        if hospitalTitle in Bean.TITLES[0]:
                            dao.HospitalName = hospitalDetail
                        if hospitalTitle in Bean.TITLES[1]:
                            dao.HosAliasName = hospitalDetail
                        if hospitalTitle in Bean.TITLES[2]:
                            dao.HospitalLevel = hospitalDetail
                        if hospitalTitle in Bean.TITLES[3]:
                            dao.HospitalType = hospitalDetail
                        if hospitalTitle in Bean.TITLES[4]:
                            dao.Provice = hospitalDetail
                        if hospitalTitle in Bean.TITLES[5]:
                            dao.City = hospitalDetail
                        if hospitalTitle in Bean.TITLES[6]:
                            dao.Count = hospitalDetail
                        if hospitalTitle in Bean.TITLES[7]:
                            dao.HospitalAdress = hospitalDetail
                        if hospitalTitle in Bean.TITLES[8]:
                            dao.HospitalCreateYear = hospitalDetail
                        if hospitalTitle in Bean.TITLES[9]:
                            dao.HospitalCharer = hospitalDetail
                        if hospitalTitle in Bean.TITLES[10]:
                            dao.HospitalMethod = hospitalDetail
                        if hospitalTitle in Bean.TITLES[11]:
                            dao.OutpatientVolume = hospitalDetail
                        if hospitalTitle in Bean.TITLES[12]:
                            dao.HospitalDepartments = hospitalDetail
                        if hospitalTitle in Bean.TITLES[13]:
                            dao.Email = hospitalDetail
                        if hospitalTitle in Bean.TITLES[14]:
                            dao.ZipCode = hospitalDetail
                        if hospitalTitle in Bean.TITLES[15]:
                            dao.HospitalWebsite = hospitalDetail
            MysqlIn.save(dao)


if __name__ == "__main__":
    hospitalGet = GetUserListByBS4()
    hospitalGet.start()
