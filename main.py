from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# 1. Initialisation de l'application FastAPI
app = FastAPI(title="Wine Prediction API", description="API pour prédire la classe de vin")

# 2. Chargement du modèle au démarrage
try:
    model = joblib.load("models/model.pkl")
except Exception as e:
    model = None
    print(f"Erreur lors du chargement du modèle : {e}")

# 3. Définition du format d'entrée JSON attendu
class WineInput(BaseModel):
    # Le dataset Wine possède 13 features (alcool, acide malique, etc.)
    features: list[float]

# 4. Endpoint de santé
@app.get("/health")
def health_check():
    if model is None:
        raise HTTPException(status_code=503, detail="Modèle indisponible")
    return {"status": "ok", "message": "L'API est fonctionnelle et le modèle est chargé !"}

# 5. Endpoint de prédiction
@app.post("/predict")
def predict(data: WineInput):
    if model is None:
        raise HTTPException(status_code=503, detail="Modèle indisponible")
    
    try:
        # scikit-learn attend un tableau 2D pour les prédictions
        input_data = np.array(data.features).reshape(1, -1)
        prediction = model.predict(input_data)
        
        return {"prediction": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur lors de la prédiction : {e}")
# Ceci est un test pour la CI
