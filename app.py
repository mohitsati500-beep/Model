from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    iq: float
    cgpa: float


@app.post("/predict")
def predict(student: Student):

    if student.iq >= 110 and student.cgpa >= 7.0:
        prediction = 1
        result = "Placed"
    else:
        prediction = 0
        result = "Not Placed"

    return {
        "prediction": prediction,
        "result": result
    }