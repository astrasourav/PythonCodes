from bs4 import BeautifulSoup as soup
import requests as req
import pandas as pd


sauce = req.get('https://news.ycombinator.com/')


url = soup(sauce.content, 'lxml')



table = url.find_all(class_='athing')


## This line is a line comprehenion##
data = [i.find('a', class_='storylink').get_text() for i in table]
print(data)

##Created a csv file usig panda in python
repo = pd.DataFrame(
    {
        'list': data
    })

print(repo)

repo.to_csv('Hacke news.csv')
