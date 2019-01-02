import requests
from bs4 import BeautifulSoup
import bs4



# Get HTML page
def getHTMLTest(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Error Occured"


def getUniList(info):
    html_relating_list = []
    str_info = str(info)
    str_info_split = str_info.split()
    for i in range(len(str_info_split)):
        str_relating_info = ''
        if str_info_split[i] == "University" or str_info_split[i] == "university":
            for j in range(i-5, i+5):
                str_relating_info += str_info_split[j] + ' '
            html_relating_list.append(str_relating_info)

    return html_relating_list


def main():
    url = "https://www.timeshighereducation.com/world-university-rankings/2019/world-ranking#!/page/0/length/-1/sort_by/rank/sort_order/asc/cols/stats"
    info = getHTMLTest(url)
    #soup = BeautifulSoup(info, "html.parser")
    #soup_better = soup.prettify()
    Relating_info = getUniList(info)

    for i in range(len(Relating_info)):
        print(Relating_info[i])
        print("\n")

main()





