# ISSUE TRACKING SYSTEM

## Application qui permet de remonter et de suivre des problémes techniques


* ### Prérequis
	- il faut installer un Shell sur votre ordinateur, sinon vous pouvez utiliser le terminal préinstallé avec votre système d'exploitation:

	- WINDOWS:
		-  touche Windows + R puis tapez 'cmd' puis ENTRER 

	- MAC:
		- Cliquez sur l’icône Launchpad dans le Dock, saisissez Terminal dans le champ de recherche, puis cliquez sur Terminal.
		- Dans le Finder, ouvrez le dossier /Applications/Utilitaires, puis cliquez deux fois sur Terminal.
	 
	- LINUX: 
		- ctrl + alt + t

* ### Démarrage
	- télécharger l'application: https://github.com/oussamaabid82/softdesk/tree/main/projet.
	- Démarrer votre terminal et diriger vous dans le dossier télécharger (projet).
    - Créer un environnement virtuel en tapant dans votre terminal:
        ```bash
        python -m venv venv
        ```
    - Activer l'environnement en tapant dans votre terminal:
        ```bash
        source venv/Scripts/activate
        ```
	- Installez Django et les modules nécessaires pour le bon fonctionnement du programme
		```bash
		pip install -r requirements.txt
		```
	- Créer la migration des models dans la base des données en tapant dans votre terminal:
		```bash
		python manage.py migrate
	```

* ### Lancement du projet
	- Démarrer le serveur en tapant dans votre terminal:
		```bash
		python manage.py runserver
		```
    - Ouvrez votre navigateur web et taper http://127.0.0.1:8000/signup dans la barre d'adresse pour pour créer un compte.
	- taper http://127.0.0.1:8000/login dans la barre d'adresse pour vous connectez.

## N.B : POUR POUVOIR UTILISER CETTE API IL FAUT BIEN SE CONNECTER AVEC UN NOM D'UTILISATEUR ET UN MOT DE PASSE

## Postman
- [Documentations Postman](https://documenter.getpostman.com/view/18701507/UVz1Psxk)
    
* ### Fabriqué avec
	- [Django-rest-framwork](https://www.django-rest-framework.org/)
	- [VSCode](https://code.visualstudio.com/) 
	- [Cygwin](https://www.cygwin.com/install.html)

* ### Versions
	- Bêta

* ### Auteurs
	- Abid Oussama:
 
	 [oussamaabidd@gmail.com](oussamaabidd@gmail.com)

	- Mr Williams De Souza
