import requests
from bs4 import BeautifulSoup
import csv
import os

def extract_book_data(url):
    """Extraire les données d'un livre à partir de son URL"""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    title = soup.find('div', class_='product_main').h1.text
    
    category = soup.find('ul', class_='breadcrumb').find_all('li')[2].text.strip()
    
    product_table = soup.find('table', class_='table-striped')
    rows = product_table.find_all('tr')
    
    universal_product_code = rows[0].td.text
    price_excluding_tax = rows[2].td.text
    price_including_tax = rows[3].td.text
    number_available = rows[5].td.text.strip()
    
    product_description_element = soup.find('div', id='product_description')
    product_description = ""
    if product_description_element:
        product_description = product_description_element.find_next_sibling('p').text
    
    rating_class = soup.find('p', class_='star-rating')['class'][1]
    
    rating_mapping = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    review_rating = rating_mapping.get(rating_class, 0)
    
    image_relative_url = soup.find('div', class_='item active').img['src']
    image_url = 'http://books.toscrape.com/' + image_relative_url.replace('../', '')
    
    book_data = {
        'product_page_url': url,
        'universal_product_code': universal_product_code,
        'title': title,
        'price_including_tax': price_including_tax,
        'price_excluding_tax': price_excluding_tax,
        'number_available': number_available,
        'product_description': product_description,
        'category': category,
        'review_rating': review_rating,
        'image_url': image_url
    }
    
    return book_data

def save_to_csv(book_data, filename='data/book.csv'):
    """Sauvegarder les données d'un livre dans un fichier CSV"""
    os.makedirs('data', exist_ok=True)
    
    file_exists = os.path.isfile(filename)
    
    fieldnames = [
        'product_page_url',
        'universal_product_code',
        'title',
        'price_including_tax',
        'price_excluding_tax',
        'number_available',
        'product_description',
        'category',
        'review_rating',
        'image_url'
    ]
    
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(book_data)
    
    print(f"Données sauvegardées dans {filename}")
