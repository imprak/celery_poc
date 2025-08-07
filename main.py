from fastapi import FastAPI, Path

from celery_app import continue_task

app = FastAPI()


@app.post("/hello/{Name}")
def greeter(name: str = Path(alias="Name")) -> dict:
    continue_task.delay(name)
    return {"Message": "Your task is being processed in background"}
