from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5

app = Flask(__name__, template_folder="../utilidades_web/templates")
boostrap = Bootstrap5(app)

@app.route("/")
def formulario_inicio():
    return render_template("ejercicio5/formulario.html")

@app.route("/result", methods = ["POST","GET"])
def resolucion_formulario():
    if request.method == "POST":
        name = request.form["name"]
        physics = request.form["physics"]
        chemistry = request.form["chemistry"]
        maths = request.form["maths"]
        contexto = {
            'name': name,
            'physics' : physics,
            'chemistry' : chemistry,
            'maths': maths,
        }
        return render_template('ejercicio5/result.html', args = contexto)

if __name__ == "__main":
    app.run()
