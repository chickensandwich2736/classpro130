import pandas as pd
from bs4 import BeautifulSoup as bs
import requests 
import csv


brown_dwarfs_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

bd_name = []
bd_distance = []
bd_mass = []
bd_radius = []

bd_data = []

page = requests.get(brown_dwarfs_url)
print(page)
soup = bs(page.text, 'html.parser')
star_table = soup.find_all("table")
table_rows = star_table[7].find_all("tr")

brown_dwarfs_list = []

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    brown_dwarfs_list.append(row)

for i in range(1,len(brown_dwarfs_list)):
    bd_name.append(brown_dwarfs_list[i][0])
    bd_distance.append(brown_dwarfs_list[i][5])
    bd_mass.append(brown_dwarfs_list[i][8])
    bd_radius.append(brown_dwarfs_list[i][9])

df = pd.DataFrame(list(zip(bd_name, bd_distance, bd_mass, bd_radius)), columns=["Name", "Distance", "Mass", "Radius"])
print(df)

df.to_csv("browndwarfs.csv")