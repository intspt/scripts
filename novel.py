#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-



import urllib2
import bs4
import re


def main():
    base_url = 'http://www.piaotian.net/html/1/1705/'
    current_page_link = '764264.html'
    fout = open('tmp.txt', 'a')
    while True:
        pageHTML = urllib2.urlopen(base_url + current_page_link).read().decode('GBK', 'ignore')
        pageSoup = bs4.BeautifulSoup(pageHTML, 'lxml')
        pageSoup.find('h1').a.extract()
        print pageSoup.find('h1').text.strip().encode('utf-8')
        print >>fout, pageSoup.find('h1').text.strip().encode('utf-8')
        for child in pageSoup.body.children:
            if type(child) == bs4.element.NavigableString and child.strip() != '':
                print >>fout, child.strip('\n').encode('utf-8')

        current_page_link = pageSoup.find('div', class_='toplink').find('a', text=u'下一章').attrs['href']
        if not re.match(r'\d+\.html$', current_page_link):
            break

    fout.close()


if __name__ == '__main__':
    main()