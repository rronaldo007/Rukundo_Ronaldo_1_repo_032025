import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_cover_image(image_url, title):
    """
    Downloads and saves the cover image of a book
    """
    os.makedirs('images', exist_ok=True)
    clean_title = "".join(c if c.isalnum() or c in [' ', '.', '_'] else '_' for c in title)
    clean_title = clean_title.replace(' ', '_').lower()[:100]
    file_extension = image_url.split('.')[-1].lower()
    
    if '?' in file_extension:
        file_extension = file_extension.split('?')[0]
    file_path = f'images/{clean_title}.{file_extension}'
    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(8192):
                file.write(chunk)
        
        return file_path
    
    except Exception as e:
        print(f"Error downloading image {image_url}: {str(e)}")
        return None

def extract_all_book_images():
    """
    Extract and download images of all books from the website
    """
    base_url = "http://books.toscrape.com"
    os.makedirs('images', exist_ok=True)
    
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    category_container = soup.find('div', class_='side_categories')
    category_list = category_container.find('ul').find('ul').find_all('li')
    
    total_images = 0
    
    for category_item in category_list:
        category_url = urljoin(base_url, category_item.a['href'])
        current_url = category_url
        
        while True:
            response = requests.get(current_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            book_containers = soup.find_all('article', class_='product_pod')
            for book in book_containers:
                title = book.h3.a['title'] if book.h3.a.has_attr('title') else book.h3.a.text.strip()
                image_tag = book.find('img')
                image_src = image_tag['src']
                image_url = urljoin(base_url, image_src)
                download_cover_image(image_url, title)
                total_images += 1
            
            next_button = soup.find('li', class_='next')
            if next_button:
                next_page_relative = next_button.a['href']
                current_url = urljoin(current_url, next_page_relative)
            else:
                break
    