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
	
def on_click_button2():
	dbcursor = db_connector.cursor()
	dbcursor.execute("select * from Patient")
	myoutput = dbcursor.fetchall()
	output = "Pid\tpatName\tDOB\tgender\taddress\n"
	for i in myoutput:
		for j in i:
			output += str(j) + "\t"
		output += "\n"
	textbox.setPlainText(output)

def on_click_button3():
	dbcursor = db_connector.cursor()
	dbcursor.execute("select * from Hospital")
	myoutput = dbcursor.fetchall()
	output = "Hid\tHname\tHlocation\tHtype\n"
	for i in myoutput:
		for j in i:
			output += str(j) + "\t"
		output += "\n"
	textbox.setPlainText(output)

def on_click_button4():
	dbcursor = db_connector.cursor()
	dbcursor.execute("select * from Doctor")
	myoutput = dbcursor.fetchall()
	output = "Eid\tDocName\tspecialization\thospitalId\n"
	for i in myoutput:
		for j in i:
			output += str(j) + "\t"
		output += "\n"
	textbox.setPlainText(output)

def on_click_button5():
	dbcursor = db_connector.cursor()
	dbcursor.execute("select * from Disease")
	myoutput = dbcursor.fetchall()
	output = "Did\tDname\n"
	for i in myoutput:
		for j in i:
			output += str(j) + "\t"
		output += "\n"
	textbox.setPlainText(output)

def on_click_button6():
	dbcursor = db_connector.cursor()
	dbcursor.execute("select * from Consults")
	myoutput = dbcursor.fetchall()
	output = "Cid\tPid\tEid\tdisId\tconsultDate\tmedication\n"
	for i in myoutput:
		for j in i:
			output += str(j) + "\t"
		output += "\n"
	textbox.setPlainText(output)
	
def on_click_button7():
	dbcursor = db_connector.cursor()
	dbcursor.execute("SELECT Eid FROM Doctor JOIN Hospital ON Doctor.hospitalId = Hospital.Hid WHERE Hospital.Hname = 'Ku Hospital'")
	myoutput = dbcursor.fetchall()
	output = "Eid\n"
	for i in myoutput:
		for j in i:
			output += str(j) + "\t"
		output += "\n"
	textbox.setPlainText(output)
	
def on_click_button8():
	dbcursor = db_connector.cursor()
	query = "insert into Patient (Pid, patName, DOB, gender, address) values (%s, %s, %s, %s, %s)"
	values_sql = (6, 'John Cena', '1998-06-15', 'M', '1845 Fairmount St')
	dbcursor.execute(query, values_sql)
	db_connector.commit()

	dbcursor = db_connector.cursor()
	dbcursor.execute("select * from Patient")
	myoutput = dbcursor.fetchall()
	output = "Pid\tpatName\tDOB\tgender\taddress\n"
	for i in myoutput:
		for j in i:
			output += str(j) + "\t"
		output += "\n"
	textbox.setPlainText(output)

def on_click_button9():
	dbcursor = db_connector.cursor()
	query = "insert into Doctor (Eid, DocName, specialization, hospitalId) values (%s, %s, %s, %s)"
	values_sql = (6, 'Sarah Rachel', 'Dermatology', 5)
	dbcursor.execute(query, values_sql)
	db_connector.commit()

	dbcursor = db_connector.cursor()
	dbcursor.execute("select * from Doctor")
	myoutput = dbcursor.fetchall()
	output = "Eid\tDocName\tspecialization\thospitalId\n"
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

label2 = QLabel(widget)
label2.setText('Read Patient Table')
label2.move(20, 48)
label2.show()

button2 = QPushButton(widget)
button2.setText('Click')
button2.move(190, 45)
button2.show()

label3 = QLabel(widget)
label3.setText('Read Hospital Table')
label3.move(20, 76)
label3.show()

button3 = QPushButton(widget)
button3.setText('Click')
button3.move(190, 73)
button3.show()

label4 = QLabel(widget)
label4.setText('Read Doctor Table')
label4.move(20, 104)
label4.show()

button4 = QPushButton(widget)
button4.setText('Click')
button4.move(190, 101)
button4.show()

label5 = QLabel(widget)
label5.setText('Read Disease Table')
label5.move(20, 132)
label5.show()

button5 = QPushButton(widget)
button5.setText('Click')
button5.move(190, 129)
button5.show()

label6 = QLabel(widget)
label6.setText('Read Consults Table')
label6.move(20, 165)
label6.show()

button6 = QPushButton(widget)
button6.setText('Click')
button6.move(190, 162)
button6.show()

label7 = QLabel(widget)
label7.setText('Select using JOINS')
label7.move(20, 198)
label7.show()

button7 = QPushButton(widget)
button7.setText('Click')
button7.move(190, 195)
button7.show()

label8 = QLabel(widget)
label8.setText('Insert 1 row in Patient table')
label8.setWordWrap(True)
label8.move(20, 231)
label8.show()

button8 = QPushButton(widget)
button8.setText('Click')
button8.move(190, 228)
button8.show()

label9 = QLabel(widget)
label9.setText('Insert 1 row in Doctor Table')
label9.setWordWrap(True)
label9.move(20, 265)
label9.show()

button9 = QPushButton(widget)
button9.setText('Click')
button9.move(190, 262)
button9.show()

button1.clicked.connect(on_click_button1)
button2.clicked.connect(on_click_button2)
button3.clicked.connect(on_click_button3)
button4.clicked.connect(on_click_button4)
button5.clicked.connect(on_click_button5)
button6.clicked.connect(on_click_button6)
button7.clicked.connect(on_click_button7)
button8.clicked.connect(on_click_button8)
button9.clicked.connect(on_click_button9)

widget.show()

appli.exec_()