from PyQt5.QtCore import Qt , QDate 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtWidgets import QTableView,  QSpinBox, QHeaderView, QCheckBox, QDateEdit, QComboBox, QLineEdit, QMessageBox, QTableWidget

# for Db
from PyQt5.QtSql import QSqlQuery, QSqlDatabase, QSql

# Python lib
import matplotlib.pyplot as plt
import numpy as np 
from sys import exit

# lib for compability with matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvasQTAgg

import sys

# Import for pictures
from PyQt5.QtGui import QIcon
class Konto_Anlegen(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_konto_anlegen_Ui()
        self.konto_anlegen_Ui()
        self.button_pressed()
    
    def setup_konto_anlegen_Ui(self):
        # window for registration
        self.setWindowTitle("Signing Up...")
        self.resize(500, 600)
        # Insert colors and other nice stuff
    def konto_anlegen_Ui(self):
        # 1.  add Objects
        self.firstname_box = QLineEdit() 
        self.firstname_box.setPlaceholderText("Enter your First name")
        self.lastname_box = QLineEdit() 
        self.lastname_box.setPlaceholderText("Enter your last name")
        self.birthdate_box = QDateEdit()
        self.birthdate_box.setDate(QDate.currentDate())
        self.geschlecht_box = QComboBox()
        self.email_box = QLineEdit() 
        self.email_box.setPlaceholderText("Enter your Email") 
        self.password_box = QLineEdit()
        self.height_box = QLineEdit()
        self.height_box.setPlaceholderText("Enter your Height in cm") 
        self.weight_box = QLineEdit()
        self.weight_box.setPlaceholderText("Enter your Weight in kg")

        # Add Items to combo box
        self.geschlecht_box.addItem(" ")
        self.geschlecht_box.addItem("Male")
        self.geschlecht_box.addItem("Female")
      

        # buttons
        self.save_btn = QPushButton("save")
        self.cancel_btn = QPushButton("cancel")

        # 2. layout 
        self.konto_anlegen_master_layout = QHBoxLayout()
        self.konto_anlegen_col1 = QVBoxLayout()


        # 3. sub rows
        self.konto_anlegen_sub_row1 = QVBoxLayout()
        self.konto_anlegen_sub_row2 = QVBoxLayout()
        self.konto_anlegen_sub_row3 = QVBoxLayout()
        self.konto_anlegen_sub_row4 = QVBoxLayout()
        self.konto_anlegen_sub_row5 = QVBoxLayout()
        self.konto_anlegen_sub_row5 = QVBoxLayout()
        self.konto_anlegen_sub_row6 = QVBoxLayout()
        self.konto_anlegen_sub_row7 = QVBoxLayout()
        self.konto_anlegen_sub_row8 = QVBoxLayout()

        # 4. Add widgets
        self.konto_anlegen_sub_row1.addWidget(QLabel("Firstname"))
        self.konto_anlegen_sub_row1.addWidget(self.firstname_box)
        self.konto_anlegen_sub_row2.addWidget(QLabel("Lastname"))
        self.konto_anlegen_sub_row2.addWidget(self.lastname_box)
        self.konto_anlegen_sub_row3.addWidget(QLabel("Birthdate"))
        self.konto_anlegen_sub_row3.addWidget(self.birthdate_box)
        self.konto_anlegen_sub_row4.addWidget(QLabel("Geschlecht"))
        self.konto_anlegen_sub_row4.addWidget(self.geschlecht_box)
        self.konto_anlegen_sub_row5.addWidget(QLabel("Height in cm"))
        self.konto_anlegen_sub_row5.addWidget(self.height_box)
        self.konto_anlegen_sub_row6.addWidget(QLabel("Weight in kg"))
        self.konto_anlegen_sub_row6.addWidget(self.weight_box)
        self.konto_anlegen_sub_row7.addWidget(QLabel("Email"))
        self.konto_anlegen_sub_row7.addWidget(self.email_box)
        self.konto_anlegen_sub_row8.addWidget(QLabel("Password"))  # change to password field with * for visibility  # QLineEdit(self, echoMode=QLineEdit.Password)  # change to password field with * for visibility  # QLineEdit(self, echoMode=QLineEdit.Password)  # change to password field with * for visibility  # QLineEdit(self, echoMode=QLineEdit.Password)  # change
        self.konto_anlegen_sub_row8.addWidget(self.password_box)

        # 5. Add sub rows to col and then to layout
        self.konto_anlegen_col1.addLayout(self.konto_anlegen_sub_row1)
        self.konto_anlegen_col1.addLayout(self.konto_anlegen_sub_row2)
        self.konto_anlegen_col1.addLayout(self.konto_anlegen_sub_row3)
        self.konto_anlegen_col1.addLayout(self.konto_anlegen_sub_row4)
        self.konto_anlegen_col1.addLayout(self.konto_anlegen_sub_row5)
        self.konto_anlegen_col1.addLayout(self.konto_anlegen_sub_row6)
        self.konto_anlegen_col1.addLayout(self.konto_anlegen_sub_row7)
        self.konto_anlegen_col1.addLayout(self.konto_anlegen_sub_row8)


        self.konto_anlegen_col1.addWidget(self.save_btn)
        self.konto_anlegen_col1.addWidget(self.cancel_btn)

        # 6. add cols to master layout
        self.konto_anlegen_master_layout.addLayout(self.konto_anlegen_col1)
        self.setLayout(self.konto_anlegen_master_layout)
    
    # Events
    def button_pressed(self):
        self.save_btn.clicked.connect(self.save_btn_pressed)
        self.cancel_btn.clicked.connect(self.cancel_btn_pressed)
    def save_btn_pressed(self):
        QMessageBox.information(self, "Save", "Successfully created a profile")
        pass
    def cancel_btn_pressed(self):
        pass