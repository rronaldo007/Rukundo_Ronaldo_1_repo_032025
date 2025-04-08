import os
import csv
from bs4 import BeautifulSoup
import time
import requests
from urllib.parse import urljoin
from extract_book_from_url import extract_book_data


def extract_category_books(category_url):
    """Extraire les données de tous les livres d'une catégorie"""
    print(f"Extraction des livres de la catégorie: {category_url}")
    response = requests.get(category_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    category_name = soup.find('h1').text.strip()
    csv_filename = f"data/{category_name}.csv"
    book_count = 0
    current_url = category_url

    while True:
        print(f"Traitement de la page: {current_url}")
        response = requests.get(current_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        book_containers = soup.find_all('article', class_='product_pod')

        for book in book_containers:
            relative_url = book.h3.a['href']
            book_path = relative_url.split('/')[-2:]
            absolute_url = f"http://books.toscrape.com/catalogue/{'/'.join(book_path)}"
            print(f"URL relative: {relative_url}, URL absolue: {absolute_url}")
            book_count += 1

            try:
                book_data = extract_book_data(absolute_url)
                save_to_csv(book_data, csv_filename)
            except Exception as e:
                print(f"Erreur lors de l'extraction du livre {absolute_url}: {str(e)}")

        next_button = soup.find('li', class_='next')
        if next_button:
            next_page_relative = next_button.a['href']
            current_url = urljoin(current_url, next_page_relative)
        else:
            break

    print(f"Extraction terminée! {book_count} livres ont été traités et sauvegardés dans {csv_filename}")


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

    with open(filename, 'a', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(book_data)

    print(f"Données sauvegardées dans {filename}")
