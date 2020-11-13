#set up and dependencies
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#set up driver
options = Options()
options.headless = True
driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=options)

# establish url and scrape web page
url = "https://mars.nasa.gov/news/"

driver.get(url)
driver.implicitly_wait(3)
html = driver.page_source
driver.close()

# pass to bs4 for parsing
soup = BeautifulSoup(html, "html.parser")

# extract news titles
news_titles = soup.find_all("li", class_="slide")

# extract latest news title and assign to variable
latest = news_titles[0].find("div", class_="content_title")
news_title = latest.text.strip()

print(news_title)



