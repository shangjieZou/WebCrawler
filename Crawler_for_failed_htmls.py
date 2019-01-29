import requests
import re
from bs4 import BeautifulSoup


def get_url_txt(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Error Occured in get_url_txt"



def from_parts_html_get_seq():
    f_positive = open('Positive-promoter-failed-html.txt','r')
    content_positive = f_positive.read()
    Positive_promoters_html = content_positive.split('\n')
    #print(len(Positive_promoters_html))
    #print(Positive_promoters_html)
    f_positive.close()
    f_constitutive = open('Constitutive-promoter-failed-html.txt', 'r')
    content_constitutive = f_constitutive.read()
    Constitutive_promoters_html = content_constitutive.split('\n')
    #print(len(Constitutive_promoters_html))
    #print(Constitutive_promoters_html)
    f_constitutive.close()
    f_Negative = open('Negative-promoter-failed-html.txt', 'r')
    content_negative = f_Negative.read()
    Negative_promoters_html = content_negative.split('\n')
    #print(len(Negative_promoters_html))
    #print(Negative_promoters_html)
    f_Negative.close()

    def get_seq_from_html(html):
        part_name_pattern = r"var PrimaryPartName = \'(.+)\'; var PrimaryPartID"
        part_seq_pattern = r"var sequence = new String((.+));\s*var subParts"
        part_name = str(re.findall(part_name_pattern, html))
        part_seq_list = list(set(list(re.findall(part_seq_pattern, html)[0])))
        part_seq = eval(part_seq_list[0])
        if(1):
            #print(part_name)
            #print(part_seq)
            return part_name+" : "+part_seq + "\n"
        if(0):
            return part_seq + "\n"

    def get_name(html):
        part_name_pattern = r"var PrimaryPartName = \'(.+)\'; var PrimaryPartID"
        part_name = str(re.findall(part_name_pattern, html))
        return part_name




    if(0):
        k=0
        f = open('Positive_failed_seqs_with_ref.txt', 'w')
        for i in range(len(Positive_promoters_html)):
            try:
                url = Positive_promoters_html[i]
                print(url)
                html = get_url_txt(url)
                f.write(get_seq_from_html(html))
                k += 1
                print(get_name(html)+"finished" + str(k))
            except:
                continue
        f.close()


    if(0):
        k=0
        f = open('Constitutive_failed_seqs_with_ref.txt', 'w')
        for i in range(len(Constitutive_promoters_html)):
            try:
                url = Constitutive_promoters_html[i]
                print(url)
                html = get_url_txt(url)
                f.write(get_seq_from_html(html))
                k += 1
                print(get_name(html)+"finished" + str(k))
            except:
                continue
        f.close()

    if(0):
        k = 0
        f = open('Negative_failed_seqs_with_ref.txt', 'w')
        for i in range(len(Negative_promoters_html)):
            try:
                url = Negative_promoters_html[i]
                print(url)
                html = get_url_txt(url)
                f.write(get_seq_from_html(html))
                k += 1
                print(get_name(html) + "finished" + str(k))
            except:
                continue
        f.close()

from_parts_html_get_seq()