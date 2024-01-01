
from bs4 import BeautifulSoup
import csv

# Define the URL of the e-commerce website to scrape
url = "https://www.amazon.com/best-sellers-electronics/zgbs/electronics/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the product information on the page (modify the selectors according to the website's structure)
    products = soup.find_all("div", class_="zg_itemImmersion")
    
    # Create a CSV file to store the data
    with open('product_data.csv', mode='w', newline='') as csv_file:
        fieldnames = ['Name', 'Price', 'Rating']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        # Write the header row to the CSV file
        writer.writeheader()
        
        # Extract and store product information
        for product in products:
            name = product.find("div", class_="p13n-sc-truncate").text.strip()
            price = product.find("span", class_="p13n-sc-price").text.strip()
            rating = product.find("span", class_="a-icon-alt").text.strip()
            
            # Write the product information to the CSV file
            writer.writerow({'Name': name, 'Price': price, 'Rating': rating})
    
    print("Product data has been successfully scraped and saved to product_data.csv.")
else:
    print("Failed to retrieve the webpage.")

