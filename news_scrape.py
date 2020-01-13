# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:02:13 2020

@author: ShubhamBhatnagar

scraping
"""
#%%
# =============================================================================
# Imports
# =============================================================================
import requests
from bs4 import BeautifulSoup
import os

#%%
# =============================================================================
# Requests
# =============================================================================
bbc_url = r'https://www.bbc.co.uk/news'
cnn_url = r'https://edition.cnn.com/'
dailymail_url = r'https://www.dailymail.co.uk/home/index.html'
independent_url = r'https://www.independent.co.uk/'

bbc = requests.get(url = bbc_url)
cnn = requests.get(url = cnn_url)
dailymail = requests.get(url = dailymail_url)
#independent = requests.get(url = independent_url)


#%%
# =============================================================================
# Reading data
# =============================================================================
bbc_soup = BeautifulSoup(bbc.text, 'html.parser')
heading_bbc = bbc_soup.find('title')

cnn_soup = BeautifulSoup(cnn.text, 'html.parser')
heading_cnn = cnn_soup.find('title')

dailymail_soup = BeautifulSoup(dailymail.text, 'html.parser')
heading_dailymail = dailymail_soup.find('title')

# =============================================================================
# bbc_soup = BeautifulSoup(bbc.text, 'html.parser')
# tag = 'a' # (element name)
# attributes = {'class':'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold nw-o-link-split__anchor'}
# heading = bbc_soup.find(tag,attributes)
# =============================================================================

#%%
directory = os.path.dirname(os.path.realpath(__file__))
file_path = directory + "\\webscrape_output\\"
try: # make the webscrape output folder
    os.mkdir(file_path)
except: # if its already made, do nothing
    pass


filename = file_path + 'output.txt'
file = open(filename, 'w')

file.write('BBC Headline: \n')
file.write(heading_bbc.text + '\n')
file.write('CNN Headline: \n')
file.write(heading_cnn.text + '\n')
file.write('Dailymail Headline: \n')
file.write(heading_dailymail.text)
file.close()