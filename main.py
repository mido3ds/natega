#!/usr/bin/env python3
from bs4 import BeautifulSoup
from urllib.request import urlopen


def get_page():
    return urlopen(url='http://www.results.eng.cu.edu.eg/').read()


def is_marked(page):
    return BeautifulSoup(page, 'html.parser').find(id='td44').find('a') is not None

natega_appeared = is_marked(get_page())

##########################################################################
