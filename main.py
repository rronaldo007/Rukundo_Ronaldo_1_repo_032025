import os
import sys
import time
from extract_book_from_url import extract_book_data
from extract_books_by_category import extract_category_books, save_to_csv
from extract_all_cotegories_and_books import extract_all_categories
from download_all_cover_image import extract_all_book_images, download_cover_image
from download_image_and_category import download_all_book_images_by_category


def main():
    os.makedirs('data', exist_ok=True)
    os.makedirs('images', exist_ok=True)

    if len(sys.argv) < 2:
        choix = demander_choix()
        if not choix:
            return
    else:
        choix = sys.argv[1:]

    try:
        executer_commande(choix)

    except KeyboardInterrupt:
        print("\nOpération interrompue par l'utilisateur.")
        sys.exit(1)
    except Exception as e:
        print(f"Erreur: {str(e)}")
        sys.exit(1)

    print("\nOpération terminée avec succès!")


def executer_commande(args):
    if not args:
        return

    command = args[0].lower()

    match command:
        case "book" if len(args) >= 2:
            url = args[1]
            print(f"Extraction du livre: {url}")
            try:
                book_data = extract_book_data(url)
                if book_data:
                    save_to_csv(book_data)
                    print(f"Livre '{book_data['title']}' extrait avec succès!")
                else:
                    print("Échec de l'extraction du livre.")
            except Exception as e:
                print(f"Erreur lors de l'extraction du livre {url}: {str(e)}")

        case "category" if len(args) >= 2:
            url = args[1]
            print(f"Extraction de la catégorie: {url}")
            try:
                extract_category_books(url)
            except Exception as e:
                print(f"Erreur lors de l'extraction de la catégorie {url}: {str(e)}")

        case "allcategories":
            print("Extraction de toutes les catégories")
            base_url = "http://books.toscrape.com/"
            try:
                extract_all_categories(base_url)
            except Exception as e:
                print(f"Erreur lors de l'extraction des catégories: {str(e)}")

        case "allimages":
            print("Téléchargement de toutes les images de couverture")
            try:
                extract_all_book_images()
            except Exception as e:
                print(f"Erreur lors du téléchargement des images: {str(e)}")

        case "categoryimages":
            print("Téléchargement des images de leur catégorie")
            try:
                download_all_book_images_by_category()
            except Exception as e:
                print(f"Erreur lors du téléchargement des images de la catégorie {url}: {str(e)}")

        case _:
            print(f"Commande '{command}' invalide ou paramètres manquants")
            print("Utilisez une des commandes: book, category, allcategories, allimages, categoryimages")


def demander_choix():
    print("\nQue souhaitez-vous faire ? (entrez le numéro ou la commande)")
    print("1 ou book      : Extraire un seul livre (vous devrez fournir l'URL)")
    print("2 ou category  : Extraire tous les livres d'une catégorie (vous devrez fournir l'URL)")
    print("3 ou allcategories : Extraire toutes les catégories")
    print("4 ou allimages : Télécharger toutes les images de couverture")
    print("5 ou categoryimages : Télécharger les images d'une catégorie (vous devrez fournir l'URL)")
    print("q ou quitter   : Quitter le programme")

    choix = input("\nVotre choix: ").strip().lower()

    if choix in ('q', 'quitter', 'exit'):
        return None

    mapping = {
        '1': 'book',
        '2': 'category',
        '3': 'allcategories',
        '4': 'allimages',
        '5': 'categoryimages'
    }

    if choix in mapping:
        choix = mapping[choix]

    if choix in ('book', 'category', ):
        url = input(f"Entrez l'URL pour la commande '{choix}': ").strip()
        return [choix, url]
    elif choix in ('allcategories', 'allimages', 'categoryimages'):
        return [choix]
    else:
        print("Choix non reconnu.")
        return demander_choix()  # Redemander avec récursivité


if __name__ == "__main__":
    main()