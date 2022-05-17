####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen Certificatif
###  Nom: Simon Lacaille
###  Numéro étudiant: 2129107
###  Description du fichier: classe emprunt
###  Travail basé sur l'exercice_Interface_graphique_Propriété de Hasna Hocini surtout méthode d'annotation
####################################################################################
class Emprunt:
    """
    classe Emprunt
    """

    ###################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ###################################

    def __init__(self,p_code_emprunt = "",p_date_emprunt= "",p_list_detail = "",p_abonner = ""):
        """
             méthode constructeur avec paramètre de défaut
             définie les différents attributs de l'emprunt
        """
        self.__code_emprunt = p_code_emprunt
        self.date_emprunt = p_date_emprunt
        self.list = p_list_detail
        self.abonner= p_abonner

    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ####                                          ####
    ##################################################

    def _get_code_emprunt(self):
        """
        Accès à l'attribut privée du code d'emprunt
        """

        return self.__code_emprunt

    def _set_code_emprunt(self, p_code_emprunt):
        """
        mutateur de __code emprunt
        """
        if len(p_code_emprunt) <= 50:
            self.__code_emprunt = p_code_emprunt

    code_emprunt = property(_get_code_emprunt, _set_code_emprunt)

    def __str__(self):
        """
                Méthode spéciale d'affichage. À utiliser avec print(objet)
                :return: Chaine à afficher
        """
        chaine_emprunt = " " * 60 + "\n" + "*" * 60 + "\n\n" + "   Le code de l'emprunt : " + self.code_emprunt + "\n" + \
                      "   La liste de détail: " + self.list + "\n" + \
                      "   L'abbonée: " + self.abonner + "\n" + \
                      "   La date de l'emprunt : " + str(self.date_emprunt.year()) + "-" \
                      + str(self.date_emprunt.month()) + "-" + str(self.date_emprunt.day()) + "\n\n" + "*" * 60
        return chaine_emprunt


