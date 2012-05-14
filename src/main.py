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
import pays,tHelp
import drapeau
import option
import option_config
import controleJeu
import texte
import deco
import fond
import menu
import bouton
import niveau
import jeu
import affichage
import niveau_fini


def init():
    """! \brief Initialisation
    \enum Liste_drapeau_niveau -> Liste contenant les drapeaux par niveaux.
    \return Liste_drapeau_niveau -> Liste
    """
    largeur,hauteur = option.window()
    window = pyglet.window.Window(largeur,hauteur)
    #window = pyglet.window.Window()
    icon1 = pyglet.image.load('../data/texture/image/16x16.png')
    icon2 = pyglet.image.load('../data/texture/image/32x32.png')
    window.set_icon(icon1, icon2)
    liste_drapeau = deco.chargement_deco_menu()
    fondImage = fond.Fond()
    Liste_niveau =  niveau.structuration_niveau()
    jeu.creation_qcm()
    controleJeu.modifierPage("menu")
    global drapeau_help
    drapeau_help = tHelp.Help()
    global player
    player = pyglet.media.Player()
    #music1 = pyglet.media.load("../data/son/music_01.mp3")
    #player.queue(music1)
    Largeur_fenetre,Longueur_fenetre,ON_OFF_musique,ON_OFF_son = option_config.lecture_option()
    if ON_OFF_musique == True :
        player.play()
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
    elif page == "option":
        option_config.option_affichage()
    elif page =="niveau_fini":
        niveau_fini.affiche()
    elif page == "help" :
        drapeau_help.affiche_drapeau()        
        
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
    elif page == "option" :
        option_config.option_clique(x,y,button,player)
    elif page == "niveau_fini" :
        pass
@window.event
def on_mouse_motion(x,y,dx,dy):
    page = controleJeu.lirePage()
    if page == "help":
        drapeau_help.vitesse_modifie(x,y)
    elif page == "menu":
        menu.mouse_motion(x,y)
@window.event
def on_key_press(key,moddifier):
    page = controleJeu.lirePage()
    if page == "niveau_fini":
        niveau_fini.clavier_pseudo(key)
def animer(dt):
            # On fait varier yPlus pour les mouvement des drapeaux
            global yPlus
            yPlus = dt + 0.02


if __name__ == "__main__" :
                    pyglet.clock.get_fps()
                    glEnable(GL_BLEND)
                    #glEnable(GL_DEPTH_TEST)
                    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
                    # Fonction mainloop
                    pyglet.clock.schedule_interval(animer,0.00001)
                    pyglet.app.run()
    


