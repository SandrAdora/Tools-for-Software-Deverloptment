import sys
from PyQt5.QtCore import Qt , QDate 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtWidgets import QTableView,  QTextEdit,QMainWindow, QSpinBox, QHeaderView, QCheckBox, QDateEdit, QComboBox, QLineEdit, QMessageBox, QTableWidget
from PyQt5.QtGui import QPixmap
# for Db
from PyQt5.QtSql import QSqlQuery, QSqlDatabase, QSql

# Python lib
import matplotlib.pyplot as plt
import numpy as np 

from konto_anlegen import Konto_Anlegen as KA
from anmelden import Anmeldung as AM



class Home(QWidget):
    def __init__(self):
        super().__init__()

        self.setupUi()
        self.initUi()  # Call the initUI method to setup the UI
        self.button_clicked()

    def setupUi(self):
        self.setWindowTitle("Fitness Application")
        self.resize(500, 500)

    def initUi(self):
        # Add Objects
        self.date_box = QDateEdit() 
        self.date_box.setDate(QDate.currentDate()) 
        # Add buttons
        self.btn_konto_anlegen = QPushButton("Sign Up")
        self.btn_anmelden = QPushButton("Login") 

        # Add design
        self.master_layout = QVBoxLayout()
        self.col1 = QHBoxLayout()
        self.col2 = QHBoxLayout()

        self.sub_row1 = QHBoxLayout()
        self.sub_row2 = QHBoxLayout()
        self.sub_row3 = QHBoxLayout()

        # Add widgets
    
        self.sub_row1.addWidget(self.date_box)
        self.sub_row2.addWidget(self.btn_konto_anlegen)
        self.sub_row3.addWidget(self.btn_anmelden)

        # Add sub rows to cols and then to layout
        self.col1.addLayout(self.sub_row1)
        self.col2.addLayout(self.sub_row2)  
        self.col2.addLayout(self.sub_row3)  # Add sub rows to cols and then to layout

        # Add cols to master layout 
        self.master_layout.addLayout(self.col1)
        self.master_layout.addLayout(self.col2)

        # show on the screen 
        self.setLayout(self.master_layout)

    # Event handlers
    def button_clicked(self):
        self.btn_konto_anlegen.clicked.connect(self.konto_anlegen)
        self.btn_anmelden.clicked.connect(self.anmelden)
    def konto_anlegen(self):
        self.konto_anlegen = KA()
        self.konto_anlegen.show()
        #get Class Konto Anlgen Instance

    

    def anmelden(self):
        self.anmelden = AM() 
        self.anmelden.show()

    def load_database(self):
        qu = QSqlQuery("SELECT * FROM app ") 
        while qu.next():
            train_id = qu.value(0)
            firstname = qu.value(1)
            lastname = qu.value(2)
            dateofbirth = qu.value(3)
            gender = qu.value(4)
            nationality = qu.value(5)
            height = qu.value(6)
            weight = qu.value(7)
            email = qu.value(8)
            password = qu.value(9)
            # TODO: do something with these attributes

    # load Database 
def initialize_database():
    # initialise Database
    db = QSqlDatabase.addDatabase("QSQLITE")
    # Set database name
    db.setDatabaseName("app.db")
    # check if database opens
    if not db.open():
        QMessageBox.critical(None, "Cannot open database","Unable to establish a database connection.\n""Please check your database settings.")
        sys.exit(2)
    query = QSqlQuery()
    query.exec_("CREATE TABLE IF NOT EXISTS app (id INTEGER PRIMARY KEY AUTOINCREMENT,firstname TEXT NOT NULL,lastname TEXT NOT NULL,dateofbirth DATE,gender TEXT NOT NULL,nationality TEXT,height REAL,weight REAL,email TEXT UNIQUE NOT NULL,password TEXT NOT NULL)")

# Excecute app
if __name__ == "__main__":
    # Initialize Application 
    app = QApplication([])
    initialize_database()
    # Get Instance of class
    main = Home()
    # Show the main window and execute application
    main.show() 
    app.exec_()