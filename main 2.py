# vamos a recibir dos fotos desde el API y compararlas a ver si son la misma persona
import cv2 
import face_recognition
from fastapi import FastAPI, File, UploadFile
import shutil

def getEncoded(archivoImagen):

    imagen = face_recognition.load_image_file(archivoImagen)
    imagenEncoded = face_recognition.face_encodings(imagen)[0]

    return imagenEncoded




app = FastAPI()

# Este es el primer punto de respuesta del API
# En un navegador colocar:  http://127.0.0.1:8000
@app.get("/")
def read_root():
    return {"Hola":"Mundo Maravilloso con platica"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    
    # Esto toma el archivo pasado como parámetro y lo salva en
    # este directorio como archivoCapturado.jpg
    with open('archivoCapturado.jpeg','wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    # leemos las fotos y obtenemos su codificación
    imagenConocida = getEncoded('f4 2.jpeg')
    imagenAReconocer = getEncoded('archivoCapturado.jpeg')

    resultado = False

    try:
        resultado = face_recognition.compare_faces([imagenConocida], imagenAReconocer)
    except Exception as err:
        resultado = False
    
        

    return {"resultado":  str(resultado)} 

