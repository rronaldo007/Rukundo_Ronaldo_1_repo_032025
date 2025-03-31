# Rukundo_Ronaldo_1_repo_032025
# Books Online Price Monitoring System

Ce projet est un système de scraping qui extrait les informations de prix et de produits du site Books to Scrape. Le système est divisé en quatre phases, chacune ajoutant de nouvelles fonctionnalités.

## Installation

1. Clonez ce repository:
```
git clone <votre-repository-url>
cd <nom-du-dossier>
```

2. Créez un environnement virtuel et activez-le:
```
python -m venv env
source env/bin/activate  # Sur Windows, utilisez: env\Scripts\activate
```

3. Installez les dépendances:
```
pip install -r requirements.txt
```

## Fonctionnalités

### Phase 1: Extraction d'un seul livre
Extrait les données d'un livre spécifique et les sauvegarde dans un fichier CSV.

### Phase 2: Extraction d'une catégorie
Extrait les données de tous les livres d'une catégorie spécifique et les sauvegarde dans un fichier CSV.

### Phase 3: Extraction de toutes les catégories
Extrait les données de tous les livres de toutes les catégories et les sauvegarde dans des fichiers CSV séparés par catégorie.

### Phase 4: Téléchargement d'images
Télécharge les images de couverture des livres et les organise par catégorie.

## Utilisation

Le script principal `main.py` offre une interface simple pour utiliser toutes les fonctionnalités:

```
python main.py <commande> [arguments]
```

### Commandes disponibles:

1. **Extraire un seul livre**:
```
python main.py 1 <url_livre>
```
Exemple:
```
python main.py 1 http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html
```

2. **Extraire un livre avec son image**:
```
python main.py 1i <url_livre>
```
Exemple:
```
python main.py 1i http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html
```

3. **Extraire tous les livres d'une catégorie**:
```
python main.py 2 <url_categorie>
```
Exemple:
```
python main.py 2 http://books.toscrape.com/catalogue/category/books/travel_2/index.html
```

4. **Extraire toutes les catégories**:
```
python main.py 3
```

## Structure des fichiers

- `main.py`: Script principal pour exécuter le programme
- `phase1.py`: Fonctions pour extraire les données d'un seul livre
- `phase2.py`: Fonctions pour extraire les données d'une catégorie
- `phase3.py`: Fonctions pour extraire les données de toutes les catégories
- `phase4.py`: Fonctions pour télécharger les images de couverture

## Données extraites

Pour chaque livre, les informations suivantes sont extraites:

- URL de la page produit
- Code produit universel (UPC)
- Titre
- Prix TTC
- Prix HT
- Nombre d'exemplaires disponibles
- Description du produit
- Catégorie
- Évaluation (nombre d'étoiles)
- URL de l'image de couverture

## Sortie

- Les données des livres sont sauvegardées dans le dossier `data/`
- Les images sont sauvegardées dans le dossier `images/` et organisées par catégorie

## Remarques

- Le programme gère automatiquement la pagination sur les pages de catégorie
- Les requêtes sont espacées dans le temps pour éviter de surcharger le serveur
- Les noms de fichiers d'images sont nettoyés pour éviter les problèmes de caractères spéciaux

## Exigences

Voir le fichier `requirements.txt` pour la liste des dépendances.