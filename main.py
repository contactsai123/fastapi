from fastapi import FastAPI
from flask import Flask, request, jsonify, json, abort
from flask_cors import CORS, cross_origin

import pandas as pd

app = FastAPI()

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.get("/")
@cross_origin()
def home():
    return {"message":"Hello TutLinks.com"}

@app.get("/query")
@cross_origin()
def func1():
    return [
  {
    "columns":[
      {"text":"Time","type":"time"},
      {"text":"Country","type":"string"},
      {"text":"Number","type":"number"}
    ],
    "rows":[
      [1234567,"SE",123],
      [1234567,"DE",231],
      [1234567,"US",321]
    ],
    "type":"table"
  }
]
@app.get("/search")
@cross_origin()
def func2():
    return ["Active Memory (MB)","Inactive Memory (MB)","CPU Utilization (%)","Disk I/O Utilization (IOPS)"]
