from fastapi import FastAPI
from flask import Flask
from flask_cors import CORS

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.get("/")
@cross_origin()
def home():
    return {"message":"Hello TutLinks.com"}
