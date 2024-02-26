import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.fis-ski.com/DB/freestyle-freeski/freeski/trick-list.html"
data = requests.get(url)

soup = BeautifulSoup(data.text, "html.parser")
table = soup.find("div", class_="tbody")

trick_id = table.find_all("div", class_="g-lg-8 g-md-8 g-sm-8 g-xs-24 justify-left")
trick_name = table.find_all("div", class_="g-lg-12 g-md-12 g-sm-12 g-xs-24 justify-left")
event = table.find_all("div", class_="g-lg-3 g-md-3 g-sm-3 justify-left hidden-xs")
desc = table.find_all("div", class_="g-lg g-md g-sm g-xs justify-left")

col1 = [i.text.strip() for i in trick_id]
col2 = [i.text.strip() for i in trick_name]
col3 = [i.text.strip() for i in event]
col4 = [i.text.strip() for i in desc]

data = {
    'Trick ID': col1,
    'Trick Name': col2,
    'Event': col3,
    'Description': col4
}

df = pd.DataFrame(data)

df.to_excel('scraped_data.xlsx', index=False)
