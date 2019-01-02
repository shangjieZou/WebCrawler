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


def parsePage(list_job, html):
    try:
        # data-sname="96" data-desc="search-公司名称">深声科技</a>
        # <span class="type">数据库</span>
        # data-desc="search-职位名称">实习&#xe22d（数据审核员）</a>
        Company_pattern = r"data-sname=\"96\" data-desc=\"search-公司名称\">(.+)</a>"
        Company_name = re.findall(Company_pattern,html)
        Responsibility_pattern = r"<span class=\"type\">(.+)</span>"
        Responsibility_name = re.findall(Responsibility_pattern,html)
        Job_Title_pattern = r"data-desc=\"search-职位名称\">（.+）</a>"
        Job_Title = re.findall(Job_Title_pattern,html).strip("&#xe22d")
        for i in range(len(Company_name)):
            list_job.append([Company_name,Responsibility_name,Job_Title])
    except:
        print("Error Occured in Parse")


def printJobList(list_job):
    pass


def main():
    job_title = '数据'   # key word for browsing
    depth = 2   # similar to the number of pages to be scanned
    Job_url_start = 'https://www.shixiseng.com/interns/c-440100_?k=' + job_title
    list_job = []
    for i in range(depth):
        try:
            url = Job_url_start + '&p=' + str(i)
            html = getHTMLText(url)
            parsePage(list_job, html)
        except:
            continue
    printJobList(list_job)


main()