from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

url = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'

browser = webdriver.Chrome(executable_path=r"C:\Users\Sruthi Alagan\Desktop\whitehat\class 127 - WEB SCRAPING\chromedriver.exe")
browser.get(url)

time.sleep(10)

def scrape():
    headers = ['NAME',	'LIGHT-YEARS FROM EARTH',	'PLANET MASS',	'STELLAR MAGNITUDE',	'DISCOVERY DATE']
    planetdata = []

    for i in range(0,203):
        soup = BeautifulSoup(browser.page_source, 'html.parser')

        for ul_tag in soup.find_all('ul', attrs = {'class', 'exoplanet'}):
            li_tag = ul_tag.find_all('li')
            templist = []
            for index, list_tag in enumerate(li_tag):
                if index==0:
                    templist.append(list_tag.find_all('a')[0].contents[0])
                else:
                    try:
                        templist.append(list_tag.contents[0])
                    except:
                        templist.append('')
        
            planetdata.append(templist)

        browser.find_element('//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click()

    with open('planets.csv', 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planetdata)


scrape()
