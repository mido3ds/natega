#!/usr/bin/env python3
from bs4 import BeautifulSoup
from urllib.request import urlopen
from random import randrange, random
import webbrowser


def get_page():  # -> String
    return urlopen(url='http://www.results.eng.cu.edu.eg/').read()


def is_marked(page):  # String -> Bool
    return BeautifulSoup(page, 'html.parser').find(id='td45').find('a') is not None

natega_appeared = is_marked(get_page())

##########################################################################


def get_rand_location():  # -> Float, Float
    latitude = randrange(-90, 90) + random()
    longitude = randrange(-180, 180) + random()

    return longitude, latitude


def get_google_maps_link(lat, long, zoom=8):  # Int, Int, Int -> String
    return 'https://www.google.com/maps/preview/@{latitude},{longitude},{zoomlevel}z'.format(
        latitude=lat,
        longitude=long,
        zoomlevel=zoom
    )
##########################################################################

if natega_appeared:
    long, lat = get_rand_location()
    link = get_google_maps_link(lat, long, 8)

    print('Appeared')
    webbrowser.open(link)
else:
    print('Not Yet')
