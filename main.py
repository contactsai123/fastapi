from fastapi import FastAPI

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.get("/")
def home():
    return {"message":"Hello TutLinks.com"}

@app.get('/query/')
def func1():
       return {"status": "success",
    "data": {
        "resultType": "matrix",
        "result": [
            {
                "metric": {
                    "__name__": "node_memory_Inactive_bytes",
                    "instance": "localhost:9100",
                    "job": "node"
                },
                "values": [
                    [
                        1597829526,
                        "421081088"
                    ],
                    [
                        1597829536,
                        "421183488"
                    ],
                    [
                        1597829546,
                        "421183488"
                    ],
                    [
                        1597829556,
                        "403398656"
                    ],
                    [
                        1597829566,
                        "403476480"
                    ],
                    [
                        1597829576,
                        "403476480"
                    ],
                    [
                        1597829586,
                        "404279296"
                    ],
                    [
                        1597829596,
                        "404447232"
                    ],
                    [
                        1597829606,
                        "404447232"
                    ],
                    [
                        1597829616,
                        "404484096"
                    ],
                    [
                        1597829626,
                        "405118976"
                    ],
                    [
                        1597829636,
                        "405118976"
                    ],
                    [
                        1597829646,
                        "405168128"
                    ],
                    [
                        1597829656,
                        "405471232"
                    ],
                    [
                        1597829666,
                        "405471232"
                    ],
                    [
                        1597829676,
                        "405487616"
                    ],
                    [
                        1597829686,
                        "406052864"
                    ],
                    [
                        1597829696,
                        "406052864"
                    ],
                    [
                        1597829706,
                        "406155264"
                    ],
                    [
                        1597829716,
                        "406167552"
                    ],
                    [
                        1597829726,
                        "406167552"
                    ],
                    [
                        1597829736,
                        "406192128"
                    ],
                    [
                        1597829746,
                        "406552576"
                    ]
                ]
            }
        ]
    }
}
