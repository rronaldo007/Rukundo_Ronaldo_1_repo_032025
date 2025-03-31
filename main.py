import os

from phase4 import extract_book_data_with_image

def main():
    """
    Fonction principale qui démontre l'utilisation du module
    """
    print("Démarrage du programme de scraping Books to Scrape - Phase 4")
    
    # Créer les répertoires nécessaires
    os.makedirs('data', exist_ok=True)
    os.makedirs('images', exist_ok=True)
    
    # URL d'exemple pour démontrer le fonctionnement
    book_url = "https://books.toscrape.com/catalogue/the-requiem-red_995/index.html"
    
    print(f"Extraction des données et téléchargement de l'image pour: {book_url}")
    
    # Extraire les données du livre et télécharger son image
    extract_book_data_with_image(book_url)
    
    # Sauvegarder les données dans un fichier CSV
    
    print("\nPhase 4 terminée!")

if __name__ == "__main__":
    main()