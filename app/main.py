from fastapi import FastAPI
import uvicorn
from data_interactor import DB_Connection

from api import router


app = FastAPI(title="Contact Manager API", version="1.0.0")

app.include_router(router)

@app.get("/")
def root():
    return {"Welcome to the Contacts Manager"}

if __name__ == "__main__":
    DB_Connection.connect_to_db()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)