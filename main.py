from PyQt5.QtWidgets import *
import sys
import mysql.connector

db_connector = mysql.connector.connect(host="127.0.0.1", user="root", password="Ruchitha@1998", database="hospitalmanagementsystem")

appli = QApplication(sys.argv)

widget = QWidget()
widget.resize(900, 600)
widget.setWindowTitle("Hospital Management System")

textbox = QPlainTextEdit(widget)
textbox.move(340, 20)
textbox.resize(550, 560)
textbox.show()

widget.show()

appli.exec_()