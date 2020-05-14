import requests
from numpy import *
from bs4 import BeautifulSoup
import csv

URLlist=['https://www.livemint.com/news/india/covid-19-vaccine-might-not-be-enough-to-end-the-corona-pandemic-11589349063107.html',
'https://www.bbc.com/news/world',
'https://www.ndtv.com/',
'https://timesofindia.indiatimes.com/life-style/health-fitness/health-news/coronavirus-vaccine-latest-news-covid-19-vaccine-status-update-these-6-coronavirus-vaccines-are-leading-the-race/photostory/75670744.cms',
'https://www.indiatoday.in/news.html',
'https://www.npr.org/sections/goatsandsoda/2020/05/12/852886535/when-can-we-expect-a-coronavirus-vaccine',
'https://indianexpress.com/',
'https://www.mayoclinic.org/diseases-conditions/coronavirus/in-depth/coronavirus-vaccine/art-20484859',
'https://economictimes.indiatimes.com/',
'https://www.telegraph.co.uk/global-health/science-and-disease/covid-19-coronavirus-vaccine-trials-latest-uk/']

n=len(URLlist)
#i=0
vaccinepara=[]
nonvaccinepara=[]

'''for iin list:
    print(i)
'''

for url in URLlist:
  print(url)
  r=requests.get(url)
  print(r.status_code)
  soup=BeautifulSoup(r.content,'html5lib')
  table=soup.findAll('p')
  #print(table)
  paratext=str(table)
  #table.prettify()
  
  #str="Messi is the best soccer player">>>"soccer" in str  will return true or false
  
  if "vaccine" in paratext:
      nonvaccinepara.append(paratext)
  else:
      vaccinepara.append(paratext)

  '''stri='vaccine'
  n=paratext.find(stri,0,len(paratext))
  print(n)
  if n==-1:
    nonvaccinepara.append(paratext)
  else:
    vaccinepara.append(paratext)'''

filename='vaccinefound.txt'
with open(filename,'wt') as f:
    #w=csv.DictWriter(f,['Paragraph'])
    #w.writeheader()
    for para in vaccinepara:
        #print(para)
        #w.writerow(para)
        f.write(para)

filename='vaccinenotfound.txt'
with open(filename,'wt') as f:
    #w=csv.DictWriter(f,['Paragraph'])
    #w.writeheader()
    for para in nonvaccinepara:
        f.write(para)