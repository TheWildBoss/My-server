import os
import requests
import zipfile

# URL del archivo ZIP que deseas descargar
url_archivo_zip = "https://download1582.mediafire.com/wp6wr0d8urqgLWOJRTjpmA2Ct-wu5Ga40m9qnEMP4G14G_ea26O4SNOnuKSq8lhk9Q-ha8dTPhOASYfZ6zSvcE3LmYJqVYP6JBFlLUu9CLwcrE7n7Ry7MU5Qh_PJOtsqy3Qsplm6qCx6c4xdG0B3wkz3H_pvODpz_L36BGXkCA/i188v240ecpa1zf/Minecraft-server-20240513T232640Z-001.zip"

# Ruta de destino para guardar el archivo ZIP
ruta_destino = "/workspaces/My-server/Minecraft-server-20240513T232640Z-001.zip"

# Descargar el archivo ZIP
response = requests.get(url_archivo_zip)
with open(ruta_destino, "wb") as archivo_zip:
    archivo_zip.write(response.content)

# Descomprimir el archivo ZIP en la misma ubicación
with zipfile.ZipFile(ruta_destino, "r") as zip_ref:
    zip_ref.extractall("/workspaces/My-server")

print("Archivo ZIP descargado y descomprimido con éxito.")