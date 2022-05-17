####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen Certificatif
###  Nom: Simon Lacaille
###  Numéro étudiant: 2129107
###  Description du fichier: classe fille de document
###  Travail basé sur l'exercice_Interface_graphique_Propriété de Hasna Hocini surtout méthode d'annotation
####################################################################################

from Document import *

"""
import la classe mère
"""


class Film(Document):
    """
    classe Film qui fait parti de la classe document
    """

    ###################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ###################################

    def __init__(self, p_code_de_document="", p_titre="", p_nb_de_rangee=0,
                 p_genre="", p_acteur_principal="", p_realisateur=""):
        """
                     méthode constructeur avec paramètre de défaut
                     définie les différents attributs des films
        """
        Document.__init__(self, p_code_de_document, p_titre, p_nb_de_rangee)  # Appel constructeur classe document
        self.__genre = p_genre
        self.__acteur_principal = p_acteur_principal
        self.__realisateur = p_realisateur

        ##################################################
        ####   Propriétés, accesseurs et mutateurs    ####
        ####                                          ####
        ##################################################

        # propriété genre

    def _get_genre(self):
        """
            Accès à l'attribut privée du genre
            """

        return self.__genre

    def _set_genre(self, p_genre):
        """
            mutateur de __genre
            """
        if len(p_genre) <= 100:
            self.__genre = p_genre

    genre = property(_get_genre, _set_genre)

    # propriété acteur principal
    def _get_acteur_prin(self):
        """
        Accès à l'attribut privée de l'acteur principal
        """

        return self.__acteur_principal

    def _set_acteur_prin(self, p_acteur_principal):
        """
        mutateur de __acteur_prin
        """
        if len(p_acteur_principal) <= 100:
            self.__auteur = p_acteur_principal

    acteur_principal = property(_get_acteur_prin, _set_acteur_prin)

    # propriété réalisateur
    def _get_realisateur(self):
        """
        Accès à l'attribut privée du réalisateur
        """

        return self.__realisateur

    def _set_realisateur(self, p_realisateur):
        """
        mutateur de __realisateur
        """
        if len(p_realisateur) <= 100:
            self.__auteur = p_realisateur

    realisateur = property(_get_realisateur, _set_realisateur)

    def __str__(self):
        """
                Méthode spéciale d'affichage. À utiliser avec print(objet)
                :return: Chaine à afficher
        """
        chaine_film = " " * 60 + "\n" + "*" * 60 + "\n\n" + "   Le code du document : " + self.code_document + "\n" + \
                      "   Le titre du film : " + self.titre + "\n" + \
                      "   Le nombre de la rangée : " + str(self.Nb_de_rangee) + "\n" + \
                      "   Le genre du film : " + self.genre + "\n" + \
                      "   L'acteur principal du film : " + self.acteur_principal + "\n" + \
                      "   Le réalisateur du film: " + self.realisateur + "\n" + \
                      "\n" + "*" * 60
        return chaine_film
