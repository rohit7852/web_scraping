import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies?fbclid=IwAR2GrcMSrKuMf0G60S7O5qxsPQXCUKfTK0cjnCsQdDAUM43mt7Yt29GrX_k"
html = urlopen(url)
soup = BeautifulSoup(html,"html.parser" )
type(soup)

rows = soup.find('table',{'id':'constituents'}) 
#print(rows)
ty=rows.find_all("tr")

list_company=[]
list_stickers=[]
print(len(ty))
for i in range(1,506):
    zk=ty[i].find_all("td")
    for k in range(0,2):
        if k==0:
            a=str(zk[k])
            cleantext = BeautifulSoup(a, "lxml").get_text()
            list_stickers.append(cleantext)
        else: 
            a=str(zk[k])
            cleantext = BeautifulSoup(a, "lxml").get_text()
            list_company.append(cleantext)           
#print(list_rows)    
#str_cells = str(list_rows)
#cleantext = BeautifulSoup(str_cells, "lxml").get_text()
#print(cleantext[1])
df1 = pd.DataFrame(list_company,columns=['Company_Name'])
#print(df1)
df2= pd.DataFrame(list_stickers,columns=['Stickers'])

df3=df2.join(df1)
print(df3)
#print(df1)
#df3 = {'sticker':'list_stickers','company' :'list_company'}

#df4 = pd.DataFrame(df3,columns=['sticker','company'])
#print(df4)
df3.to_csv('out.csv')
