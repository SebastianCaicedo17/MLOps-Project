# Rapport : Mini Projet MLOps

## 1. Informations Générales
* **Nom et Prénom :** Sebastian Caicedo
* **Dataset choisi :** Wine Dataset (Classification multiclasse, scikit-learn)

---

## 2. Résumé du Projet et Stack Technique
Ce projet met en œuvre un flux MLOps complet, de la création du modèle jusqu'à son déploiement automatisé :
* **Entraînement du modèle :** Utilisation d'un pipeline scikit-learn (StandardScaler + RandomForestClassifier) entraîné sur le dataset Wine. L'artefact généré (model.pkl) affiche une précision (accuracy) de 100% sur le jeu de test.
* **Développement de l'API :** Création d'une API web avec **FastAPI** exposant deux endpoints :
  * GET /health : Vérification de l'état de l'API et de la disponibilité du modèle.
  * POST /predict : Inférence basée sur les caractéristiques physico-chimiques d'un vin envoyées en format JSON.
* **Conteneurisation :** Emballage de l'application via **Docker** garantissant la portabilité du code et des dépendances.
* **Intégration et Déploiement Continus (CI/CD) :** Automatisation du flux de travail avec **GitHub Actions**.

---

## 3. Preuves d'exécution de la Pipeline CI

La pipeline CI (ci.yml) a été configurée pour répondre de manière asymétrique en fonction de la branche ciblée par le push.

### Scénario 1 : Push sur une branche feature/*
Lorsqu'un développeur pousse du code sur une branche de fonctionnalité (ici feature/test-pipeline), la pipeline déclenche uniquement l'installation des dépendances et l'entraînement du modèle. Cela permet de valider l'intégrité du code sans consommer de ressources inutiles pour la publication d'une image.


### Scénario 2 : Push sur la branche develop
Lorsqu'une modification est poussée sur la branche de développement (develop), la pipeline exécute le flux complet. Après avoir validé l'entraînement du modèle, elle déclenche le job de construction et de publication. L'image Docker est construite puis poussée automatiquement sur le registre **GitHub Container Registry (GHCR)**.
