import requests
import re
from bs4 import BeautifulSoup
import sys

def get_url_txt(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Error Occured in get_url_txt"


    # for first time use
def get_page_structure(url):
    Target_page = get_url_txt(url)
    Target_page_soup = BeautifulSoup(Target_page, "html.parser")
    return Target_page_soup

def get_html_list_for_parts(url):
    BioBrick_pattern = r"<TR><TD><A class='noul_link part_link' href='(.+)'>BBa_"
    BioBrick_html = str(re.findall(BioBrick_pattern, url))







