from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time


chromedriver_path = '/Users/tetyanahvozda/Downloads/chromedriver-mac-arm64/chromedriver'

s = Service(chromedriver_path)
driver = webdriver.Chrome(service=s)

# Step 1: Access the webpage
url = 'https://coinmarketcap.com/'
driver.get(url)

time.sleep(5)

soup = BeautifulSoup(driver.page_source, 'html.parser')

driver.quit()

# Step 2: Extract tables and information using BeautifulSoup:
table = soup.find('table')

data = []
rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    if cols:
        data.append(cols)

df = pd.DataFrame(data, columns=[
    '', 'Rank', 'Name', 'Price', '1h %', '24h %', '7d %', 'Market Cap', 'Volume(24h)', 'Circulating Supply',
    'Last 7 Days'
])

df.dropna(inplace=True)

# Step 5: Save the data in the form of a CSV file:
df.to_csv('scraped_data.csv', index=False)

print("Data successfully scraped and saved to 'scraped_data.csv'")
