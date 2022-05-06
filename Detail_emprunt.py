####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen Certificatif
###  Nom: Simon Lacaille
###  Numéro étudiant: 2129107
###  Description du fichier: classe emprunt
###  Travail basé sur l'exercice_Interface_graphique_Propriété de Hasna Hocini surtout méthode d'annotation
####################################################################################
class Detail_emprunt:
    """
    classe detail Emprunt
    """

    ###################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ###################################

    def __init__(self,p_code_emprunt = "",p_qte_copie = 0,p_duree_emprunt = "",p_document = ""):
        """
             méthode constructeur avec paramètre de défaut
             définie les différents attributs de les détail d'emprunt
        """
        self.__code_emprunt = p_code_emprunt
        self.document = p_document
        self.duree = p_duree_emprunt
        self.__copie = p_qte_copie

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

    def _get_qte_copie(self):
        """
        Accès à l'attribut privée qté de copie
        """

        return self.__copie

    def _set_qte_copie(self, p_qte_copie):
        """
        mutateur de __qte_copie
        """
        if p_qte_copie >= 0 or p_qte_copie <= 3:
            self.__copie = p_qte_copie

    qte_copie = property(_get_qte_copie, _set_qte_copie)

    def __str__(self):
        """
                Méthode spéciale d'affichage. À utiliser avec print(objet)
                :return: Chaine à afficher
        """
        chaine_det_emprunt = " " * 60 + "\n" + "*" * 60 + "\n\n" + "   Le code de l'emprunt : " + self.code_emprunt + "\n" + \
                      "   La quantité de copie : " + str(self.qte_copie) + "\n" + \
                      "   La durée de l'emprunt: " + self.duree + "\n" + \
                      "   Le doccument: " + self.document + "\n" + \
                      "\n" + "*" * 60
        return chaine_det_emprunt