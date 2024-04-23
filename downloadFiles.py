# f   F
from bs4 import BeautifulSoup
import requests
import time
import os
from subprocess import Popen
import subprocess
import validators

class DownloadFiles() : 
    def __init__ (self, url):
        self.url = url
        self.user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        self.listaUrl = []
        self.listaArchivos = []
        self.rutaResultado = f"{os.getcwd()}/result"

    def crearDirectory (self):
        nombre = self.url.split("/")[2]
        if os.path.exists( f"{self.rutaResultado}/{nombre}" ):
            #print(nombre, self.url)
            return True
        else: 
            os.makedirs( f"{self.rutaResultado}/{nombre}" )
            return True
        
    def ejecutarComando(self, url):
        nombre = self.url.split("/")[2]
        os.chdir(f"{self.rutaResultado}/{nombre}")
        comando = f"wget {url} >/dev/null 2>&1"
        print(comando)
        salida = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE).stdout
        nuevaSalida = salida.read()
        nuevaSalida = nuevaSalida.decode("utf-8")
        time.sleep(2)

        

    def crawling(self, url):
        if self.crearDirectory():
            if validators.url(url):
                response = requests.get(url, headers = { 'User-Agent': self.user_agent})
                if response.status_code == 200: 
                    soup = BeautifulSoup(response.text, 'html.parser')
                    for a in soup.find_all('td'):
                        if a.findChildren('a'):
                            for t in a.findChildren('a'):
                                if t.text != 'Parent Directory':
                                    href = t.get('href')
                                    if href.find('/') <= 0:
                                        u = f"{url}/{href}"
                                        self.listaArchivos.append(u)
                                    else: 
                                        u = f"{url}/{href}"
                                        self.listaUrl.append(u)
                                        self.crawling(u)
                else:
                    pass