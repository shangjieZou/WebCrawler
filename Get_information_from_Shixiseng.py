import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Error Occured when getting url"


def parsePage(html):
    try:
        # data-sname="96" data-desc="search-公司名称">深声科技</a>
        # <span class="type">数据库</span>
        # data-desc="search-职位名称">实习&#xe22d（数据审核员）</a>
        Company_pattern = r"data-sname=\"96\" data-desc=\"search-公司名称\">(.+)</a>"
        Company_name = str(re.findall(Company_pattern,html))
        Responsibility_pattern = r"<span class=\"type\">(.+)</span>"
        Responsibility_name = str(re.findall(Responsibility_pattern,html))
        Job_Title_pattern = r"data-desc=\"search-职位名称\">（.+）</a>"
        Job_Title = str(re.findall(Job_Title_pattern,html))
        Job_Title.strip("&#xe22d")
        Company_list = Company_name.split(",")
        Responsibility_list = Responsibility_name.split(",")
        Job_list = Job_Title.split(",")
        # use this block to check problem when Error Occured in Parse
        if(0):
            print(Company_list)
            print(len(Company_list))
            print(Responsibility_list)
            print(len(Responsibility_list))
            print(Job_list)
            print(len(Job_list))
        for i in range(10):
            print(Company_list[i]+"  "+Responsibility_list[i])
    except:
        print("Error Occured in Parse")


def main():
    job_title = '数据'   # key word for browsing
    depth = 10   # similar to the number of pages to be scanned
    Job_url_start = 'https://www.shixiseng.com/interns/c-440100_?k=' + job_title
    for i in range(1,depth+1):
        try:
            url = Job_url_start + '&p=' + str(i)
            html = getHTMLText(url)
            print(url)
            parsePage(html)
        except:
            continue


main()
