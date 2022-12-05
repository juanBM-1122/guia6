from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, request
from utilidades_web.obtener_titulos import bonita_sopa
from utilidades_web.obtener_titulos import obtener_usuario

app = Flask(__name__, template_folder="utilidades_web/templates")
bootstrap = Bootstrap5(app)
@app.route("/persona/<string:nombre>/<int:edad>")
def inicio(nombre,edad):
    context =  {
        "nombre"  : nombre,
        "edad" : edad
    }
    return render_template('ejercicio1/persona.html', usuario = context)
@app.route("/")
def formulario_busqueda_noticias():
    return render_template("ejercicio3/formulario.html")

@app.route("/resultados", methods = ["GET",'POST'])
def resultados_noticias():
    if request.method == "GET":
        palabra_clave = request.args.get("inputPalabraClave")
        lista_titulos = []
        lista_completa = bonita_sopa.obtener_lista()[0:20]
        if palabra_clave:
            for titulo in lista_completa:
                if palabra_clave.upper() in titulo.upper():
                    lista_titulos.append(titulo)
        if lista_titulos:
            print(lista_titulos)
            contexto = {'lista':lista_titulos, 'mensaje':"Las coincidencias se muestra a continuación: "}
            return render_template("ejercicio3/resultados_noticias.html", contexto = contexto)
        else:
            contexto = {"lista" : lista_completa, 'error': "No se encontrarón coincidencias"}
            return render_template("ejercicio3/resultados_noticias.html", contexto = contexto)
    else:
        return render_template("ejercicio3/resultados_noticias.html")
@app.route("/formulario-calculadora/")
def caluladora():
    return render_template("ejercicio2/calc.html")

@app.route("/lista-usuarios")
def listar_usuarios():
    usuarios = obtener_usuario.importar_usuarios()
    if usuarios:
        return render_template("ejercicio4/lista-usuarios.html",user_list = usuarios)
    else:
        error = "No hay usuarios en la API"
        render_template("plantilla.html", mensaje_error = error)
    pass

@app.route("/math",methods = ["GET","POST"])
def realizar_calculo():
    if request.method == "GET":
        num1 = float(request.args.get("num1"))
        num2 = float(request.args.get("num2"))
        opcion = request.args.get("opcion")
        respuesta = 0
        error = None
        if opcion == "suma":
            respuesta = num1 +num2
        elif opcion == "resta":
            respuesta = num1 - num2
        elif opcion == "multiplicacion":
            respuesta = num1 * num2
        elif opcion == "division":
            if num2 == 0:
                error = "No se puede dividir entre cero"
        contexto = {'resultado': respuesta,'error':error}
        return render_template('ejercicio2/respuesta.html', resultados = contexto)
    else:
        pass
if __name__ == "__main__":
    app.run(debug=True)