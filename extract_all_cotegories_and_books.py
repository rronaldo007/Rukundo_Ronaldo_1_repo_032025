import requests
from bs4 import BeautifulSoup
import os
import csv
import time
from extract_books_by_category import extract_category_books

def extract_all_categories(base_url):
    """
    Extraire toutes les catégories et leurs livres
    """
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    category_container = soup.find('div', class_='side_categories')
    category_list = category_container.find('ul').find('ul').find_all('li')
    total_categories = len(category_list)

    for category_item in category_list:
        category_name = category_item.a.text.strip()
        category_url = base_url + category_item.a['href']

        try:
            extract_category_books(category_url)
                
        except Exception as e:
            print(f"Erreur lors de l'extraction de la catégorie {category_name}: {str(e)}")
    
    print("\nExtraction de toutes les catégories terminée!")