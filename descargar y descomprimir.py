import os
import requests
import zipfile

# URL del archivo ZIP que deseas descargar
url_archivo_zip = "https://download1323.mediafire.com/08zsnzjzo2wg6N9T0XNFkMR8O8eDazoUXZdtzZrEkf-hQNaQvPk22OvuRCUsyQL35EAJ6cDQI_7uaDr4fRA61GezZuPOGt0vDSvjSif_mp2WuruBfcxE8dXe4U3mMA-Hfj1mwNZRdGu-UbR1xEP2GGZPPWg52pIuo2yqvuhkJA/69nzl22igshktwm/llllll.zip"

# Ruta de destino para guardar el archivo ZIP
ruta_destino = "/workspaces/My-server/servidor_minecraft/llllll.zip"

# Descargar el archivo ZIP
response = requests.get(url_archivo_zip)
with open(ruta_destino, "wb") as archivo_zip:
    archivo_zip.write(response.content)

# Descomprimir el archivo ZIP en la misma ubicación
with zipfile.ZipFile(ruta_destino, "r") as zip_ref:
    zip_ref.extractall("/workspaces/My-server/servidor_minecraft")

print("Archivo ZIP descargado y descomprimido con éxito.")