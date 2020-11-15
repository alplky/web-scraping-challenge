#set up and dependencies
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd 

#set up driver
options = Options()
options.headless = True
driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=options)

# NASA Mars News

# establish url and scrape web page
url = "https://mars.nasa.gov/news/"

driver.get(url)
driver.implicitly_wait(10)
html = driver.page_source

# pass to bs4 for parsing
soup = BeautifulSoup(html, "html.parser")

# extract news titles
news_titles = soup.find_all("li", class_="slide")

# extract latest news title and assign to variable
latest = news_titles[0].find("div", class_="content_title")
news_title = latest.text.strip()

# extract latest news paragraph text and assign to variable
p_text = news_titles[0].find("div", class_="article_teaser_body")
news_p = p_text.text.strip()

print("NASA Mars News")
print("-" * 30)
print(news_title)
print(news_p)

# JPL Mars Space Images - Featured Image

# establish url and go seach Mars images
base_url = "https://www.jpl.nasa.gov"
url = base_url + "/spaceimages/?search=&category=Mars"

driver.get(url)
driver.implicitly_wait(10)

# navigate web page to find large image url
driver.find_element_by_link_text("FULL IMAGE").click()
driver.find_element_by_partial_link_text("more info").click()

# scrape page
driver.implicitly_wait(10)
html = driver.page_source

# pass to bs4 for parsing
soup = BeautifulSoup(html, "html.parser")

main_img = soup.find_all("img", class_="main_image")

# extract out src attribute
src = ""

for image in main_img:
    src = image["src"]

# combine base url with src string and assign to variable
featured_image_url = base_url + src

print("Featured Mars Image URL")
print("-" * 30)
print(featured_image_url)

# Mars Facts

# establish url and scrape web page
url = "https://space-facts.com/mars/"

driver.get(url)
driver.implicitly_wait(10)
html = driver.page_source

# pass to bs4 for parsing
soup = BeautifulSoup(html, "html.parser")

tables = soup.find_all("table")

# index for info only on the mars facts table
facts_table = tables[0]

# extract data from the facts table
table_data = [[cell.text for cell in row.find_all(["th", "td"])] for row in facts_table.find_all("tr")]

# convert to dataframe
df = pd.DataFrame(table_data)

#save html of table to a string
mars_table = df.to_html(index=False)

print("Mars Facts Table")
print("-" * 30)
print(df)

# Mars Hemispheres
