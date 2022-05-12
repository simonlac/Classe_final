# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer la boite de dialogue


import jeux_inter


######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetrejeux(QtWidgets.QDialog, jeux_inter.Ui_jeux):
    def __init__(self, parent=None):
        super(Fenetrejeux, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Liste des jeux")


    @pyqtSlot()
    def on_pushButton_quitter_jeux_clicked(self):
        self.close()