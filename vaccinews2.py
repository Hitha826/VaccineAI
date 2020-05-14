import requests
from numpy import *
from bs4 import BeautifulSoup
import csv

URLlist=['https://www.livemint.com/news/india/covid-19-vaccine-might-not-be-enough-to-end-the-corona-pandemic-11589349063107.html',
'https://timesofindia.indiatimes.com/life-style/health-fitness/health-news/coronavirus-vaccine-latest-news-covid-19-vaccine-status-update-these-6-coronavirus-vaccines-are-leading-the-race/photostory/75670744.cms',
'https://www.npr.org/sections/goatsandsoda/2020/05/12/852886535/when-can-we-expect-a-coronavirus-vaccine',
'https://www.mayoclinic.org/diseases-conditions/coronavirus/in-depth/coronavirus-vaccine/art-20484859',
'https://www.telegraph.co.uk/global-health/science-and-disease/covid-19-coronavirus-vaccine-trials-latest-uk/']

r=requests.get(URLlist[0])

soup = BeautifulSoup(r.content, 'html5lib') 
print(soup.prettify()) 

