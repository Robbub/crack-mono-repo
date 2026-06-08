from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "online"
    }

@app.post("/process-all")
def process_all():

    # call existing pipeline

    return {
        "status": "success"
    }