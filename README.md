# MiniProjet_WebApp
Mini-projet application web Master 1 H3 HiTeMa</br>
Application accessible � <a href="http://my-portfolio-edesmetz.herokuapp.com/">http://my-portfolio-edesmetz.herokuapp.com/</a>.
## Objectif
Mise en place de mon portfolio qui pr�sentera :
- Mes projets
- Mon profil avec un lien vers mes r�seaux sociaux
- Un formulaire de contact

## Routes disponibles
### Route "/"
Fonction ```redirection()```<br/>
Redirige vers la page "/home/"
### Route "/home/"
Fonction ```home()```</br>
Retourne la page d'accueil ```index.html```</br>
Methode : GET
### Route "/projets/"
Fonction ```projets()```</br>
Retourne la page ```projets.html```
Methode : GET
### Route "/contact/"
<i>WORK IN PROGRESS</i>
Fonction ```contact()``` </br>
Retourne la page ```contact.html```</br>
Methode : GET
### Route "/about/"
Fonction ```about()```</br>
Retourne la page ```about.html```</br>
Methode : GET
### Route "/redirect/\<string:url>/"</br>
Fonction ```redirection_externe(url)``` </b>
Redirige vers la page r�f�renc�e par la variable ```url```
Dans le cas ou la variable r�f�renc�e n'est pas list�e, redirige vers la page "/home/"