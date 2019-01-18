import sys # system
from bs4 import BeautifulSoup # html parse (解析程式碼)
import time # for delay
from selenium import webdriver # web simulator (網頁模擬器)
from selenium.webdriver.chrome.options import Options # web simulator (網頁模擬器)
import os # operation system

options = Options()
options.add_argument('--headless') # hidden browser (無標頭)
options.add_argument('--disable-gpu') 
driver = webdriver.Chrome(os.getcwd() + "/python/Crawler/chromedriver") # assign chromedriver
# driver2 = webdriver.Chrome(os.getcwd() + "/python/Crawler/chromedriver")

for i in range (1, 2):
    # time.sleep(1) # delay
    driver.get("https://www.basketball-reference.com/boxscores/") # designate website
    sourceCode = BeautifulSoup (driver.page_source, "html.parser") # initialize page source
    headerScores = sourceCode.find_all(id = "header_scores")
    # print(headerScores)
    for headerScore in headerScores:
        sourceCode2 = BeautifulSoup (str(headerScore), "html.parser")
        gameSummaries = sourceCode2.find_all("div", "game_summary")
        # print(gameSummaries)
        for gameSummary in gameSummaries:
            sourceCode3 = BeautifulSoup (str(gameSummary), "html.parser")
            boxes = sourceCode3.find_all("td", "gamelink")
            # print(boxes)
            for box in boxes:
                sourceCode4 = BeautifulSoup (str(box), "html.parser")
                link = sourceCode4.find_all("a")[0]['href']
                print(link)
                driver2.get("https://www.basketball-reference.com" + link) # designate website
driver.close() # end browser
