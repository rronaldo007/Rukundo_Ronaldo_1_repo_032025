import os

from phase3 import extract_all_categories

def main():
    print("Démarrage du programme de scraping Books to Scrape - Phase 3")
    
    # Créer le dossier pour les données
    os.makedirs('data', exist_ok=True)
    
    # URL de base par défaut
    base_url = "http://books.toscrape.com/"
    
    # Extraire toutes les catégories et leurs livres
    extract_all_categories(base_url)
    
    print("\nPhase 3 terminée!")

if __name__ == "__main__":
    main()