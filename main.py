from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import os
from rembg import remove

app = FastAPI()

@app.post("/remove-bg/")
async def remove_background(file: UploadFile = File(...)):
    input_data = await file.read()
    output_data = remove(input_data)

    output_path = f"output_{file.filename}"
    with open(output_path, "wb") as out_file:
        out_file.write(output_data)

    return FileResponse(output_path, media_type="image/png", filename=f"no-bg-{file.filename}")
