import requests
from bs4 import BeautifulSoup
import csv
import os
import time

from phase1 import extract_book_data, save_to_csv

def main():
    print("Démarrage du programme de scraping Books to Scrape - Phase 1")
    
    # Créer le dossier pour les données
    os.makedirs('data', exist_ok=True)
    
    # URL d'exemple pour un livre
    book_url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    
    print(f"Extraction des données du livre: {book_url}")
    
    # Extraire les données du livre
    book_data = extract_book_data(book_url)
    
    # Sauvegarder les données dans un fichier CSV
    save_to_csv(book_data)
    
    print("\nPhase 1 terminée!")

if __name__ == "__main__":
    main()