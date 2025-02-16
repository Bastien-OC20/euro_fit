# Euro Fit

Ce projet est une application de gestion pour un club de fitness, permettant de gérer efficacement l'ensemble des aspects liés aux salles, aux équipements, aux membres et aux transactions financières.

## Fonctionnalités

- **Gestion du personnel et des membres**  
  Suivi des coaches, médecins, agents de sécurité et de nettoyage, ainsi que des membres du club.

- **Gestion des abonnements et des transactions**  
  Enregistrement et suivi des abonnements, paiements et souscriptions.

- **Gestion des infrastructures**  
  Administration des salles, machines, capteurs et équipements.

- **Génération de données fictives**  
  Utilisation de Faker pour créer automatiquement des jeux de données afin de tester et démontrer les différentes fonctionnalités de l'application.

## Technologies utilisées

- **Python 3.x**
- **SQLAlchemy** : ORM pour interagir avec la base de données.
- **SQLite** : Base de données relationnelle.
- **Faker** : Génération de données fictives.

## Installation

1. **Cloner le dépôt**  

```bash
   git clone <URL_DU_REPO>
   cd euro_fit
   ```

1. **Installer les dépendances**

   ```bash
   pip install -r requirements.txt
   ```

2. **Initialisation de la base de données**  
   Exécutez le script `create_db.py` pour créer et initialiser la base de données avec toutes les tables requises.

   ```bash
   python create_db.py
   ```

3. **Insertion des données fictives**  
   Pour peupler la base avec des données de test, exécutez le script `fake_my_db.py` :

   ```bash
   python fake_my_db.py
   ```

## Structure du projet

- `create_db.py` : Script de création et d'initialisation de la base de données.
- `fake_my_db.py` : Génération et insertion de données fictives dans la base.
- `README.md` : Documentation du projet.
- Autres fichiers et dossiers liés aux différentes entités (tables) de la base de données.

## Contribution

Les contributions sont les bienvenues !
Pour proposer des améliorations ou corriger des problèmes, veuillez ouvrir une issue ou soumettre une pull request.
