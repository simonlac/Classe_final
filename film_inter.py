# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'film.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Film(object):
    def setupUi(self, Film):
        Film.setObjectName("Film")
        Film.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Film)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_ajout_film = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ajout_film.setGeometry(QtCore.QRect(230, -10, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_ajout_film.setFont(font)
        self.lbl_ajout_film.setObjectName("lbl_ajout_film")
        self.label_erreur_nb_rangee_film = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_nb_rangee_film.setEnabled(True)
        self.label_erreur_nb_rangee_film.setGeometry(QtCore.QRect(20, 220, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_nb_rangee_film.setFont(font)
        self.label_erreur_nb_rangee_film.setObjectName("label_erreur_nb_rangee_film")
        self.lineEdit_genre = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_genre.setGeometry(QtCore.QRect(480, 50, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_genre.setFont(font)
        self.lineEdit_genre.setObjectName("lineEdit_genre")
        self.label_erreur_code_inv_film = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_code_inv_film.setEnabled(True)
        self.label_erreur_code_inv_film.setGeometry(QtCore.QRect(10, 120, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_code_inv_film.setFont(font)
        self.label_erreur_code_inv_film.setObjectName("label_erreur_code_inv_film")
        self.pushButton_quitter_film = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quitter_film.setGeometry(QtCore.QRect(680, 520, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_quitter_film.setFont(font)
        self.pushButton_quitter_film.setObjectName("pushButton_quitter_film")
        self.lineEdit_nb_rangee_film = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nb_rangee_film.setGeometry(QtCore.QRect(10, 170, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_nb_rangee_film.setFont(font)
        self.lineEdit_nb_rangee_film.setObjectName("lineEdit_nb_rangee_film")
        self.label_titre_film = QtWidgets.QLabel(self.centralwidget)
        self.label_titre_film.setGeometry(QtCore.QRect(10, 240, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_titre_film.setFont(font)
        self.label_titre_film.setObjectName("label_titre_film")
        self.textBrowser_lst_film = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_lst_film.setGeometry(QtCore.QRect(200, 390, 451, 161))
        self.textBrowser_lst_film.setObjectName("textBrowser_lst_film")
        self.label_genre = QtWidgets.QLabel(self.centralwidget)
        self.label_genre.setGeometry(QtCore.QRect(480, 20, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_genre.setFont(font)
        self.label_genre.setObjectName("label_genre")
        self.label_nb_rangee_film = QtWidgets.QLabel(self.centralwidget)
        self.label_nb_rangee_film.setGeometry(QtCore.QRect(10, 140, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_nb_rangee_film.setFont(font)
        self.label_nb_rangee_film.setObjectName("label_nb_rangee_film")
        self.lineEdit_realisateur = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_realisateur.setGeometry(QtCore.QRect(480, 250, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_realisateur.setFont(font)
        self.lineEdit_realisateur.setObjectName("lineEdit_realisateur")
        self.pushButton_ajouter_film = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ajouter_film.setGeometry(QtCore.QRect(540, 330, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_ajouter_film.setFont(font)
        self.pushButton_ajouter_film.setObjectName("pushButton_ajouter_film")
        self.label_erreur_code_film = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_code_film.setGeometry(QtCore.QRect(10, 110, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreur_code_film.setFont(font)
        self.label_erreur_code_film.setObjectName("label_erreur_code_film")
        self.label_code_film = QtWidgets.QLabel(self.centralwidget)
        self.label_code_film.setGeometry(QtCore.QRect(10, 30, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_code_film.setFont(font)
        self.label_code_film.setObjectName("label_code_film")
        self.label_realisateur = QtWidgets.QLabel(self.centralwidget)
        self.label_realisateur.setGeometry(QtCore.QRect(480, 220, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_realisateur.setFont(font)
        self.label_realisateur.setObjectName("label_realisateur")
        self.label_erreur_genre = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_genre.setEnabled(True)
        self.label_erreur_genre.setGeometry(QtCore.QRect(480, 100, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_genre.setFont(font)
        self.label_erreur_genre.setObjectName("label_erreur_genre")
        self.lineEdit_film = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_film.setGeometry(QtCore.QRect(10, 270, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_film.setFont(font)
        self.lineEdit_film.setObjectName("lineEdit_film")
        self.label_erreur_annee = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_annee.setEnabled(True)
        self.label_erreur_annee.setGeometry(QtCore.QRect(480, 200, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_annee.setFont(font)
        self.label_erreur_annee.setObjectName("label_erreur_annee")
        self.lineEdit_code_film = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_code_film.setGeometry(QtCore.QRect(10, 60, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_code_film.setFont(font)
        self.lineEdit_code_film.setObjectName("lineEdit_code_film")
        self.label_erreur_realisateur = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_realisateur.setEnabled(True)
        self.label_erreur_realisateur.setGeometry(QtCore.QRect(490, 300, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_realisateur.setFont(font)
        self.label_erreur_realisateur.setObjectName("label_erreur_realisateur")
        self.lineEdit_acteur_prin = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_acteur_prin.setGeometry(QtCore.QRect(480, 150, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_acteur_prin.setFont(font)
        self.lineEdit_acteur_prin.setObjectName("lineEdit_acteur_prin")
        self.label_acteur_prin = QtWidgets.QLabel(self.centralwidget)
        self.label_acteur_prin.setGeometry(QtCore.QRect(480, 120, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_acteur_prin.setFont(font)
        self.label_acteur_prin.setObjectName("label_acteur_prin")
        self.pushButton_suppriemer_film = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_suppriemer_film.setGeometry(QtCore.QRect(140, 330, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_suppriemer_film.setFont(font)
        self.pushButton_suppriemer_film.setObjectName("pushButton_suppriemer_film")
        self.pushButton_modifier_film = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_modifier_film.setGeometry(QtCore.QRect(340, 330, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_modifier_film.setFont(font)
        self.pushButton_modifier_film.setObjectName("pushButton_modifier_film")
        Film.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Film)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Film.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Film)
        self.statusbar.setObjectName("statusbar")
        Film.setStatusBar(self.statusbar)

        self.retranslateUi(Film)
        QtCore.QMetaObject.connectSlotsByName(Film)

    def retranslateUi(self, Film):
        _translate = QtCore.QCoreApplication.translate
        Film.setWindowTitle(_translate("Film", "MainWindow"))
        self.lbl_ajout_film.setText(_translate("Film", "Ajout de film"))
        self.label_erreur_nb_rangee_film.setText(_translate("Film", "<html><head/><body><p><span style=\" color:#ff0000;\">le numéro de rangée est invalide.</span></p></body></html>"))
        self.label_erreur_code_inv_film.setText(_translate("Film", "<html><head/><body><p><span style=\" color:#ff0000;\">Le code de film est invalide.</span></p></body></html>"))
        self.pushButton_quitter_film.setText(_translate("Film", "Quitter"))
        self.label_titre_film.setText(_translate("Film", "Titre du film"))
        self.label_genre.setText(_translate("Film", "genre"))
        self.label_nb_rangee_film.setText(_translate("Film", "nombre de rangée"))
        self.pushButton_ajouter_film.setText(_translate("Film", "Ajouter"))
        self.label_erreur_code_film.setText(_translate("Film", "<html><head/><body><p><span style=\" color:#ff0000;\">le code de film existe déjà.</span></p></body></html>"))
        self.label_code_film.setText(_translate("Film", "code de film"))
        self.label_realisateur.setText(_translate("Film", "réalisateur"))
        self.label_erreur_genre.setText(_translate("Film", "<html><head/><body><p><span style=\" color:#ff0000;\">genre invalide.</span></p></body></html>"))
        self.label_erreur_annee.setText(_translate("Film", "<html><head/><body><p><span style=\" color:#ff0000;\">acteur principal invalide.</span></p></body></html>"))
        self.label_erreur_realisateur.setText(_translate("Film", "<html><head/><body><p><span style=\" color:#ff0000;\">réalisateur invalide.</span></p></body></html>"))
        self.label_acteur_prin.setText(_translate("Film", "Acteur Principal"))
        self.pushButton_suppriemer_film.setText(_translate("Film", "supprimer"))
        self.pushButton_modifier_film.setText(_translate("Film", "modifier"))