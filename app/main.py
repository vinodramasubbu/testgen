from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal

app = FastAPI()

class CalculationRequest(BaseModel):
    operator: Literal["add", "subtract", "multiply", "divide"]
    numbers: list[float]

@app.post("/calculate")
def calculate(request: CalculationRequest):
    operator = request.operator
    numbers = request.numbers

    if len(numbers) != 2:
        raise HTTPException(status_code=400, detail="Exactly two numbers are required.")

    if operator == "add":
        result = numbers[0] + numbers[1]
    elif operator == "subtract":
        result = numbers[0] - numbers[1]
    elif operator == "multiply":
        result = numbers[0] * numbers[1]
    elif operator == "divide":
        if numbers[1] == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
        result = numbers[0] / numbers[1]
    else:
        raise HTTPException(status_code=400, detail="Invalid operator.")

    return {"result": result}