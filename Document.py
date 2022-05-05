####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen Certificatif
###  Nom: Simon Lacaille
###  Numéro étudiant: 2129107
###  Description du fichier: classe mère de documentation
###  Travail basé sur l'exercice_Interface_graphique_Propriété de Hasna Hocini surtout méthode d'annotation
####################################################################################

class Document:
    """
    classe
    classe document

    """

    ###################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ###################################
    def __init__(self,p_code_de_document = "",p_titre = "",p_nb_de_rangee = 0):
        """
             méthode constructeur avec paramètre de défaut
             définie les différents attributs des documents
        """
        self.__code_document = p_code_de_document
        self.titre = p_titre
        self.__nb_rangee = p_nb_de_rangee

     ##################################################
     ####   Propriétés, accesseurs et mutateurs    ####
     ####                                          ####
     ##################################################

#propriété du code du document
    def _get_code_document(self):
        """
        Accès à l'attribut privée du code du document
        """

        return self.__code_document

    def _set_code_document(self,p_code_de_document):
        """
        mutateur de __code_document
        """
        if len(p_code_de_document)<= 25:
            self.__code_document = p_code_de_document

    code_document = property(_get_code_document,_set_code_document)
      #propriété nb_de_rangée
    def _get_nb_de_rangee(self):
        """
        Accès à l'attribut privée du nb_de_rangee
        """

        return self.__nb_rangee

    def _set_nb_de_rangee(self, p_nb_de_rangee):
        """
        mutateur de __nb_rangee
        """
        if p_nb_de_rangee >= 0 or p_nb_de_rangee <=100:
            self.__nb_rangee = p_nb_de_rangee

    nb_de_rangee = property(_get_nb_de_rangee,_set_nb_de_rangee)

