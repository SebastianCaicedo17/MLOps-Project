import os
import joblib
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

def train_model():
    # 1. Charger le dataset
    print("Chargement des données...")
    data = load_wine()
    X, y = data.data, data.target

    # 2. Séparation en jeu d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Création du pipeline (Prétraitement + Modèle)
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', RandomForestClassifier(random_state=42))
    ])

    # 4. Entraînement du modèle
    print("Entraînement du modèle...")
    pipeline.fit(X_train, y_train)

    # 5. Évaluation
    y_pred = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Métrique calculée - Accuracy : {accuracy:.4f}")

    # 6. Sauvegarde de l'artefact
    os.makedirs("models", exist_ok=True)
    model_path = "models/model.pkl"
    joblib.dump(pipeline, model_path)
    print(f"Modèle sauvegardé avec succès dans : {model_path}")

if __name__ == "__main__":
    train_model()