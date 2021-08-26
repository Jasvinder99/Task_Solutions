# Task 5

# Use the BeautifulSoup and requests Python packages to print out a list of all the news titles on the https://news.ycombinator.com/.
#.......................................................................................................................

import bs4
import requests
from typing import Optional


#----------------------------------------------------------------------------------

get_request: Optional = requests.get("https://news.ycombinator.com/")
var_soup: Optional = bs4.BeautifulSoup(get_request.text, 'lxml')
#storylink is class from a tag to get all news titles
news_title: Optional[classmethod] = var_soup.select(".storylink")

for i in var_soup.select('.storylink'):
    print(i.text)
