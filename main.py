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

def on_click_button1():
	dbcursor = db_connector.cursor()
	query =  " CREATE TABLE Laboratory (Lid INT PRIMARY KEY,Lname VARCHAR(15) NOT NULL,Llocation VARCHAR(20) NOT NULL)"
	dbcursor.execute(query)
	db_connector.commit()

	dbcursor = db_connector.cursor()
	dbcursor.execute("select * from Laboratory")
	myoutput = dbcursor.fetchall()
	output = "Lid\tLName\tLlocation\n"
	for i in myoutput:
		for j in i:
			output += str(j) + "\t"
		output += "\n"
	textbox.setPlainText(output)
	
label1 = QLabel(widget)
label1.setText('Create new Laboratory Table')
label1.move(20, 20)
label1.show()

button1 = QPushButton(widget)
button1.setText('Click')
button1.move(190, 17)
button1.show()

button1.clicked.connect(on_click_button1)

widget.show()

appli.exec_()