from fastapi import FastAPI
import time

app = FastAPI()


@app.get("/")
def root():
    return {"version": "1.0"}


@app.get("/time")
def get_time():
    return {
        "time": int(time.time())
    }