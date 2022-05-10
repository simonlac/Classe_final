####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen Certificatif
###  Nom: Simon Lacaille
###  Numéro étudiant: 2129107
###  Description du fichier: classe abonnement
###  Travail basé sur l'exercice_Interface_graphique_Propriété de Hasna Hocini surtout méthode d'annotation
####################################################################################


####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Exercice 1 - Interface graphique
###  Nom: Hasna Hocini
###  No étudiant: 123456
###  No Groupe:
###  Description du fichier: Programme principal
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
########+###############################

# Importer le module sys nécessaire à l'exécution.
import sys
# Pour la réinitialisation de la date dans le dateEdit
from PyQt5.QtCore import QDate

# Importer Pour le model de la listView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

# importer les interfaces graphiques
import bibliotheque_prin
from abonnement_inter import *
from emprunt_inter import *
from livre_inter import *
from jeux_inter import *
from film_inter import *

# Importer les classes
from Detail_emprunt import *
from Abbonement import *
from Document import *
from Emprunt import *
from Film import *
from Jeux import *
from Livre import *

##########################################################
###  DÉCLARATIONS ET INITIALISATIONS - Portée globale  ###
##########################################################

# Déclarer les listes
ls_abonner = []
ls_document = []
ls_emprunt = []
ls_livre = []
ls_jeux = []
ls_film = []

#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################
#code document
def verifier_livre_liste(p_code_de_document):
    """
         Vérifie si le code de document existe dans la liste des document
             :param p_code_de_document:  le code de document
             :return: True si lecode de document est trouvé dans la liste des documents et False sinon
    """
    for elt in ls_document and ls_livre and ls_film and ls_jeux:
        if elt.code_document == p_code_de_document.capitalize():
            return True
    return False
# code abonnement
def verifier_abonner(p_code_abbonnement):
    """
         Vérifie si l'abonner existe dans la liste des abonner
             :param p_code-abonnement:  le numéro de l,abonner
             :return: True si l'abonner est trouvé dans la liste des abonner et False sinon
    """
    for elt in ls_abonner:
        if elt.code_abbonnement == p_code_abbonnement.capitalize():
            return True
    return False
# code emprunt
def verifier_emprunt(p_code_emprunt ):
    """
         Vérifie si le code d'emprunt existe dans la liste des emprunts
             :param p_code-emprunt:  le numéro de l'emprunt
             :return: True si l'emprunt est trouvé dans la liste des emprunts et False sinon
    """
    for elt in ls_emprunt:
        if elt.code_emprunt == p_code_emprunt.capitalize():
            return True
    return False

def cacher_labels_erreur(objet):
    """
    Cacher les différents labels d'erreur abonnement
    """
    objet.label_erreur_code_abonnement.setVisible(False)
    objet.label_erreur_code_inv_abonnement.setVisible(False)
    objet.label_erreur_nom.setVisible(False)
    objet.label_erreur_code_inv_nom.setVisible(False)
    objet.label_erreur_abonnement.setVisible(False)
    objet.label_erreur_code_inv_cour_tele.setVisible(False)
# emprunt
    objet.label_erreur_code_emprunt.setVisible(False)
    objet.label_erreur_code_inv_emprunt.setVisible(False)
    objet.label_erreur_code_inv_document_emprunt.setVisible(False)
    objet.label_erreur_code_inv_abonnement_emprunt.setVisible(False)
    objet.label_erreur_emprunt.setVisible(False)
# film
    objet.label_erreur_code_film.setVisible(False)
    objet.label_erreur_code_inv_film.setVisible(False)
    objet.label_erreur_nb_rangee_film.setVisible(False)
    objet.label_erreur_genre.setVisible(False)
    objet.label_erreur_annee.setVisible(False)
    objet.label_erreur_realisateur.setVisible(False)
# jeux
    objet.label_erreur_code_jeux.setVisible(False)
    objet.label_erreur_code_inv_jeux.setVisible(False)
    objet.label_erreur_nb_rangee_jeux.setVisible(False)
    objet.label_erreur_createur.setVisible(False)
    objet.label_erreur_nb_joueur.setVisible(False)
# livre
    objet.label_erreur_code.setVisible(False)
    objet.label_erreur_code_inv.setVisible(False)
    objet.label_erreur_nb_rangee.setVisible(False)
    objet.label_erreur_auteur.setVisible(False)
    objet.label_erreur_annee.setVisible(False)


########################################################
###### DÉFINITIONS DE LA CLASSE fenetrePrincipale ######
########################################################
# Créer une classe qui hérite de Qt et de notre ui.
# Nom de ma classe (fenetrePrincipal)          # Nom de mon fichier ui
class fenetreBibliotheque(QtWidgets.QMainWindow, bibliotheque.Ui.Ui_MainWindow):
    """
    Nome de la classe : fenetreBibliotheque
    Héritages :
    - QtWidgets.QMainWindow : Type d'interface créé par QtDesigner
    - bibliotheque.Ui_MainWindow : Ma classe générée avec QtDesigner
    """
    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QMainWindow et interfacegraphique.Ui_MainWindow
        """
        # Appeler le constructeur parent avec ma classe en paramètre...
        super(fenetrePrincipale, self).__init__(parent)
        # Préparer l'interface utilisateur
        self.setupUi(self)
        # Donner un titre à la fenêtre principale
        self.setWindowTitle("Gestion de scolarité")
        # Cacher tous les labels d'erreur
        cacher_labels_erreur(self)

    # Utiliser le décorateur ici pour empêcher que le code du gestionnaire d'événement du bouton ne s'éxecute deux fois
    @pyqtSlot()