####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen Certificatif
###  Nom: Simon Lacaille
###  Numéro étudiant: 2129107
###  Description du fichier: classe abonnement
###  Travail basé sur l'exercice_Interface_graphique_Propriété de Hasna Hocini surtout méthode d'annotation
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
########+###############################

# Importer le module sys nécessaire à l'exécution.
import sys
# Pour la réinitialisation de la date dans le dateEdit
from PyQt5.QtCore import QDate, pyqtSlot

# Importer Pour le model de la listView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

# importer les interfaces graphiques
import bibliotheque
import abonnement_inter
from emprunt_inter import *
from fenetreabonnement import *
from fenetreemprunt import *
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
# code document
def verifier_document_liste(p_code_de_document):
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
def verifier_abonner_liste(p_code_abbonnement):
    """
         Vérifie si le code de l'abonner existe dans la liste des document
             :param p_code_abonnement:  le code de l'abonner
             :return: True si le code de l'abonner est trouvé dans la liste des abonners et False sinon
    """
    for elt in ls_abonner:
        if elt.p_code_abbonnement == p_code_abbonnement.capitalize():
            return True
    return False


# code emprunt
def verifier_emprunt(p_code_emprunt):
    """
         Vérifie si le code d'emprunt existe dans la liste des emprunts
             :param p_code-emprunt:  le numéro de l'emprunt
             :return: True si l'emprunt est trouvé dans la liste des emprunts et False sinon
    """
    for elt in ls_emprunt:
        if elt.code_emprunt == p_code_emprunt.capitalize():
            return True
    return False


def cacher_labels_erreur_abonner(objet):
    """
    Cacher les différents labels d'erreur abonnement
    """
    objet.label_erreur_code_abonnement.setVisible(False)
    objet.label_erreur_code_inv_abonnement.setVisible(False)
    objet.label_erreur_nom.setVisible(False)
    objet.label_erreur_code_inv_nom.setVisible(False)
    objet.label_erreur_abonnement.setVisible(False)
    objet.label_erreur_code_inv_cour_tele.setVisible(False)


def cacher_labels_erreur_emprunt(objet):
    """
    Cacher les différents labels d'erreur emprunt
    """
    objet.label_erreur_code_emprunt.setVisible(False)
    objet.label_erreur_code_inv_emprunt.setVisible(False)
    objet.label_erreur_code_inv_document_emprunt.setVisible(False)
    objet.label_erreur_code_inv_abonnement_emprunt.setVisible(False)
    objet.label_erreur_emprunt.setVisible(False)


def cacher_labels_erreur_film(objet):
    """
    Cacher les différents labels d'erreur de film
    """
    objet.label_erreur_code_film.setVisible(False)
    objet.label_erreur_code_inv_film.setVisible(False)
    objet.label_erreur_nb_rangee_film.setVisible(False)
    objet.label_erreur_genre.setVisible(False)
    objet.label_erreur_annee.setVisible(False)
    objet.label_erreur_realisateur.setVisible(False)


def cacher_labels_erreur_jeux(objet):
    """
    Cacher les différents labels d'erreur de jeux
    """
    objet.label_erreur_code_jeux.setVisible(False)
    objet.label_erreur_code_inv_jeux.setVisible(False)
    objet.label_erreur_nb_rangee_jeux.setVisible(False)
    objet.label_erreur_createur.setVisible(False)
    objet.label_erreur_nb_joueur.setVisible(False)


def cacher_labels_erreur_livre(objet):
    """
     Cacher les différents labels d'erreur de livre
    """
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
class fenetreBibliotheque(QtWidgets.QMainWindow, bibliotheque.Ui_Bibliothequecegep):
    """
    Nome de la classe : fenetreBibliotheque
    Héritages :
    - QtWidgets.QMainWindow : Type d'interface créé par QtDesigner
    - bibliotheque.Ui_MainWindow : Ma classe générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QMainWindow et bibliotheque.Ui_MainWindow
        """
        # Appeler le constructeur parent avec ma classe en paramètre...
        super(fenetreBibliotheque, self).__init__(parent)
        # Préparer l'interface utilisateur
        self.setupUi(self)
        # Donner un titre à la fenêtre principale
        self.setWindowTitle("Bibliothèque du cegep de l'outaouais")

    # Bouton Afficher listview
    @pyqtSlot()
    def on_pushButton_ajouter_abonner__clicked(self):
        # Instancier une boite de dialogue FenetreListview
        dialog = Fenetreabonnement()
        # Afficher la boite de dialogue
        dialog.show()
        reply = dialog.exec_()



        # Bouton Afficher listview
    @pyqtSlot()
    def on_pushButton_ajouter_emprunt_clicked(self,dialog):
        # Instancier une boite de dialogue FenetreListview
        emprunt = Fenetreemprunt()
        # Préparer la listview
        model = QStandardItemModel()
        dialog.listView_abonnement.setModel(model)
        for e in ls_abonner:
            item = QStandardItem(
                e.code_abbonnement + " * " + e.type_abbonnement + " * " + e.prix + " * " + e.duree + " * " + e.date + " * " + e.nom + " * " + e.courriel_tele)
            model.appendRow(item)
        emprunt.listView_emprunt.setModel(model)
        for e in ls_emprunt:
            item = QStandardItem(
               e.code_emprunt + " * " + e.date_emprunt + " * " + e.list+ " * " + e.abonner)
            model.appendRow(item)
            # Afficher la boite de dialogue
        emprunt.show()
        reply = emprunt.exec_()


#################################
###### PROGRAMME PRINCIPAL ######
#################################

# Créer le main qui lance la fenêtre de Qt

def main():
    """
    Méthode main : point d'entré du programme.
    Exécution de l'applicatin avec l'interface graphique.
    reply = Dialog.exec_()
    """
    # Instancier une application et une fenetre principale
    app = QtWidgets.QApplication(sys.argv)
    form = fenetreBibliotheque()
    # Afficher la fenêtre principale
    form.show()
    # Lancer l'application
    app.exec()


if __name__ == "__main__":
    main()
