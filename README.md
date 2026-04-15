# Rapport : Mini Projet MLOps

## 1. Informations Générales
* [cite_start]**Nom et Prénom :** Sebastian Caicedo [cite: 65]
* [cite_start]**Dataset choisi :** Wine Dataset (Classification multiclasse, `scikit-learn`) [cite: 66]
* [cite_start]**URL du dépôt Git :** [https://github.com/SebastianCaicedo17/MLOps-Project](https://github.com/SebastianCaicedo17/MLOps-Project) [cite: 67]

---

## 2. Résumé du Projet et Stack Technique
[cite_start]Ce projet met en œuvre un flux MLOps complet, de la création du modèle jusqu'à son déploiement automatisé [cite: 3-8] :
* [cite_start]**Entraînement du modèle :** Utilisation d'un pipeline `scikit-learn` (StandardScaler + RandomForestClassifier) entraîné sur le dataset Wine [cite: 13-19]. [cite_start]L'artefact généré (`model.pkl`) affiche une précision (accuracy) de 100% sur le jeu de test[cite: 21, 22].
* [cite_start]**Développement de l'API :** Création d'une API web avec **FastAPI** [cite: 59] exposant deux endpoints :
  * [cite_start]`GET /health` : Vérification de l'état de l'API et de la disponibilité du modèle[cite: 26, 29].
  * [cite_start]`POST /predict` : Inférence basée sur les caractéristiques physico-chimiques d'un vin envoyées en format JSON[cite: 27, 30, 31].
* [cite_start]**Conteneurisation :** Emballage de l'application via **Docker** garantissant la portabilité du code et des dépendances [cite: 32-38, 60].
* [cite_start]**Intégration et Déploiement Continus (CI/CD) :** Automatisation du flux de travail avec **GitHub Actions**[cite: 39, 40, 61].

---

## 3. Preuves d'exécution de la Pipeline CI

[cite_start]La pipeline CI (`ci.yml`) a été configurée pour répondre de manière asymétrique en fonction de la branche ciblée par le push [cite: 40-50].

### Scénario 1 : Push sur une branche `feature/*`
[cite_start]Lorsqu'un développeur pousse du code sur une branche de fonctionnalité (ici `feature/test-pipeline`), la pipeline déclenche uniquement l'installation des dépendances et l'entraînement du modèle [cite: 41-44]. Cela permet de valider l'intégrité du code sans consommer de ressources inutiles pour la publication d'une image.

### Scénario 2 : Push sur la branche `develop`
Lorsqu'une modification est poussée sur la branche de développement (`develop`), la pipeline exécute le flux complet. Après avoir validé l'entraînement du modèle, elle déclenche le job de construction et de publication. [cite_start]L'image Docker est construite puis poussée automatiquement sur le registre **GitHub Container Registry (GHCR)** [cite: 45-50, 53].
