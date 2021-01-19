from bs4 import BeautifulSoup
import requests
import logging

"""
분석, README 발
오늘의 매경 : https://www.mk.co.kr/today-paper/ 에서 값을 긁어와야함

1. https://www.mk.co.kr/today-paper/
    - 오늘의 기사의 모든 링크가 모여있는 곳
    - 필요한 정보를 가지고 있는 곳
    - ```
      <a href="https://www.mk.co.kr/today-paper/view/2021/4746876/" 
      class="nclicks(cls_eco.clsart1)">
        백신 못미더운 국민들…3명중 2명 "일단 지켜본 후 맞을것"
      </a>
      ```
2. https://www.mk.co.kr/today-paper/view/2021/{기사코드}/
    - 제목 
        - ```
          <h3 class="article_title">
          ...
          </h3>
          ```
    - 부제목
        - ```
          <h2 class="sub_title1">
            ...
          </h2>
          ```
    - 본문 
        - ```
          <div class="article_body" id="article_body">
            ....          
          </div>
          ```
"""


class Content:
    """
    페이지에 적용시킬 기반 클래스
    """

    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        """
        테스트용! 콘솔에 출력시키기
        :return: void
        """
        print("URL: {}".format(self.url))
        print("Title: {}".format(self.title))
        print("Content: \n\t{}".format(self.body))


class WebSite:
    """
    웹 사이트 구조에 관한 정보를 저장할 클래스
    """

    def __init__(self, name, url, titleTag, subTitleTag, bodyTag, internalLinkTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.subTitleTag = subTitleTag
        self.bodyTag = bodyTag
        self.internalLinkTag = internalLinkTag
