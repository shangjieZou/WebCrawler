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


def get_html_main():
        # for first time use
    def get_page_structure(url):
        Target_page = get_url_txt(url)
        Target_page_soup = BeautifulSoup(Target_page, "html.parser")
        return Target_page_soup

    def get_html_list_for_parts(html):
        BioBrick_pattern = r"<TR><TD><A class='noul_link part_link' href='(.+)'>BBa_"
        BioBrick_html = str(re.findall(BioBrick_pattern, html))
        return BioBrick_html


    html = get_url_txt("http://parts.igem.org/Promoters/Catalog/Ecoli/Constitutive")
    f = open('Constitutive.txt', 'w')
    f.write(get_html_list_for_parts(html))
    f.close()
    print("finished")


def from_parts_html_get_seq():
    f_positive = open('Positive-promoter-html.txt','r')
    content_positive = f_positive.read()
    Positive_promoters_html = content_positive.split(',')
    f_positive.close()
    f_constitutive = open('Constitutive promoter html.txt', 'r')
    content_constitutive = f_constitutive.read()
    Constitutive_promoters_html = content_constitutive.split(',')
    f_constitutive.close()
    f_Negative = open('Repressible-promoter-html.txt', 'r')
    content_negative = f_Negative.read()
    Negative_promoters_html = content_negative.split(',')
    f_Negative.close()

    def get_seq_from_html(html):
        part_name_pattern = r"var PrimaryPartName = \'(.+)\'; var PrimaryPartID"
        part_seq_pattern = r"var sequence = new String((.+));\s*var seqFeatures"
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
        f = open('Positive_seqs_with_ref.txt', 'w')
        for i in range(len(Positive_promoters_html)):
            try:
                url = eval(Positive_promoters_html[i])
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
        f = open('Constitutive_seqs_with_ref.txt', 'w')
        for i in range(len(Constitutive_promoters_html)):
            try:
                url = eval(Constitutive_promoters_html[i])
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
        f = open('Negative_seqs_with_ref.txt', 'w')
        for i in range(len(Negative_promoters_html)):
            try:
                url = eval(Negative_promoters_html[i])
                print(url)
                html = get_url_txt(url)
                f.write(get_seq_from_html(html))
                k += 1
                print(get_name(html) + "finished" + str(k))
            except:
                continue
        f.close()
"""""
    url = eval(Positive_promoters_html[6])
    print(url)
    html = get_url_txt(url)
    print(html)
    part_name_pattern = r"var PrimaryPartName = \'(.+)\'; var PrimaryPartID"
    part_seq_pattern = r"var sequence = new String((.+));\s*var seqFeatures"
    part_name = str(re.findall(part_name_pattern, html))
    part_seq_list = list(set(list(re.findall(part_seq_pattern, html)[0])))
    part_seq = eval(part_seq_list[0])
    print(part_name)
    print(part_seq)
"""""

from_parts_html_get_seq()
