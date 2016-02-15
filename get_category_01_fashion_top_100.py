# -*- coding: UTF-8 -*-

import urllib2
from bs4 import BeautifulSoup

# import urllib.request
import urllib
import sys 
import re

# ------ open the top 100 items with 5 different files
# html_top20 = urllib.urlopen("
# ...

html_top20 = urllib.urlopen("http://shopping.yahoo.co.jp/category/2517/ranking/?sc_i=shp_pc_ranking-top_mdSideListCategory_20")
html_top40 = urllib.urlopen("http://shopping.yahoo.co.jp/category/2517/ranking/cr_20/?sc_i=shp_pc_ranking-cate_mdRankListPager_21-40#list")
html_top60 = urllib.urlopen("http://shopping.yahoo.co.jp/category/2517/ranking/cr_40/?sc_i=shp_pc_ranking-cate_mdRankListPager_41-60#list")
html_top80 = urllib.urlopen("http://shopping.yahoo.co.jp/category/2517/ranking/cr_60/?sc_i=shp_pc_ranking-cate_mdRankListPager_61-80#list")
html_top100 = urllib.urlopen("http://shopping.yahoo.co.jp/category/2517/ranking/cr_80/?sc_i=shp_pc_ranking-cate_mdRankListPager_81-100#list")

f1 = open("yahoo_rankings_cat_01_html_top20.txt", "w")
f2 = open("yahoo_rankings_cat_01_html_top40.txt", "w")
f3 = open("yahoo_rankings_cat_01_html_top60.txt", "w")
f4 = open("yahoo_rankings_cat_01_html_top80.txt", "w")
f5 = open("yahoo_rankings_cat_01_html_top100.txt", "w")

# ------ [1-5]

soup = BeautifulSoup(html_top20)
ol = soup.find('ol', attrs={'class': 'elLists'})
lis = ol.findAll('li')

for li in lis:
    h3s = li.find('p', attrs={'class': 'elPhoto'})
    f1.write(str(h3s))


soup = BeautifulSoup(html_top40)
ol = soup.find('ol', attrs={'class': 'elLists'})
lis = ol.findAll('li')

for li in lis:
    h3s = li.find('p', attrs={'class': 'elPhoto'})
    f2.write(str(h3s))

soup = BeautifulSoup(html_top60)
ol = soup.find('ol', attrs={'class': 'elLists'})
lis = ol.findAll('li')

for li in lis:
    h3s = li.find('p', attrs={'class': 'elPhoto'})
    f3.write(str(h3s))


soup = BeautifulSoup(html_top80)
ol = soup.find('ol', attrs={'class': 'elLists'})
lis = ol.findAll('li')

for li in lis:
    h3s = li.find('p', attrs={'class': 'elPhoto'})
    f4.write(str(h3s))


soup = BeautifulSoup(html_top100)
ol = soup.find('ol', attrs={'class': 'elLists'})
lis = ol.findAll('li')

for li in lis:
    h3s = li.find('p', attrs={'class': 'elPhoto'})
    f5.write(str(h3s))

# close files here ....

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()

# -- --

f1 = open("yahoo_rankings_cat_01_top_20_filtered.txt", "w")
f2 = open("yahoo_rankings_cat_01_top_40_filtered.txt", "w")
f3 = open("yahoo_rankings_cat_01_top_60_filtered.txt", "w")
f4 = open("yahoo_rankings_cat_01_top_80_filtered.txt", "w")
f5 = open("yahoo_rankings_cat_01_top_100_filtered.txt", "w")

with open('yahoo_rankings_cat_01_html_top20.txt', 'rU') as f:
    for line in f:
        urls = re.findall(r'src=[\'"]?([^\'" >]+)', line)
        f1.write(str(urls))
        f1.write("\n")

with open('yahoo_rankings_cat_01_html_top40.txt', 'rU') as f:
    for line in f:
        urls = re.findall(r'src=[\'"]?([^\'" >]+)', line)
        f2.write(str(urls))
        f2.write("\n")

with open('yahoo_rankings_cat_01_html_top60.txt', 'rU') as f:
    for line in f:
        urls = re.findall(r'src=[\'"]?([^\'" >]+)', line)
        f3.write(str(urls))
        f3.write("\n")

with open('yahoo_rankings_cat_01_html_top80.txt', 'rU') as f:
    for line in f:
        urls = re.findall(r'src=[\'"]?([^\'" >]+)', line)
        f4.write(str(urls))
        f4.write("\n")

with open('yahoo_rankings_cat_01_html_top100.txt', 'rU') as f:
    for line in f:
        urls = re.findall(r'src=[\'"]?([^\'" >]+)', line)
        f5.write(str(urls))
        f5.write("\n")

# ----  [close the files ]

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()


# ---- [処理する]
# ①　change from small to Large size
# ②　remove the empty links []
# ③　remove the end of line
# ④　make downloadable via wget

# -- > top 20 items

with open("yahoo_rankings_cat_01_top_20_size.txt", "wt") as fout:
    with open("yahoo_rankings_cat_01_top_20_filtered.txt", "rt") as fin:
        for line in fin:
            fout.write(line.replace('i/e/', 'i/l/'))

