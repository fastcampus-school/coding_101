import requests # 요청을 보내기 위한 requests
from bs4 import BeautifulSoup # 응답을 분석하기 위한 BeautifulSoup

# url에 요청을 보낼 주소를 지정하고 requests로 요청을 보내 그 응답을 response에 저장합니다.
url = "https://www.rottentomatoes.com/"
response = requests.get(url)

# 응답 결과로 받은 html을 BeautifulSoup으로 분석합니다.
html = response.text
soup = BeautifulSoup(html, "html.parser")
# html 전체 중 id가 일치하는 table 태그를 선택합니다.
table = soup.find("table", attrs={"id":"Top-Box-Office"})
# table에서 모든 tr태그를 찾아냅니다.
all_tr = table.find_all("tr")
# tr태그 리스트 요소를 반복시키면서 td > span 의 텍스트를 추출해 score와 movie_name을 바로 출력합니다.
for tr in all_tr:
    all_td = tr.find_all("td")
    score = all_td[0].find("span", attrs={"class":"tMeterScore"}).text
    movie_name = all_td[1].a.text
    print(score, movie_name)
