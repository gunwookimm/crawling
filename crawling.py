import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N', headers=headers)
# https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309
# https://www.genie.co.kr/chart/top200?ditc=D&rtm=N

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

rawdata = soup.select('.newest-list > .music-list-wrap > .list-wrap tr')
date = soup.select('.chart-date input#curDateComma')[0]['value']

rank = 1
print(date, "지니차트 순위")
for titleitem in rawdata:
    song_title = titleitem.select_one('a.title.ellipsis')
    song_artist = titleitem.select_one('a.artist.ellipsis')
    if song_title is not None:
        print('[' + str(rank) + ']', song_title.string.strip(), "-", song_artist.string)
        rank += 1
