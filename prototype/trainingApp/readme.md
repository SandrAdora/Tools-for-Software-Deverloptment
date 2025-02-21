# Requirements

1. Install VSC
2. Install Python
3. Install Pip
4. Use Virtual environement
```
   python -m venv <name of the environment > 
   # Activate virtual environment for windows 
   <name of the environment>\Scripts\activate.bat 
   ```
4. In virtual environment install PyQt in VSCode terminal :
5. ```
   pip install PyQt5 
   pip install  PyQt6
   ```
6. Install tools terminals :
7. ```
   pip install PyQt5-tools
   ```

   Standard Import:
8. ```
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
   ```

# PyQt Lib

```
fromPyQt5.QtCoreimportQt , QDate

fromPyQt5.QtWidgetsimportQApplication, QWidget, QLabel, QLineEdit, QGridLayout, QHBoxLayout, QVBoxLayout, QPushButton

fromPyQt5.QtWidgetsimportQTableView,  QSpinBox, QHeaderView, QCheckBox, QDateEdit, QComboBox, QLineEdit, QMessageBox, QTableWidget
```


# For Database

Install Extensions from VSC for viewing DB: **SQLITE** Editor or Viewer

```
fromPyQt5.QtSqlimportQSqlQuery, QSqlDatabase, QSql
```


# Python lib

```
import matplotlib.pyplotasplt
import numpy as np
from sys import exit
```


# Lib for compability with matplotlib

```
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvasQTAgg
```
