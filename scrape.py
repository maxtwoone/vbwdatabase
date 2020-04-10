import csv
import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup

episodes = []


def getLinks(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features="html.parser")
    # get the title of the episode
    title = soup.h1.get_text().strip()

    # get a list of all a tags
    aTags = soup.main.section.find_all('a')

    # loop through a tags and for each, add the href text and the link text to a dictionary, then add the dictionary to a list
    links = []
    for tag in aTags:
        link = {
            "linkText" : tag.getText().replace('\n', ' ').replace('\xa0', ''),
            "linkURL" : tag.get("href")
        }
        links.append(link)

    episode = {
        "episode_number": i,
        "title": title,
        "links": links
    }
    episodes.append(episode)



for i in range(1,186):
    url = "http://www.verybadwizards.com/" + str(i)
    getLinks(url);
    i += 1


with open('output.txt', 'wt') as out:
    pprint(episodes, stream=out)