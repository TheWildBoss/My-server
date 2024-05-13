import os
import requests
import zipfile

# URL del archivo ZIP que deseas descargar
url_archivo_zip = "https://edge.forgecdn.net/files/4497/274/server-1.2.3.zip"

# Ruta de destino para guardar el archivo ZIP
ruta_destino = "/workspaces/My-server/servidor_minecraft/server-1.2.3.zip"

# Descargar el archivo ZIP
response = requests.get(url_archivo_zip)
with open(ruta_destino, "wb") as archivo_zip:
    archivo_zip.write(response.content)

# Descomprimir el archivo ZIP en la misma ubicación
with zipfile.ZipFile(ruta_destino, "r") as zip_ref:
    zip_ref.extractall("/workspaces/My-server/servidor_minecraft")

print("Archivo ZIP descargado y descomprimido con éxito.")