# Euro Fit

Euro Fit est une application de gestion complète pour un club de fitness. Elle permet de superviser l'ensemble des aspects liés aux salles, équipements, membres, transactions financières et personnel (coachs, médecins, agents de sécurité et de nettoyage).

## Fonctionnalités

- **Gestion du personnel et des membres**  
  Suivi des coachs, médecins, agents de sécurité, agents de nettoyage ainsi que des membres du club.

- **Gestion des abonnements et des transactions**  
  Enregistrement et suivi des abonnements, paiements et souscriptions.

- **Administration des infrastructures**  
  Gestion des salles, machines, capteurs, équipements, et analyses corporelles.

- **Insertion de données fictives**  
  Utilisation de Faker pour générer automatiquement des jeux de données afin de faciliter les tests et la démonstration des fonctionnalités.

## Technologies utilisées

- **Python 3.x**  
- **FastAPI** : Framework pour créer l'API REST.
- **SQLAlchemy** : ORM pour l'interaction avec la base de données.
- **SQLite** : Base de données relationnelle.
- **Faker** : Génération de données fictives pour les tests.
- **Pytest** : Framework de test pour Python.

## Prérequis

- Python 3.x installé.
- Pip pour la gestion des packages.

## Installation

1. **Cloner le dépôt**

   ```bash
   git clone <URL_DU_REPO>
   cd euro_fit
   ```

2. **Installer les dépendances**

   ```bash
   pip install -r requirements.txt
   ```

3. **Initialisation de la base de données**  
   Exécutez le script `create_db.py` pour créer et initialiser la base de données avec toutes les tables requises.

   ```bash
   python create_db.py
   ```

4. **Insertion des données fictives**  
   Pour peupler la base avec des données de test, exécutez le script `fake_my_db.py` :

   ```bash
   python fake_my_db.py
   ```

## Utilisation

Pour lancer l'API en mode développement avec rechargement automatique, utilisez la commande suivante :

  ```bash
   python -m uvicorn api.main:app --reload
   ```

L'API sera accessible par défaut sur [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Structure du projet

- `api`
Contient l'implémentation de l'API avec :

  - `main.py` : Fichier principal définissant les endpoints.
  - `models.py` : Définition des modèles SQLAlchemy.
  - `schemas.py` : Définition des schémas Pydantic pour la validation des données.
  - `crud.py` : Fonctions CRUD.
  - `database.py` : Configuration de la base de données et création de la session.
- `database`
  - `create_db.py` : Script de création et d'initialisation de la base de données.
  - `fake_my_db.py` : Script de génération et insertion de données fictives.
- test
Contient l'ensemble des tests unitaires et d'intégration.

- `requirements.txt`
Liste des dépendances du projet.

## Tests

Pour exécuter l'ensemble des tests, lancez la commande suivante :

  ```bash
   pytest --maxfail=1 --disable-warnings -q
   ```

## Contribution

Les contributions sont les bienvenues !
Pour proposer des améliorations ou corriger des problèmes, veuillez ouvrir une issue ou soumettre une pull request.
