import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Access the webpage
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Extract tables and information using BeautifulSoup:
tables = soup.find_all('table')

# Step 3: Convert it into a structured format using pandas:
data = []

for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append(cols)

df = pd.DataFrame(data)

# Step 4: Clean the data using pandas and NumPy:
df.dropna(inplace=True)

# Step 5: Save the data in the form of a CSV file:
df.to_csv('scraped_data.csv', index=False)

print("Data successfully scraped and saved to 'scraped_data.csv'")
