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
import fenetreabonnement
from emprunt_inter import *
from fenetreabonnement import *
from fenetrelivre import *
from fenetreemprunt import *
from fenetrejeux import *
from fenetrefilm import *
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
ls_livre = []
ls_jeux = []
ls_film = []
ls_emprunt = []


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

    # Bouton aller dialogue abonner
    @pyqtSlot()
    def on_pushButton_ajouter_abonner__clicked(self):
        # Instancier une boite de dialogue Fenetreabonner
        dialog = Fenetreabonnement()
        # Afficher la boite de dialogue
        dialog.show()
        reply = dialog.exec_()



    # Bouton aller dialogue emprunt
    @pyqtSlot()
    def on_pushButton_ajouter_emprunt_clicked(self):
        # Instancier une boite de dialogue Fenetreemprunt
        emprunt = Fenetreemprunt()
        # Préparer la listview
        # Afficher la boite de dialogue
        emprunt.show()
        reply = emprunt.exec_()

      # Bouton aller dialogue jeux
    @pyqtSlot()
    def on_pushButton_ajouter_doc_clicked(self):
        # Instancier une boite de dialogue Fenetre jeux
        jeux = Fenetrejeux()
        # Afficher la boite de dialogue
        jeux.show()
        reply = jeux.exec_()

    # Bouton aller dialogue livre
    @pyqtSlot()
    def on_pushButton_ajouter_livre_clicked(self):
        # Instancier une boite de dialogue Fenetre livre
        livre = Fenetrelivre()
        # Afficher la boite de dialogue
        livre.show()
        reply = livre.exec_()



    # Bouton aller dialogue film
    @pyqtSlot()
    def on_pushButton_ajouter_film_clicked(self):
        # Instancier une boite de dialogue  fenentre film
        film = Fenetrefilm()
        # Afficher la boite de dialogue
        film.show()
        reply = film.exec_()




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
