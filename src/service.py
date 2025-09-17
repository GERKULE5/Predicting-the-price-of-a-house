import joblib
from fastapi import FastAPI
from src.schemas.userDataScheme import UserData


app = FastAPI()
model = joblib.load("src/models/model.pkl")


@app.post('/predict')
async def predict(data: UserData):
    inputData = [data.totalArea, data.rommsCount, data.repairLevel]
    predictionPrice = model.predict([inputData])[0].item()

    return {"price": predictionPrice}