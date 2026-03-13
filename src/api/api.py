import uuid
from fastapi import FastAPI, Body, status, Form
from fastapi.responses import JSONResponse, FileResponse
from test_predict import Predictor
from pydantic import BaseModel
from typing import Annotated
class PinguinSchema(BaseModel):
    Culmen_Length: int 
    Culmen_Depth: int 
    Flipper_Length: int 
    Body_Mass: int 
    Delta15N: int 
    Delta13C: int 
 
# условная база данных - набор объектов Person

 
app = FastAPI()
 
@app.get("/")
async def main():
    return FileResponse("public/index.html")
 
 
@app.post("/api/predict")
def get_person(model, pinguin: Annotated[PinguinSchema, Form()]):
    predictor = Predictor()
    # tmp = 
    return predictor.predict_api(model,pinguin)