with open("yahoo_rankings_cat_01_top_20_brackets.txt", "wt") as fout:
    with open("yahoo_rankings_cat_01_top_20_size.txt", "rt") as fin:
        for line in fin:
            fout.write(line.replace('[]', ''))

with open("yahoo_rankings_cat_01_top_20_prefix.txt", "wt") as fout:
    with open("yahoo_rankings_cat_01_top_20_brackets.txt", "rt") as fin:
        for line in fin:
            fout.write(line.replace('[\'' ,'wget '))

with open("yahoo_rankings_cat_01_top_20_sufix.txt", "wt") as fout:
    with open("yahoo_rankings_cat_01_top_20_prefix.txt", "rt") as fin:
        for line in fin:
            fout.write(line.replace('\']' ,' &'))

# -- > top 40 items

with open("yahoo_rankings_cat_01_top_40_size.txt", "wt") as fout:
    with open("yahoo_rankings_cat_01_top_40_filtered.txt", "rt") as fin:
        for line in fin:
            fout.write(line.replace('i/e/', 'i/l/'))

with open("yahoo_rankings_cat_01_top_40_brackets.txt", "wt") as fout:
    with open("yahoo_rankings_cat_01_top_40_size.txt", "rt") as fin:
        for line in fin:
            fout.write(line.replace('[]', ''))

with open("yahoo_rankings_cat_01_top_40_prefix.txt", "wt") as fout:
    with open("yahoo_rankings_cat_01_top_40_brackets.txt", "rt") as fin:
        for line in fin:
            fout.write(line.replace('[\'' ,'wget '))

with open("yahoo_rankings_cat_01_top_40_sufix.txt", "wt") as fout:
    with open("yahoo_rankings_cat_01_top_40_prefix.txt", "rt") as fin:
        for line in fin:
            fout.write(line.replace('\']' ,' &'))

# -- > top 60 items

with open("yahoo_rankings_cat_01_top_60_size.txt", "wt") as fout:
    with open("yahoo_rankings_cat_01_top_60_filtered.txt", "rt") as fin:
        for line in fin:
            fout.write(line.replace('i/e/', 'i/l/'))

with open("yahoo_rankings_cat_01_top_60_brackets.txt", "wt") as fout:
    with open("yahoo_rankings_cat_01_top_60_size.txt", "rt") as fin:
        for line in fin:
            fout.write(line.replace('[]', ''))

with open("yahoo_rankings_cat_01_top_60_prefix.txt", "wt") as fout:
    with open("yahoo_rankings_cat_01_top_60_brackets.txt", "rt") as fin:
        for line in fin:
            fout.write(line.replace('[\'' ,'wget '))

with open("yahoo_rankings_cat_01_top_60_sufix.txt", "wt") as fout:
    with open("yahoo_rankings_cat_01_top_60_prefix.txt", "rt") as fin:
        for line in fin:
            fout.write(line.replace('\']' ,' &'))

# -- > top 80 items

with open("yahoo_rankings_cat_01_top_80_size.txt", "wt") as fout:
    with open("yahoo_rankings_cat_01_top_80_filtered.txt", "rt") as fin:
        for line in fin:
            fout.write(line.replace('i/e/', 'i/l/'))

with open("yahoo_rankings_cat_01_top_80_brackets.txt", "wt") as fout:
    with open("yahoo_rankings_cat_01_top_80_size.txt", "rt") as fin:
        for line in fin:
            fout.write(line.replace('[]', ''))

with open("yahoo_rankings_cat_01_top_80_prefix.txt", "wt") as fout:
    with open("yahoo_rankings_cat_01_top_80_brackets.txt", "rt") as fin:
        for line in fin:
            fout.write(line.replace('[\'' ,'wget '))

with open("yahoo_rankings_cat_01_top_80_sufix.txt", "wt") as fout:
    with open("yahoo_rankings_cat_01_top_80_prefix.txt", "rt") as fin:
        for line in fin:
            fout.write(line.replace('\']' ,' &'))

# -- > top 100 items

with open("yahoo_rankings_cat_01_top_100_size.txt", "wt") as fout:
   with open("yahoo_rankings_cat_01_top_100_filtered.txt", "rt") as fin:
       for line in fin:
           fout.write(line.replace('i/e/', 'i/l/'))

with open("yahoo_rankings_cat_01_top_100_brackets.txt", "wt") as fout:
    with open("yahoo_rankings_cat_01_top_100_size.txt", "rt") as fin:
        for line in fin:
            fout.write(line.replace('[]', ''))

with open("yahoo_rankings_cat_01_top_100_prefix.txt", "wt") as fout:
    with open("yahoo_rankings_cat_01_top_100_brackets.txt", "rt") as fin:
        for line in fin:
            fout.write(line.replace('[\'' ,'wget '))

with open("yahoo_rankings_cat_01_top_100_sufix.txt", "wt") as fout:
    with open("yahoo_rankings_cat_01_top_100_prefix.txt", "rt") as fin:
        for line in fin:
            fout.write(line.replace('\']' ,' &'))

