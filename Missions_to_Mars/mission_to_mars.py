#set up and dependencies
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#set up driver
options = Options()
options.headless = True
driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=options)

# NASA Mars News

# establish url and scrape web page
url = "https://mars.nasa.gov/news/"

driver.get(url)
driver.implicitly_wait(4)
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

print(news_title)
print(news_p)


# JPL Mars Space Images - Featured Image

# establish url and scrape web page
base_url = "https://www.jpl.nasa.gov/spaceimages/"
url = base_url + "?search=&category=Mars"

driver.get(url)

link = driver.find_element_by_link_text("FULL IMAGE")
link.click()

try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "more info"))
    )
    element.click()
except:
    driver.quit()

# driver.implicitly_wait(4)
# html = driver.page_source
# driver.close()

# soup = BeautifulSoup(html, "html.parser")

# print(soup.head.prettify())


