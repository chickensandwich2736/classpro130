#Class 127

import pandas as pd
from bs4 import BeautifulSoup as bs
import requests 
import csv


name = []
distance = []
mass = []
radius = []

stars_list_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

page = requests.get(stars_list_url)
print(page)

soup = bs(page.text,'html.parser')

star_table = soup.find('table')

star_list = []
table_rows = star_table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    star_list.append(row)

for i in range(1,len(star_list)):
    name.append(star_list[i][1])
    distance.append(star_list[i][3])
    mass.append(star_list[i][5])
    radius.append(star_list[i][7])

df = pd.DataFrame(list(zip(name, distance, mass, radius)), columns=["Name", "Distance", "Mass", "Radius"])
print(df)

df.to_csv("brightstars.csv")





    
