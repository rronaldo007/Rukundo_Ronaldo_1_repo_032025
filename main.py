import os
import sys
from phase1 import extract_book_data, save_to_csv
from phase2 import extract_category_books
from phase3 import extract_all_categories
from phase4 import extract_book_data_with_image

def main():
    """
    Programme simple pour extraire les données de livres depuis books.toscrape.com
    """
    os.makedirs('data', exist_ok=True)
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python main.py 1 <url_livre>              - Extraire un seul livre")
        print("    Exemple: python main.py 1 http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
        print("  python main.py 1i <url_livre>             - Extraire un livre avec son image (sans CSV)")
        print("    Exemple: python main.py 1i http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html")
        print("  python main.py 2 <url_categorie>          - Extraire tous les livres d'une catégorie")
        print("    Exemple: python main.py 2 http://books.toscrape.com/catalogue/category/books/travel_2/index.html")
        print("  python main.py 3                          - Extraire toutes les catégories")
        print("    Exemple: python main.py 3")
        return
    
    command = sys.argv[1]
    
    try:
        if command == "1" and len(sys.argv) >= 3:
            url = sys.argv[2]
            print(f"Extraction du livre: {url}")
            book_data = extract_book_data(url)
            save_to_csv(book_data)
            
        elif command == "1i" and len(sys.argv) >= 3:
            url = sys.argv[2]
            print(f"Extraction du livre avec image: {url}")
            book_data = extract_book_data_with_image(url)
            print("Image téléchargée avec succès!")
            
        elif command == "2" and len(sys.argv) >= 3:
            url = sys.argv[2]
            print(f"Extraction de la catégorie: {url}")
            extract_category_books(url)
            
        elif command == "3":
            print("Extraction de toutes les catégories")
            extract_all_categories("http://books.toscrape.com/")
            
        else:
            print("Commande invalide ou paramètres manquants")
            
    except Exception as e:
        print(f"Erreur: {str(e)}")
        sys.exit(1)
    
    print("Opération terminée avec succès!")

if __name__ == "__main__":
    main()