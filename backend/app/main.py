from fastapi import FastAPI, Request
import logging
import os


STAGE = os.environ.get("STAGE")
if not STAGE:
    raise ValueError("STAGE not set")

app = FastAPI(root_path="/api/")
# app = FastAPI()
logger = logging.getLogger("uvicorn")


@app.get("/")
def read_root(request: Request):
    print(f'message: Hello World, root_path: {request.scope.get("root_path")}')
    return {
        "message": "Hello World",
        "root_path": request.scope.get("root_path"),
        "edit": 13,
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


print("Running main.py")


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000)
