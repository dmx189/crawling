# f   F
from tqdm import tqdm
import downloadFiles
import time
import os
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    df = downloadFiles.DownloadFiles(url)
    print(f"Crawling de {url}")
    df.crawling(url)
    print("")
    print(f"Descargando archivos de {url}")

    for n in tqdm(range(len(df.listaArchivos))):
        try:
            df.ejecutarComando(df.listaArchivos[n])
        except Exception:
            print(Exception)

'''print(df.listaUrl)
print(" ")
print(df.listaArchivos)

print(f"Total de URL: {len(df.listaUrl)}")
print(f"Total de Archivos: {len(df.listaArchivos)}")'''