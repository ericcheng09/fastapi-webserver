import uvicorn
from fastapi import Body, FastAPI, HTTPException, Response
from fastapi import Form, File, UploadFile, Request
import time
import asyncio
app = FastAPI()


@app.get("/simple_get/{path_arg}")
def simple_get(format: str, path_arg):
    if path_arg:
        print(path_arg)
    if format is None:
        return HTTPException(404, "format not found")

    if format.lower() == "text":
        return "This is a text."
    elif format.lower() == "json":
        return {"data": "This is json data"}
    elif format.lower() == "image":
        with open("image.jpg", "rb") as f:
            frame = f.read()
        return Response(frame, media_type="image/jpeg")


@app.post("/json_post")
async def json_post(request: Request):
    json_data = await request.json()
    text = await request.body()

    print(f"JSON: {json_data}")
    print(f"TEXT: {text}")

    return "Json get."


# @app.post("/json_post")
# async def json_post(data: dict = Body(...)):
#     print(data)
#     return "Json get."


@app.post("/form_post")
def form_post(test: str = Form(), file: UploadFile = File()):
    # Need "python-multipart"
    print(test)
    if file:
        print(file)
    return "Form data get"


@app.get("/thread_test")
def thread_test():
    print("thread Enter")
    time.sleep(5)
    print("thread Leave")
    return "thread test"


@app.get("/async_test")
async def async_test():
    print("async Enter")
    await asyncio.sleep(5)  # can receive multiple requests at the same.
    # time.sleep(3) # will cause request to wait for previoust request is handled
    print("async Leave")

    return "async test"


if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=5000, root_path="/", workers=2)
    uvicorn.run("server:app", host="0.0.0.0",
                port=5000, root_path="/", workers=1)
