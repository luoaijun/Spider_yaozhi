
import urllib
import urllib.request
from bs4 import BeautifulSoup
from user import userDao
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36",
}
class GetUserListByBS4():

    def __init__(self):
        self.user = userDao.User()
        '''
        Constructor
        '''

    def get(self, url, coding):
        req = urllib.request.Request(url)
        req.add_header( 'user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36')
        response = urllib.request.urlopen(req)
        htmls = response.read()
        htm = htmls.decode(coding, 'utf-8')
        return htm


if __name__ == "__main__":
    get = GetUserListByBS4()
    html = get.get("https://db.yaozh.com/hmap/1.html", "utf-8")
    soup = BeautifulSoup(html, "html.parser")
    trs = soup.find_all(name='td')
    userList = list()
    for tr in trs:
        user = userDao.User()
        _soup = BeautifulSoup(str(tr), "html.parser")
        tds = _soup.find_all(name='td')
        _id = _soup.input['id']
        user.setId(_id)
        user.setName(str(tds[1].string))
        user.setAge(str(tds[2].string))
        userList.append(user)

    for i in userList:
        print(i)
