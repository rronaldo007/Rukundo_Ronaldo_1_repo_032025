import requests
from bs4 import BeautifulSoup
import time
from phase1 import extract_book_data, save_to_csv

def extract_category_books(category_url):
    """Extraire les données de tous les livres d'une catégorie"""
    print(f"Extraction des livres de la catégorie: {category_url}")
    
    response = requests.get(category_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    category_name = soup.find('h1').text.strip()
    csv_filename = f"data/{category_name}.csv"
    
    book_urls = []
    
    base_url = category_url.rsplit('/', 1)[0]
    current_url = category_url
    
    while True:
        print(f"Traitement de la page: {current_url}")
        
        response = requests.get(current_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        book_containers = soup.find_all('article', class_='product_pod')
        
        for book in book_containers:
            relative_url = book.h3.a['href']
            
            if '../../../' in relative_url:
                absolute_url = 'http://books.toscrape.com/catalogue/' + relative_url.replace('../../../', '')
            elif '../../' in relative_url:
                absolute_url = 'http://books.toscrape.com/catalogue/' + relative_url.replace('../../', '')
            else:
                absolute_url = base_url + '/' + relative_url
            
            book_urls.append(absolute_url)
        
        next_button = soup.find('li', class_='next')
        if next_button:
            next_page_relative = next_button.a['href']
            current_url = base_url + '/' + next_page_relative
        else:
            break
    
    print(f"Nombre total de livres trouvés: {len(book_urls)}")
    
    for i, url in enumerate(book_urls, 1):
        try:
            print(f"Extraction du livre {i}/{len(book_urls)}: {url}")
            book_data = extract_book_data(url)
            save_to_csv(book_data, csv_filename)
            
            time.sleep(0.5)
        except Exception as e:
            print(f"Erreur lors de l'extraction du livre {url}: {str(e)}")
    
    print(f"Extraction terminée! Toutes les données ont été sauvegardées dans {csv_filename}")

