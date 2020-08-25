from fastapi import FastAPI

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.get("/")
def home():
    return {"message":"Hello TutLinks.com"}

@app.get("/query")
def func1():
    return { "target": "123",
"datapoints":[
[1597829556, 111],
[1597829576, 222],
[1597829616, 333],
[1597829736, 210]
]
           }
