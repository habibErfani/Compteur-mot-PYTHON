import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
            QVBoxLayout, QLabel, QLineEdit


class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        # création du champ de texte
        self.champ = QLineEdit()
        self.motChoisi = QLineEdit()    
        
        
          
        # création du bouton
        self.bouton = QPushButton("GO")
        self.bouton2 = QPushButton("GO")
        self.bouton3 = QPushButton("RESET")
        # on connecte le signal "clicked" à la méthode "appui_bouton_copie"
        self.bouton.clicked.connect(self.resultat)
        self.bouton2.clicked.connect(self.resultat2)
        self.bouton3.clicked.connect(self.resultat3)
 
        # création de l'étiquette
        self.label = QLabel()
        self.resize(750,500)
 
        # mise en place du gestionnaire de mise en forme
        layout = QVBoxLayout()
        layout.addWidget(self.champ)
        layout.addWidget(self.bouton)
        layout.addWidget(self.label)
        self.label2 = QLabel("nbr de mots : ")
        self.label3 = QLabel("nbr de phrases : ")
        self.label4 = QLabel("le mot choisi apparait ... fois")
        self.label5 = QLabel("Choisir le mot : ")
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        layout.addWidget(self.label5)
        layout.addWidget(self.motChoisi)
        layout.addWidget(self.bouton2)
        layout.addWidget(self.label4)
        layout.addWidget(self.bouton3)
        self.setLayout(layout)
        
        self.setWindowTitle("Compteur de mot")

        
    # on définit une méthode à connecter au signal envoyé
    def resultat(self):
        contenu = self.champ.text()
        str1 = "nbr de mots : " + str(len(contenu.split(" ")))
        str2 = "nbr de phrases : "+ str(13)
        self.label2.setText(str1)
        self.label3.setText(str2)
    
    def resultat2(self):

        str3 = "le mot choisi apparait "+str(2)+" fois"
        self.label4.setText(str3)
    
    def resultat3(self):
        self.label2.setText("nbr de mots : ")
        self.label3.setText("nbr de phrases : ")
        self.label4.setText("le mot choisi apparait ... fois")
       
app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)
   
 
fen = Fenetre()
fen.show()
app.exec_()
