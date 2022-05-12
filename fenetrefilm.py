# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer la boite de dialogue


import film_inter


######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetrefilm(QtWidgets.QDialog, film_inter.Ui_film):
    def __init__(self, parent=None):
        super(Fenetrefilm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Liste des film")


    @pyqtSlot()
    def on_pushButton_quitter_film_clicked(self):
        self.close()