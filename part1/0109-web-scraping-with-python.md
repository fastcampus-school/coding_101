# Python으로 웹스크래핑하기(Web Scraping with Python)

## World Wide Web(WWW)

- URL로 구분된 하이퍼텍스트(Hypertext)를 공유하는 정보의 공간
	- text: 텍스트는 이렇게 생겼구요
	- Hypertext: [하이퍼텍스트](https://en.wikipedia.org/Hypertext)는 이렇게 생겼답니다.

## HTTP(HyperText Transfer Protocol)

- 하이퍼텍스트를 주고 받기 위한 서로간의 약속

![](img/server-client.png)

## Web Crawling
- 웹을 자동으로 탐색하며 구조화된 정보(xml, html 등)을 수집하는 일

## Web Scraping
- 웹에 게시된 문서를 수집하는 행위

## Requirements
- Python으로 웹 스크래핑을 하기 위해 필요한 라이브러리를 알아봅시다.

### requests
- Python에서 웹 서버에 요청을 보내고 응답을 받는 행위와 관련된 라이브러리
- `pip install requests`

### beautifulsoup
- 요청을 통해 받은 응답을 분석하여 원하는 값을 얻을 수 있도록 도와주는 라이브러리
- `pip install beautifulsoup4`