import sys
from PyQt5.QtCore import Qt , QDate 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtWidgets import QTableView,  QTextEdit,QMainWindow, QSpinBox, QHeaderView, QCheckBox, QDateEdit, QComboBox, QLineEdit, QMessageBox, QTableWidget
from PyQt5.QtGui import QIcon
# for Db
from PyQt5.QtSql import QSqlQuery, QSqlDatabase, QSql

# Python lib
import matplotlib.pyplot as plt
import numpy as np 

class Anmeldung(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_anmeldung_Ui()
        self.anmeldung_initUI()  # Call the initUI method to setup the UI
        self.button_clicked()
    
    def setup_anmeldung_Ui(self):
        self.setWindowTitle("Signing in...")
        self.resize(500, 500)
        self.setWindowIcon(QIcon('fitness-icon.jpg'))
        self.master_layout = QVBoxLayout()
        self.col1 = QVBoxLayout()
        self.col2 = QVBoxLayout()
    def anmeldung_initUI(self):
        # Add objects
        self.anmeldung_email_box = QLineEdit()
        self.anmeldung_password_box = QLineEdit()
        self.anmeldung_btn = QPushButton("sign in")

        # add design
        self.anmeldung_master_layout = QVBoxLayout()
        self.anmeldung_col = QHBoxLayout()
        self.anmeldung_col2 = QHBoxLayout()

        # Sub rows
        self.anmeldung_sub_row1 = QHBoxLayout()
        self.anmeldung_sub_row2 = QHBoxLayout()

        # add widgets
        self.anmeldung_sub_row1.addWidget(QLabel("E-Mail:"))
        self.anmeldung_sub_row1.addWidget(self.anmeldung_email_box)
        self.anmeldung_sub_row2.addWidget(QLabel("Password:"))
        self.anmeldung_sub_row2.addWidget(self.anmeldung_password_box)

        # Add Objects to layout
        self.anmeldung_col.addLayout(self.anmeldung_sub_row1)
        self.anmeldung_col.addLayout(self.anmeldung_sub_row2)
        self.anmeldung_col2.addWidget(self.anmeldung_btn)

        # Add cols to master layout
        self.anmeldung_master_layout.addLayout(self.anmeldung_col)
        self.anmeldung_master_layout.addLayout(self.anmeldung_col2)
        # Call master layout
        self.setLayout(self.anmeldung_master_layout)
    def button_clicked(self):
        pass