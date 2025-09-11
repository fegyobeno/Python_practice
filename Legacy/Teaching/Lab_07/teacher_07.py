from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uvicorn

app = FastAPI()

# 3. Create the Temperature class
class Temperature(BaseModel):
    temp: float
    unit: str
    location: str
    time: datetime

# 4. Create a list to store temperature objects
temperatures: List[Temperature] = []

# 2. Define the root endpoint
@app.get("/")
def read_root(name: Optional[str] = None):
    return {"message": "Welcome to the Temperature API {name}" if name else "Welcome to the Temperature API"}

# 5. Create a GET endpoint to return the temperature objects
@app.get("/temperatures", response_model=List[Temperature])
def get_temperatures():
    if not temperatures:
        raise HTTPException(status_code=404, detail="No temperature data available")
    return temperatures

# 6. Create a POST endpoint to add a new temperature object asynchronously
@app.post("/temperatures", response_model=Temperature)
async def add_temperature(temp: Temperature):
    temperatures.append(temp)
    return temp

# 1. Ask for the port number and start the FastAPI server
if __name__ == "__main__":
    port = int(input("Enter the port number to run the server: "))
    uvicorn.run(app, host="0.0.0.0", port=port)