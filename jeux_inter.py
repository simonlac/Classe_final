# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jeux.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_erreur_createur = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_createur.setEnabled(True)
        self.label_erreur_createur.setGeometry(QtCore.QRect(490, 80, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_createur.setFont(font)
        self.label_erreur_createur.setObjectName("label_erreur_createur")
        self.label_titre_jeux = QtWidgets.QLabel(self.centralwidget)
        self.label_titre_jeux.setGeometry(QtCore.QRect(30, 240, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_titre_jeux.setFont(font)
        self.label_titre_jeux.setObjectName("label_titre_jeux")
        self.lineEdit_createur = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_createur.setGeometry(QtCore.QRect(490, 30, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_createur.setFont(font)
        self.lineEdit_createur.setObjectName("lineEdit_createur")
        self.label_code_jeux = QtWidgets.QLabel(self.centralwidget)
        self.label_code_jeux.setGeometry(QtCore.QRect(20, 30, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_code_jeux.setFont(font)
        self.label_code_jeux.setObjectName("label_code_jeux")
        self.lineEdit_code_jeux = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_code_jeux.setGeometry(QtCore.QRect(20, 60, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_code_jeux.setFont(font)
        self.lineEdit_code_jeux.setObjectName("lineEdit_code_jeux")
        self.pushButton_quitter_jeux = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quitter_jeux.setGeometry(QtCore.QRect(690, 520, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_quitter_jeux.setFont(font)
        self.pushButton_quitter_jeux.setObjectName("pushButton_quitter_jeux")
        self.label_nb_joueur = QtWidgets.QLabel(self.centralwidget)
        self.label_nb_joueur.setGeometry(QtCore.QRect(490, 90, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_nb_joueur.setFont(font)
        self.label_nb_joueur.setObjectName("label_nb_joueur")
        self.label_erreur_nb_rangee_jeux = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_nb_rangee_jeux.setEnabled(True)
        self.label_erreur_nb_rangee_jeux.setGeometry(QtCore.QRect(30, 220, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_nb_rangee_jeux.setFont(font)
        self.label_erreur_nb_rangee_jeux.setObjectName("label_erreur_nb_rangee_jeux")
        self.lineEdit_nb_rangee_jeux = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nb_rangee_jeux.setGeometry(QtCore.QRect(20, 170, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_nb_rangee_jeux.setFont(font)
        self.lineEdit_nb_rangee_jeux.setObjectName("lineEdit_nb_rangee_jeux")
        self.label_createur = QtWidgets.QLabel(self.centralwidget)
        self.label_createur.setGeometry(QtCore.QRect(490, 0, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_createur.setFont(font)
        self.label_createur.setObjectName("label_createur")
        self.label_nb_rangee_jeux = QtWidgets.QLabel(self.centralwidget)
        self.label_nb_rangee_jeux.setGeometry(QtCore.QRect(20, 140, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_nb_rangee_jeux.setFont(font)
        self.label_nb_rangee_jeux.setObjectName("label_nb_rangee_jeux")
        self.label_erreur_code_jeux = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_code_jeux.setGeometry(QtCore.QRect(20, 110, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreur_code_jeux.setFont(font)
        self.label_erreur_code_jeux.setObjectName("label_erreur_code_jeux")
        self.lineEdit_jeux = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_jeux.setGeometry(QtCore.QRect(30, 270, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_jeux.setFont(font)
        self.lineEdit_jeux.setObjectName("lineEdit_jeux")
        self.label_erreur_code_inv_jeux = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_code_inv_jeux.setEnabled(True)
        self.label_erreur_code_inv_jeux.setGeometry(QtCore.QRect(20, 120, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_code_inv_jeux.setFont(font)
        self.label_erreur_code_inv_jeux.setObjectName("label_erreur_code_inv_jeux")
        self.pushButton_ajouter_jeux = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ajouter_jeux.setGeometry(QtCore.QRect(150, 330, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_ajouter_jeux.setFont(font)
        self.pushButton_ajouter_jeux.setObjectName("pushButton_ajouter_jeux")
        self.textBrowser_lst_jeux = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_lst_jeux.setGeometry(QtCore.QRect(210, 390, 451, 161))
        self.textBrowser_lst_jeux.setObjectName("textBrowser_lst_jeux")
        self.label_type_jeu = QtWidgets.QLabel(self.centralwidget)
        self.label_type_jeu.setGeometry(QtCore.QRect(490, 190, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_type_jeu.setFont(font)
        self.label_type_jeu.setObjectName("label_type_jeu")
        self.label_erreur_nb_joueur = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_nb_joueur.setEnabled(True)
        self.label_erreur_nb_joueur.setGeometry(QtCore.QRect(490, 170, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_nb_joueur.setFont(font)
        self.label_erreur_nb_joueur.setObjectName("label_erreur_nb_joueur")
        self.lineEdit_nb_joueur = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nb_joueur.setGeometry(QtCore.QRect(490, 120, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_nb_joueur.setFont(font)
        self.lineEdit_nb_joueur.setObjectName("lineEdit_nb_joueur")
        self.lbl_ajout_jeu = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ajout_jeu.setGeometry(QtCore.QRect(240, -10, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_ajout_jeu.setFont(font)
        self.lbl_ajout_jeu.setObjectName("lbl_ajout_jeu")
        self.comboBox_jeu = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_jeu.setGeometry(QtCore.QRect(490, 220, 261, 91))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_jeu.setFont(font)
        self.comboBox_jeu.setObjectName("comboBox_jeu")
        self.comboBox_jeu.addItem("")
        self.comboBox_jeu.addItem("")
        self.comboBox_jeu.addItem("")
        self.pushButton_modifier_jeux_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_modifier_jeux_2.setGeometry(QtCore.QRect(330, 330, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_modifier_jeux_2.setFont(font)
        self.pushButton_modifier_jeux_2.setObjectName("pushButton_modifier_jeux_2")
        self.pushButton_supprimer_jeux = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_supprimer_jeux.setGeometry(QtCore.QRect(510, 330, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_supprimer_jeux.setFont(font)
        self.pushButton_supprimer_jeux.setObjectName("pushButton_supprimer_jeux")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_erreur_createur.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">créateur invalide.</span></p></body></html>"))
        self.label_titre_jeux.setText(_translate("MainWindow", "Titre du jeux"))
        self.label_code_jeux.setText(_translate("MainWindow", "code de jeux"))
        self.pushButton_quitter_jeux.setText(_translate("MainWindow", "Quitter"))
        self.label_nb_joueur.setText(_translate("MainWindow", "nombre de joueur"))
        self.label_erreur_nb_rangee_jeux.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">le numéro de rangée est invalide.</span></p></body></html>"))
        self.label_createur.setText(_translate("MainWindow", "créateur"))
        self.label_nb_rangee_jeux.setText(_translate("MainWindow", "nombre de rangée"))
        self.label_erreur_code_jeux.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">le code de jeux existe déjà.</span></p></body></html>"))
        self.label_erreur_code_inv_jeux.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">Le code de jeux est invalide.</span></p></body></html>"))
        self.pushButton_ajouter_jeux.setText(_translate("MainWindow", "Ajouter"))
        self.label_type_jeu.setText(_translate("MainWindow", "type de jeu"))
        self.label_erreur_nb_joueur.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">nombre de joueur invalide.</span></p></body></html>"))
        self.lbl_ajout_jeu.setText(_translate("MainWindow", "Ajout de jeux"))
        self.comboBox_jeu.setItemText(0, _translate("MainWindow", "Jeu de cartes"))
        self.comboBox_jeu.setItemText(1, _translate("MainWindow", "Jeu vidéo"))
        self.comboBox_jeu.setItemText(2, _translate("MainWindow", "jeu de table"))
        self.pushButton_modifier_jeux_2.setText(_translate("MainWindow", "modifier"))
        self.pushButton_supprimer_jeux.setText(_translate("MainWindow", "supprimer"))
