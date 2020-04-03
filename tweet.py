from twitterscraper import query_tweets
from twitterscraper.query import query_user_info

import requests
from bs4 import BeautifulSoup

from datetime import date

def scrape(url):
    urlData = requests.get(url)
    return urlData.text

if __name__ == "__main__":
  
    url3himanta = "https://twitter.com/himantabiswa"
    html = scrape(url3himanta)
    soup = BeautifulSoup(html, "html.parser")
    tweets = [p.text for p in soup.findAll('p', class_='tweet-text')]

    for i in range(10):
        print("\n")
        print(tweets[i] )

    today = date.today()
    end = date.today()
    limit = 100
    userx = "Brandonwoelfel"
    #tweets = query_tweets( userx, begindate = today, enddate = end, limit = 100)
    #twitter_user_data = {}
    #twitter_user_data["num_tweets"] = user_info.tweets
    #print(tweets)

