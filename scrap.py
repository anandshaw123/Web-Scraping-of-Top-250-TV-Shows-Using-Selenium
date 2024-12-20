from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time
import pandas as pd


TV_S_name = []
TV_Shows_Ratings=[]
TV_Shows_Episodes=[]
Review_Count_Numbers=[]
release_years = []


def web_Scraping_of_Top_TV_Shows(url, chrome_driver_path = "chromedriver-win64//chromedriver.exe"):

    service = Service(chrome_driver_path)

    driver = webdriver.Chrome(service=service)
    driver.get(url)

    # Hold the page open for 5 seconds for better Extracting.
    time.sleep(11)





## Extracting TV Shows {Names}::
    time.sleep(10)
    elements = driver.find_elements(By.CSS_SELECTOR, "h3.ipc-title__text")

    new_name = [element.text.split('. ')[1] for element in elements if '. ' in element.text]
    for namess in new_name:
        TV_S_name.append(namess)




## Extracting TV Shows {Ratings}::
    time.sleep(10)
    rating_elements = driver.find_elements(By.CSS_SELECTOR, "span.ipc-rating-star--rating")
    ratings = [element.text for element in rating_elements]
    for r in ratings:
        TV_Shows_Ratings.append(r)




## Extracting TV Shows {Episodes}::
    time.sleep(10)
    elements1 = driver.find_elements(By.CSS_SELECTOR, "span.sc-300a8231-7.eaXxft.cli-title-metadata-item")
    episode_info = [elem.text for elem in elements1 if "eps" in elem.text]
    for info in episode_info:
        TV_Shows_Episodes.append(info)




## Extracting {Review Count Numbers}::
    time.sleep(10)
    elements2 = driver.find_elements(By.CSS_SELECTOR, "span.ipc-rating-star--voteCount")
    vote_counts = [element.text for element in elements2]
    for counteds in vote_counts:
     Review_Count_Numbers.append(counteds)





## Extracting the {Year Data}::
    time.sleep(10)
    elements3 = driver.find_elements(By.CSS_SELECTOR, "span.sc-300a8231-7.eaXxft.cli-title-metadata-item")
    year_ranges = [elem.text for elem in elements3 if '–' in elem.text and elem.text[:4].isdigit() or elem.text.isdigit()]
    for year_range in year_ranges:
        release_years.append(year_range)



    data = {
        "Shows Name":TV_S_name,
        "Release Year":release_years,
        "Episodes":TV_Shows_Episodes,
        "Rating":TV_Shows_Ratings,
        "Rating given by people":Review_Count_Numbers
    }
    ## Creating a DataFrame
    df = pd.DataFrame(data)
    
    ## Convert Extracting Data into CSV File
    df.to_csv("imdb_Top_250_TV_Shows.csv",index=False)
    print("Data Successfully saved Into 'imdb_Top_250_TV_Shows.csv'")

    driver.close()


web_Scraping_of_Top_TV_Shows('https://www.imdb.com/chart/toptv/')

