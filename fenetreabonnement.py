# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer la boite de dialogue


import abonnement_inter


######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetreabonnement(QtWidgets.QDialog, abonnement_inter.Ui_Dialog):
    def __init__(self, parent=None):
        super(Fenetreabonnement, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Liste des abonnement")

    @pyqtSlot()
    def on_pushButton_quitter_abonner_clicked(self):
        self.close()

