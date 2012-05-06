#-*- coding: utf-8 -*-
#!/usr/bin/python
#--------------------------------
##  @package main
##  \brief Gère tout
##  \author Bouilly Loïc & Kerhel Jélani
##  \version 2
##  \date 27 avril 2012
##  
## 

#--------------------------------
# Importation des modules
import pyglet
from pyglet.gl import *
import pays
import drapeau
import option
import controleJeu
import texte
import deco
import fond
import menu
import bouton
import niveau
import jeu
import affichage


def init():
    """! \brief Initialisation
    \enum Liste_drapeau_niveau -> Liste contenant les drapeaux par niveaux.
    \return Liste_drapeau_niveau -> Liste
    """
    largeur,hauteur = option.window()
    window = pyglet.window.Window(largeur,hauteur)
    liste_drapeau = deco.chargement_deco_menu()
    fondImage = fond.Fond()
    Liste_niveau =  niveau.structuration_niveau()
    jeu.creation_qcm()
    controleJeu.modifierPage("menu")
    return liste_drapeau,window,fondImage,Liste_niveau

liste_drapeau,window,fondImage,Liste_niveau = init()

@window.event
def on_draw():
    window.clear()
    fondImage.blit(0,0)
    ## On lit la page dans laquelle le joueur est pour l'affiché :
    page = controleJeu.lirePage()
    ## Bouton home :
    if page != "menu" :
        bouton.bouton_home()
    if page == "menu" :
        deco.affiche_menu_drapeau(liste_drapeau,yPlus)
        menu.affiche_menu()
    elif page == "niveau":
        niveau.affiche_niveau(Liste_niveau)
    elif page == "partie":
        jeu.affichage_jeu()
@window.event
def on_mouse_press(x,y,button,modifier):
    ## On lit la page dans laquelle le joueur se trouve
    page = controleJeu.lirePage()
    if page != "menu" :
        bouton.gestionRetour(x,y)
    if page == "menu" :
        menu.mouse_menu_clic(x,y)
    elif page == "niveau":
        niveau.niveau_clique(x,y)
    elif page == "partie":
        jeu.clique_reponse(x,y,button)


def animer(dt):
            # On fait varier yPlus pour les mouvement des drapeaux
            global yPlus
            yPlus = dt + 0.02

if __name__ == "__main__" :
                    glEnable(GL_BLEND)
                    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
                    # Fonction mainloop
                    pyglet.clock.schedule_interval(animer,0.00001)
                    pyglet.app.run()
    


