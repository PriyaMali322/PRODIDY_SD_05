import requests
from bs4 import BeautifulSoup
import csv
import time

# Example URL with a real product search query
url = "https://www.amazon.com/s?k=laptops"

# Headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send a GET request to the website
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error for bad status codes
except requests.HTTPError as e:
    print(f"Error fetching the URL: {e}")
    response = None

# Check if response is valid
if response and response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Continue with the parsing logic...
    # List to store extracted product data
    products = []
    
    # Find all product listings
    for product in soup.find_all('div', class_='s-result-item'):
        # Extract product name
        name = product.find('span', class_='a-size-medium a-color-base a-text-normal')
        name = name.text if name else "N/A"
        
        # Extract product price
        price = product.find('span', class_='a-price-whole')
        price = price.text if price else "N/A"
        
        # Extract product rating
        rating = product.find('span', class_='a-icon-alt')
        rating = rating.text if rating else "N/A"
        
        # Append the data to the list
        products.append([name, price, rating])
    
    # Define the CSV file path
    csv_file = 'products.csv'
    
    # Write data to CSV file
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(["Product Name", "Price", "Rating"])
        # Write product data
        writer.writerows(products)

    print(f"Data successfully saved to {csv_file}")
else:
    print("Failed to retrieve or parse the page.")
