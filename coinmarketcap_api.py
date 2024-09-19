import requests
import pandas as pd

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'EUR'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '',
}

response = requests.get(url, headers=headers, params=parameters).json()

data = response['data']
df = pd.json_normalize(data)

df.to_csv('scraped_data.csv', index=False)

print("Data successfully scraped and saved to 'scraped_data.csv'")