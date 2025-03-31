import requests
from bs4 import BeautifulSoup
import os
import time
from phase2 import extract_category_books

def extract_all_categories(base_url):
    """
    Extraire toutes les catégories et leurs livres
    """
    print(f"Extraction de toutes les catégories du site: {base_url}")
    
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    category_container = soup.find('div', class_='side_categories')
    category_list = category_container.find('ul').find('ul').find_all('li')
    
    total_categories = len(category_list)
    print(f"Nombre total de catégories trouvées: {total_categories}")
    
    for i, category_item in enumerate(category_list, 1):
        category_name = category_item.a.text.strip()
        category_url = base_url + category_item.a['href']
        
        print(f"\n[{i}/{total_categories}] Traitement de la catégorie: {category_name}")
        
        try:
            extract_category_books(category_url)
            
            if i < total_categories:
                print(f"Pause de 2 secondes avant la prochaine catégorie...")
                time.sleep(2)
                
        except Exception as e:
            print(f"Erreur lors de l'extraction de la catégorie {category_name}: {str(e)}")
    
    print("\nExtraction de toutes les catégories terminée!")