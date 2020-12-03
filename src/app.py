from flask import Flask, redirect, url_for, request
from flask import render_template
import os
from markupsafe import escape
app = Flask(__name__)
port = int(os.environ.get("PORT",5000))

@app.route('/')
def redirection():
    """
    Redirige depuis / jusqu'à la page d'accueil "Home"
    """
    return redirect(url_for('home'))
@app.route('/home/')
def home():
    """
    Affiche la page d'accueil
    """
    return render_template("index.html")

@app.route('/projets/')
@app.route('/projets/projet-1/')
@app.route('/projets/projet-2/')
@app.route('/projets/projet-3/')
def projets():
    """
    Affiche la page des projets
    """
    return render_template("projets.html")

@app.route('/contact/')
def aze():
    """
    Affiche la page de contact
    """
    return render_template("main.html")

@app.route('/about/')
def zer():
    """
    Affiche la page "A propos"
    """
    return render_template("main.html")

@app.route('/redirect-heroku/')
def redirection_heroku():
    """
    Redirige vers le site de Heroku
    """
    return redirect("https://www.heroku.com/")
@app.route('/redirect-flask/')
def redirection_flask():
    """
    Redirige vers le site de Flask
    """
    return redirect("https://flask.palletsprojects.com/en/1.1.x/")
@app.route('/redirect-docker/')
def redirection_docker():
    """
    Redirige vers le site de docker
    """
    return redirect("https://www.docker.com/")
@app.route('/redirect-bootstrap/')
def redirection_bootstrap():
    """
    Redirige vers le site de Bootstrap
    """
    return redirect("https://getbootstrap.com/")
@app.route('/redirect-jinja/')
def redirection_jinja():
    """
    Redirige vers le site de jinja
    """
    return redirect("https://jinja.palletsprojects.com/en/2.11.x/")

@app.route('/favicon.ico')
def favicon():
    """
    Récupère le chemin d'accès de la favicon
    """
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)