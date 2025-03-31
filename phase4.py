import requests
from bs4 import BeautifulSoup
import os
import time
from phase1 import extract_book_data, save_to_csv

def download_cover_image(image_url, title, category):
    """
    Télécharge et enregistre l'image de couverture d'un livre
    """
    os.makedirs('images', exist_ok=True)
    
    category_folder = category.strip().replace(' ', '_').lower()
    os.makedirs(f'images/{category_folder}', exist_ok=True)
    
    clean_title = "".join(c if c.isalnum() or c in [' ', '.', '_'] else '_' for c in title)
    clean_title = clean_title.replace(' ', '_').lower()[:100]
    
    file_extension = image_url.split('.')[-1].lower()
    if '?' in file_extension:
        file_extension = file_extension.split('?')[0]
    
    file_path = f'images/{category_folder}/{clean_title}.{file_extension}'
    
    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(8192):
                file.write(chunk)
        
        print(f"Image téléchargée: {file_path}")
        return file_path
    
    except Exception as e:
        print(f"Erreur lors du téléchargement de l'image {image_url}: {str(e)}")
        return None

def extract_book_data_with_image(url):
    """
    Extraire les données d'un livre et télécharger son image de couverture
    """
    # Extraire les données du livre avec la fonction de phase1
    book_data = extract_book_data(url)
    
    # Télécharger l'image de couverture
    image_path = download_cover_image(
        book_data['image_url'], 
        book_data['title'],
        book_data['category']
    )
    
    # Ajouter le chemin local de l'image aux données du livre
    book_data['local_image_path'] = image_path
    
    return book_data

