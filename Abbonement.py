####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen Certificatif
###  Nom: Simon Lacaille
###  Numéro étudiant: 2129107
###  Description du fichier: classe abonnement
###  Travail basé sur l'exercice_Interface_graphique_Propriété de Hasna Hocini surtout méthode d'annotation
####################################################################################

class Abbonement:
    """
    classe Abbonement
    """

    ###################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ###################################

    def __init__(self,p_code_abbonnement = "",p_type_abbonnement = "",p_prix= 0.0,p_duree = ""):
        """
             méthode constructeur avec paramètre de défaut
             définie les différents attributs des documents
        """
        self.__code_abbonnement = p_code_abbonnement
        self.type_abbonnement = p_type_abbonnement
        self.__prix = p_prix
        self.duree = p_duree