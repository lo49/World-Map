#-*- coding: utf-8 -*-
#!/usr/bin/python
#--------------------------------
##  @package drapeau
##  \brief Permet la gestion des boutons 
##  \author Bouilly Loïc & Kerhel Jélani
##  \version 2
##  \date 27 avril 2012
##  
## 

#--------------------------------
# Importation des modules
import pyglet
import random
import pays

# Fonction aléatoire :
def randint(n):
    """! \brief Fonction aléatoire
	     Permet de générer un nombre aléatoire compris entre 0 et n
	     \param[in] n type entier
	     \return nombre_aleatoire
	"""
    nombre_aleatoire = int(n*random.random())
    return nombre_aleatoire  

def afficher(sprite,x,y):
    """! \brief Cela permet d'afficher le bouton sur la fenêtre au coordonnée x,y
    \param[in] sprite,x,y -> sprite,entier,entier
    \return None
    """
    sprite.blit(x,y)
    return None
def creer_liste_aleatoire_drapeau(drapeauMin,drapeauMax):
	"""! \brief Cela permet de créer une liste des pays aléatoirement.
	Cette fonction à pour but de créer une liste de nombre correspondant au numéros de pays. Mis aléatoriement dans la liste et compris entre drapeauMin et drapeauMax.
	elle servirat surtout pour l'élaboration des niveaux.
	\param[in] drapeauMin,drapeauMax -> Entier,Entier
	\return liste_drapeau -> Liste
	"""
	liste_drapeau = []
	k = 0
	i = drapeauMax - drapeauMin 
	while k < i :
		# On prend un pays aléatoirement parmis les drapeau_fin:
		nombre_pays = randint(int(drapeauMax))
		while nombre_pays < int(drapeauMin):
			nombre_pays = randint(int(drapeauMax))
		if k== 0 :
			liste_drapeau.append(nombre_pays)
			k += 1
		elif nombre_pays in liste_drapeau :
			k = k
		else :
			liste_drapeau.append(nombre_pays)
			k += 1
	return liste_drapeau
            
def image_drapeau(nbr_pays):
    """! \brief Permet d'aller rechercher l'image du drapeaux
    \param[in] nbr_pays -> entier
    \return drapeau -> Sprite
    """
    ### On va chercher le nom du fichier représentant l'image du drapeau :
    nom_image = pays.liste_drapeaux(nbr_pays)
    drapeau = pyglet.image.load("../data/texture/drapeaux/"+nom_image)
    return drapeau
		
	
	

