# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for, request
from flask import render_template
import os
from markupsafe import escape
app = Flask(__name__)
port = int(os.environ.get("PORT",5000))


# Gestion routing interne
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
def projets():
    """
    Affiche la page des projets
    """
    return render_template("projets.html")
@app.route('/contact/')
def contact():
    """
    Affiche la page de contact
    """
    return render_template("contact.html")

@app.route('/about/')
def about():
    """
    Affiche la page "A propos"
    """
    return render_template("about.html")

@app.route('/redirect/<string:url>')
def redirection_externe(url=None):
    """
    Redirige vers une URL externe en fonction du paramètre d'entrée
    """
    url = url
    if url=="heroku":
        return redirect("https://www.heroku.com/")
    elif url=="flask":
        return redirect("https://flask.palletsprojects.com/en/1.1.x/")
    elif url=="docker":
        return redirect("https://www.docker.com/")
    elif url=="bootstrap":
        return redirect("https://getbootstrap.com/")
    elif url=="jinja":
        return redirect("https://jinja.palletsprojects.com/en/2.11.x/")
    elif url=="projet-1":
        return redirect("https://hatespeech-streamlit-app.herokuapp.com/")
    if url=="github":
        return redirect("https://github.com/elisa-desmetz")
    if url=="linkedin":
        return redirect("https://www.linkedin.com/in/elisa-desmetz/")
    if url=="cv":
        return redirect("https://www.aht.li/3568204/Desmetz_Elisa_CV.pdf")
    if url=="git-1":
        return redirect("https://github.com/elisa-desmetz/StreamlitApp_AlgoSentiment")
    else :
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)