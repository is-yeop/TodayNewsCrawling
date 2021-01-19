# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from OnlyMK.Crawler import TodayArticleCrawler
from OnlyMK.Models import WebSite
from csv import DictReader, DictWriter

crawler = TodayArticleCrawler()

siteData = [
    {
        "name": "매일경제",
        "url": "www.mk.co.kr",
        "titleTag": "h1.top_title",
        "subTitleTag": ""
     }
]

