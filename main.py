from fastapi import FastAPI
from fastapi.params import Body
from logic import convert_files

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Program is ready to convert files into images. Provide the files root directory path and the path to save the images"}


# Route for converting the files into images
@app.post("/convert")
def getPath(payload: dict = Body(...)):
    convert_files(payload)
    return {"message": "Conversion Completed"}