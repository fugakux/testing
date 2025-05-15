from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello! Use /multiply?number=...&multiplier=..."}

@app.get("/multiply")
def multiply(number: float = Query(...), multiplier: float = Query(...)):
    result = number * multiplier
    return JSONResponse(content={
        "number": number,
        "multiplier": multiplier,
        "result": result
    })
