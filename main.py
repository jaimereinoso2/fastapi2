from fastapi import FastAPI, File, UploadFile
import shutil

app = FastAPI()

@app.post('/inicio')
async def ruta_de_prueba(file: UploadFile):

    with open('archivoCapturado.jpeg','wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"archivo":  "archivoCapturado.jpg"} 
    