import requests
import os
def GET_USER():
    usuario = requests.request("GET",'https://randomuser.me/api/')
    
    return usuario.json()
    pass

def obtener_lista_usuarios():
    list_user = []
    for x in range(20):
        usuario = GET_USER()
        list_user.append({
            "username" : usuario["results"][0]['name']['first']+" "+usuario['results'][0]['name']['first'],
            "edad" : usuario["results"][0]['dob']['age'],
        })
    return list_user

def guardar_lista(lista, nombre_archivo):
    #print("LA RUTA ES: {}".format(str(os.getcwd()).replace(chr(92),chr(47))))
    base_path = os.getcwd().replace(chr(92),chr(47))
    archivo = open(base_path+"/"+nombre_archivo, "w")
    for titulos in lista:
        archivo.write(titulos + os.linesep)
    archivo.close()

def etiquetar_usuario(lista_usuario):
    for usuario in lista_usuario:
        if usuario['username'][0] == 'a' or usuario["username"][0] == 'A':
            usuario['es_letra_a'] = True
        else:
            usuario["es_letra_a"] = False

def importar_usuarios():
    lista_usuario = obtener_lista_usuarios()
    etiquetar_usuario(lista_usuario)
    return lista_usuario

if __name__ == "__main__":
    lista_usuario = obtener_lista_usuarios()
    etiquetar_usuario(lista_usuario)

