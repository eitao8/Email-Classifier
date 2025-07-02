from flask import Flask, render_template, request
from classifier import processar_email
from PyPDF2 import PdfReader

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/processar", methods=["POST"])
def processar():
    texto = ""
    if "emailfile" in request.files:
        file = request.files["emailfile"]
        if file.filename.endswith(".txt"):
            texto = file.read().decode("utf-8")
        elif file.filename.endswith(".pdf"):
            reader = PdfReader(file)
            texto = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])

    if not texto and "emailtexto" in request.form:
        texto = request.form["emailtexto"]

    categoria, resposta = processar_email(texto)
    return render_template("index.html", categoria=categoria, resposta=resposta, texto_original=texto)

if __name__ == "__main__":
    app.run(debug=True)
