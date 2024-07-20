# My Python App

Cette application Python utilise GitHub Actions pour exécuter des tests automatisés à chaque fois qu'un changement est poussé sur la branche principale ou lorsqu'une pull request est ouverte. Le fichier de workflow se trouve dans le répertoire `.github/workflows/ci.yml`.


# Structure du Projet
my-python-app/
│
├── .github/
│   └── workflows/
│       └── ci.yml
├── appl/
│   ├── __init__.py
│   └── main.py
├── test/
│   ├── __init__.py
│   └── test_main.py
├── requirements.txt
└── README.md


## CI Pipeline Workflow

### Description

Le workflow CI (Intégration Continue) est conçu pour s'assurer que chaque modification du code source est testée automatiquement. Il se déclenche lors des événements `push` et `pull_request` sur la branche `main`.

### Déclencheurs

- **Push**: Le workflow s'exécute chaque fois qu'un push est effectué sur la branche `main`.
- **Pull Request**: Le workflow s'exécute chaque fois qu'une pull request est ouverte, synchronisée ou réouverte vers la branche `main`.

### Fichier de Configuration

Le fichier de configuration du workflow est `ci.yml`, situé dans le répertoire `.github/workflows/`. Voici le contenu de ce fichier :

```yaml
name: CI Pipeline

# Définir les événements qui déclenchent le workflow
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

# Définir les jobs du workflow
jobs:
  test:
    # Utiliser l'environnement Ubuntu par défaut
    runs-on: ubuntu-latest

    # Définir les steps du job
    steps:
      # Vérifier le dépôt
      - name: Checkout repository
        uses: actions/checkout@v2

      # Configurer Python
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      # Installer les dépendances
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      # Exécuter les tests
      - name: Run test
        run: |
          pytest
