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

    def __init__(self,p_code_abbonnement = "",p_type_abbonnement = "",p_prix= 0.0,p_duree = "",p_date = "",p_nom = "",p_courriel_tele = ""):
        """
             méthode constructeur avec paramètre de défaut
             définie les différents attributs des documents
        """
        self.__code_abbonnement = p_code_abbonnement
        self.type_abbonnement = p_type_abbonnement
        self.__prix = p_prix
        self.duree = p_duree
        self.date = p_date
        self.__nom = p_nom
        self.__courriel_tele = p_courriel_tele

        ##################################################
        ####   Propriétés, accesseurs et mutateurs    ####
        ####                                          ####
        ##################################################

    # propriété code_abbonement

    def _get_code_abbonnement(self):
        """
        Accès à l'attribut privée du code d'abbonnement
        """

        return self.__code_abbonnement

    def _set_code_abbonnement(self, p_code_abbonnement):
        """
        mutateur de __code abbonnement
        """
        if len(p_code_abbonnement) <= 50:
            self.__code_abbonnement = p_code_abbonnement

    code_abbonnement = property(_get_code_abbonnement,_set_code_abbonnement)

    # propriété prix
    def _get_prix(self):
        """
        Accès à l'attribut privée du prix
        """

        return self.__prix

    def _set_prix(self, p_prix):
        """
        mutateur de __prix
        """
        if p_prix >= 0 or p_prix <= 60:
            self.__prix = p_prix

    prix = property(_get_prix, _set_prix)

    # propriété nom

    def _get_nom (self):
        """
        Accès à l'attribut privée du nom
        """

        return self.__nom

    def _set_nom(self, p_nom):
        """
        mutateur de __nom
        """
        if len(p_nom) <= 100:
            self.__nom = p_nom

    nom = property(_get_nom, _set_nom)

    # propriété courriel_tele

    def _get_courriel_tele(self):
        """
        Accès à l'attribut privée du courriel_tele
        """

        return self.__courriel_tele

    def _set_courriel_tele(self, p_courriel_tele):
        """
        mutateur de __courriel_tele
        """
        if len(p_courriel_tele) <= 100:
            self.__courriel_tele = p_courriel_tele

    courriel_tele = property(_get_courriel_tele, _set_courriel_tele)

    def Calculer_total(self,prix,p_duree,p_type_abbonnement):
        """
        sert à calculer le total pour le prix
        return le total de l'abbonement
        """
        total = 0
        if p_type_abbonnement == "standard":
            prix = 10.00
        elif p_type_abbonnement == "origin":
            prix = 20.00
        elif p_type_abbonnement == "deluxe":
            prix = 30.00
        total = prix
        if p_duree == "1 ans":
            total /2
        elif p_duree == "2 ans":
            total*1
        elif p_duree == "4 ans":
            total*2
        return total

    def __str__(self):
        """
                Méthode spéciale d'affichage. À utiliser avec print(objet)
                :return: Chaine à afficher
        """
        chaine_abbonnement = " " * 60 + "\n" + "*" * 60 + "\n\n" + "   Le code de l'abbonnement : " + self.code_abbonnement + "\n" + \
                      "   Le type d'abbonement : " + self.type_abbonnement + "\n" + \
                      "   Le prix : " + str(self.prix) + "\n" + \
                      "   La durée de l'abonnement: " + self.duree + "\n" + \
                      "   Le date du début de l'abbonement: " + str(self.date) + "\n" + \
                      "   Le nom de  l'abboner: " + self.nom + "\n" + \
                      "   Le courriel ou téléphone de l'abonner: " + self.courriel_tele + "\n" + \
                      "\n" + "*" * 60
        return chaine_abbonnement





