####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen Certificatif
###  Nom: Simon Lacaille
###  Numéro étudiant: 2129107
###  Description du fichier: classe emprunt
###  Travail basé sur l'exercice_Interface_graphique_Propriété de Hasna Hocini surtout méthode d'annotation
####################################################################################
from Abbonement import *
from Detail_emprunt import *
"""
import classe  Abbonement et Detail
"""
class Emprunt:
    """
    classe Emprunt
    """

    ###################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ###################################

    def __init__(self,p_list_detail = "",p_code_emprunt = "",p_date_emprunt= 0.0,p_abonner = ""):
        """
             méthode constructeur avec paramètre de défaut
             définie les différents attributs de l'emprunt
        """
        self.__code_emprunt = p_code_emprunt
        self.date_emprunt = p_date_emprunt
        self.list = p_list_detail
        self.abonner= p_abonner



