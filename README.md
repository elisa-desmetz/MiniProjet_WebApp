# MiniProjet_WebApp
Mini-projet application web Master 1 H3 HiTeMa</br>
Application accessible à <a href="http://my-portfolio-edesmetz.herokuapp.com/">http://my-portfolio-edesmetz.herokuapp.com/</a>.
## Objectif
Mise en place de mon portfolio qui présentera :
- Mes projets
- Mon profil avec un lien vers mes réseaux sociaux
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
Redirige vers la page référencée par la variable ```url```
Dans le cas ou la variable référencée n'est pas listée, redirige vers la page "/home/"

## Ressources
### Images
Les images de type icones sont disponibles dans ```/src/img```.
Les images personnelles sont héergées en externe.
### Fichiers
Les fichiers personnels sont hébergés en externe.
