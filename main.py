#!/usr/bin/env python3
from bs4 import BeautifulSoup
from urllib.request import urlopen


def get_page():
    return urlopen(url='http://www.results.eng.cu.edu.eg/').read()


def parse_page(page):
    return BeautifulSoup(page, 'html.parser').find(id='td44')


def is_marked(soup):
    return soup.find('a') is not None

natega_appeared = is_marked(parse_page(get_page()))

##########################################################################
