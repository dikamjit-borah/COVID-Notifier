import requests
from bs4 import BeautifulSoup

def scrape(url):
    urlData = requests.get(url)
    return urlData.text

if __name__ == "__main__":
    url1stats = "https://www.mohfw.gov.in/"
    
    html = scrape(url1stats)
    soup = BeautifulSoup(html, "html.parser")
    #print(soup.prettify())
    dashboard = (soup.find_all('section', attrs={'id' : 'site-dashboard'}))
    strong = []
    for element in dashboard:
        h2 = (element.find_all('h2'))
        for d in h2:
            date = d.find_all('span')
        for d in date:
            date = (d.text).upper()
        strongs = (element.find_all('strong'))
        for s in strongs:
            strong.append(s.text)
        
        active = strong[0]
        cured = strong[1]
        deaths = strong[2]

    print(str(date))
    print("The number of ACTIVE cases are   :   " + str(active))
    print("The number of CURED cases are    :   " + str(cured))
    print("The number of DEATH cases are    :   " + str(deaths))
   

   
