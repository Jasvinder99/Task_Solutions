# Task 5

# Use the BeautifulSoup and requests Python packages to print out a list of all the news titles on the https://news.ycombinator.com/.
#.......................................................................................................................

import bs4
import requests

#----------------------------------------------------------------------------------

get_request = requests.get("https://news.ycombinator.com/")
var_soup = bs4.BeautifulSoup(get_request.text, 'lxml')
news_title = var_soup.select(".storylink")      #storylink is class from a tag to get all news titles

for i in var_soup.select('.storylink'):
    print(i.text)
