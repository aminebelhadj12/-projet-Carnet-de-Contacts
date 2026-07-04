import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QListWidget,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QMessageBox
)


def ajouter_contact():
    nom = txtNom.text().strip()
    tel = txtTel.text().strip()
    email = txtEmail.text().strip()

    if nom == "" or tel == "":

        qlabelMessage.setText("Le nom et le téléphone sont obligatoires.")
        # QMessageBox.warning(
        #     fenetre,
        #     "Erreur",
        #     "Le nom et le téléphone sont obligatoires."
        # )
        return


    contact = {}
    contact["nom"] = nom
    contact["tel"] = tel
    contact["email"] = email

    # contact = f"{nom} - {tel} - {email}"

    listeContacts.addItem(str(contact))

    # with open("contacts.txt", "a", encoding="utf-8") as f:
    #     f.write(contact + "\n")

    f = open("contacts.txt", "a", encoding="utf-8")
    f.write(str(contact) + "\n")

    txtNom.clear()
    txtTel.clear()
    txtEmail.clear()


def supprimer_contact():


    row = listeContacts.currentRow()


    if row >= 0:
        listeContacts.takeItem(row)

        with open("contacts.txt", "w", encoding="utf-8") as f:
            for i in range(listeContacts.count()):
                f.write(
                    listeContacts.item(i).text()
                    + "\n"
                )



def rechercher_contact():

    # QMessageBox.information(fenetre,"","")


    texte = txtRecherche.text().lower()

   

    for i in range(listeContacts.count()):

        element = listeContacts.item(i)

        if texte in element.text().lower():
            element.setHidden(False)
        else:
            element.setHidden(True)


def charger_contacts():

        with open(
            "contacts.txt",
            "r",
            encoding="utf-8"
        ) as f:

            for ligne in f:
                listeContacts.addItem(
                    ligne.strip()
                )



app = QApplication(sys.argv)

fenetre = QWidget()
fenetre.setWindowTitle("Carnet de Contacts")
fenetre.resize(200, 150)

title = QLabel("📒 CARNET DE CONTACTS")

title.setObjectName("title")

txtNom = QLineEdit()
txtNom.setPlaceholderText("Nom complet")

txtTel = QLineEdit()
txtTel.setPlaceholderText("Téléphone")

txtEmail = QLineEdit()
txtEmail.setPlaceholderText("Email")

btnAjouter = QPushButton("➕ Ajouter Contact")

qlabelMessage = QLabel()
txtRecherche = QLineEdit()
txtRecherche.setPlaceholderText("🔍 Rechercher un contact...")

listeContacts = QListWidget()



btnSupprimer = QPushButton("🗑 Supprimer")
btnQuitter = QPushButton("❌ Quitter")



formCard = QFrame()
formCard.setObjectName("card")


formLayout = QVBoxLayout()
formLayout.addWidget(txtNom)
formLayout.addWidget(txtTel)
formLayout.addWidget(txtEmail)
formLayout.addWidget(btnAjouter)
formLayout.addWidget(qlabelMessage)

formCard.setLayout(formLayout)


buttonsLayout = QHBoxLayout()
buttonsLayout.addWidget(btnSupprimer)
buttonsLayout.addWidget(btnQuitter)


mainLayout = QVBoxLayout()
mainLayout.addWidget(title)
mainLayout.addWidget(formCard)
mainLayout.addWidget(txtRecherche)
mainLayout.addWidget(listeContacts)
mainLayout.addLayout(buttonsLayout)

btnAjouter.clicked.connect(ajouter_contact)
btnSupprimer.clicked.connect(supprimer_contact)
txtRecherche.textChanged.connect(rechercher_contact)

fenetre.setStyleSheet("""
   
    QWidget{
        background-color:#f4f6f9;
        font-family:'Segoe UI';
    }
    QLabel#title{
        font-size:34px;
        font-weight:bold;
        color:#2c3e50;
        padding:20px;
    }
    QPushButton{
        background:#3498db;
        color:white;
        border:none;
        border-radius:12px;
        padding:15px;
        font-size:18px;
        font-weight:bold;
        min-height:25px;
    }
    
""")
charger_contacts()
fenetre.setLayout(mainLayout)
fenetre.show()
sys.exit(app.exec_())




