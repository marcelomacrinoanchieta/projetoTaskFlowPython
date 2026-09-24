from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    projetos = ["App mobile da Cantina", "API de Pagamentos"]
    return render_template("index.html", projetos=projetos)

@app.route("/ola/<nome>")
def ola(nome):
    return f"Olá, {nome}! Bem-vindo ao TaskFlow."

