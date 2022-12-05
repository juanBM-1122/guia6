from bs4 import BeautifulSoup
import requests
import os

def obtener_lista():
    noticias_enlaces = []
    titulo_enlaces = []
    lista_titulos = []
    data_noticias = requests.get("https://www.eitb.eus/es/tag/ciencia/")
    documento_html_noticias = BeautifulSoup(data_noticias.text , "html.parser")
    for tag_h2 in documento_html_noticias.find_all("h2",class_ = "titulo"):
        noticias_enlaces.append(tag_h2)
    for title_a in noticias_enlaces:
        titulo_enlaces.append(title_a)
    for titulo_text in titulo_enlaces :
        lista_titulos.append(titulo_text.a.text)
    return lista_titulos

def guardar_lista(lista, nombre_archivo):
    #print("LA RUTA ES: {}".format(str(os.getcwd()).replace(chr(92),chr(47))))
    base_path = os.getcwd().replace(chr(92),chr(47))
    archivo = open(base_path+"/"+nombre_archivo, "w")
    for titulos in lista:
        archivo.write(titulos + os.linesep)
    archivo.close()
if __name__ == "__main__":
    lista = obtener_lista()
    guardar_lista(lista,"backup.txt")