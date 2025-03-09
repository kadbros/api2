from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/first")
async def first_endpoint(response: Response):
    response.headers["Content-Type"] = "application/json"
    response.headers["Authorization"] = "Bearer token123"
    response.status_code = 200
    return {
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "Bearer token123"
        },
        "status": 200
    }

@app.get("/second")
async def second_endpoint(response: Response):
    response.headers["Content-Type"] = "application/json"
    response.headers["Authorization"] = "Bearer token123"
    response.status_code = 400
    return {
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "Bearer token123"
        },
        "body": {
            "param1": "value1",
            "param2": "value2"
        },
        "status": 400
    }
