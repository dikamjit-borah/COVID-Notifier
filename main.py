import requests
from bs4 import BeautifulSoup

def scrape(url):
    urlData = requests.get(url)
    return urlData.text

if __name__ == "__main__":
    url1who = "https://www.who.int/emergencies/diseases/novel-coronavirus-2019"
    url3gPlus1 = "https://www.guwahatiplus.com/daily-news?page=1"
    url3gPlus2 = "https://www.guwahatiplus.com/daily-news?page=2"
    url3himanta = ""
    html1 = scrape(url1who)
    '''

    soup = BeautifulSoup(html1, "html.parser")
    #print(soup.div['heading1'])
    #print(soup.find("div", {"class": "heading1"}).text)
    (soup.find_all("div", {"class": "heading1"}))
    print(soup.find(id="confirmedCases").string)'''

    titles = []
    links = []

    html3a = scrape(url3gPlus1)
    soup3a = BeautifulSoup(html3a, "html.parser")
    #p3a = soup3a.find_all('p', attrs={'class' : 'news-title line-clamp-3'})
    #print(p3a.text)
 
    divs = soup3a.find_all('div', {'class': 'news-desp'})
    for div in divs:
        children = div.findChildren("a" , recursive=False)
        for child in children:
            links.append("https://www.guwahatiplus.com" + child.get('href'))
            titles.append(child.text)
         
    html3b = scrape(url3gPlus2)
    soup3b = BeautifulSoup(html3b, "html.parser")

    divs = soup3a.find_all('div', {'class': 'news-desp'})
    for div in divs:
        children = div.findChildren("a" , recursive=False)
        for child in children:
            links.append("https://www.guwahatiplus.com" + child.get('href'))
            titles.append(child.text)
        
    
    print(links)
    print("\n")
    
    print(titles)
    
    