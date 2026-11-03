from flask import Flask, render_template
 
app = Flask(__name__)
 
 
@app.route("/")
def index():
    projetos = ["App Mobile da Cantina", "API de Pagamentos"]
    return render_template("index.html", projetos=projetos)

@app.route("/sobre")
def sobre():
    sobre = ["Sou um desenvolvedor apaixonado por tecnologia e inovação.",
             "O meu grupo sou eu e Deus",
             "Tenho experiência em desenvolvimento web e mobile, e estou sempre buscando aprender novas tecnologias.",]
    return render_template("sobre.html", sobre=sobre)
