from .Models import Content, WebSite
import requests
from bs4 import BeautifulSoup


class Crawler:

    @staticmethod
    def getPage(url):
        """
        해당 url의 html 문서를 Beautiful Soup로 변환시켜주는 역할
        만약 받아오는데 실패했다면 None 객체를 반환함
        :param url: html 문서를 받을 url
        :return:
        """
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        else:
            return BeautifulSoup(req.text, 'html.parser')

    @staticmethod
    def safeGet(pageObj, selector):
        """
        BeautifulSoup 객체와 선택자를 받아 콘텐츠 문자열을 추출하는 함수
        주어진 선택자로 검색된 결과가 없다면 빈 list를 반환한다.
        :param pageObj:
            BeautifulSoup 객체
        :param selector:
            문자열을 받아올 class 나 Tag 이름
        :return:
            선택된 문자열의 배열
        """
        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            try:
                return [elem.get_text.join('\n') for elem in selectedElems]
            except AttributeError:
                return []
            except Exception as e:
                print("safeGet Error")
                raise e

    def parse(self, site, bs):
        """
        BeautifulSoup 객체를 받아 콘텐츠를 추출한다.
        :param site:
            WebSite 객체로 분석해야 할 내용을 가지고 있음
        :param bs:
            html 문서를 받아온 BeautifulSoup 객체
        :return:
        """

        # bs = self.getPage(url)
        if bs is not None:
            title = "".join(self.safeGet(bs, site.titleTag))
            body = "".join(self.safeGet(bs, site.bodyTag))
            if title != "" and body != "":
                content = Content(url, title, body)
                content.print()


class TodayArticleCrawler(Crawler):
    articleUrlDict = {}

    def getArticleUrlList(self, todayPaperUrl, site):
        """
        오늘의 신문 링크와 site 객체를 받아 기사 url 들을 수집하는 함수
        :param todayPaperUrl:
            오늘의 신문 URL
        :param site:
            site 속성을 담고 있는 WebSite 객체
        :return: 추가된 list 내용
        """

        bs = Crawler.getPage(todayPaperUrl)
        tmp = []

        if bs is not None:
            tmp.append(Crawler.safeGet(bs, site.internalLinkTag))
        self.articleUrlDict.update({site.name: tmp})

        return tmp

    def clearCache(self, siteNames=None):
        """
        article url 을 제거하는 명령
        :return:
        """

        if siteNames is None:
            tmp = self.articleUrlDict
            self.articleUrlDict = {}

        else:
            tmp = {}
            for siteName in siteNames:
                try:
                    tmp.update(self.articleUrlDict.pop(siteName))
                except KeyError:
                    print("{} does not exist".format(siteName))
                    continue

        return tmp

    def parseArticle(self, site):
        for url in self.articleUrlDict:
            bs = self.getPage(url)
            Crawler.parse(site, bs)
