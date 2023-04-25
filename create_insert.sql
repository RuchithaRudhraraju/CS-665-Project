USE hospitalmanagementsystem;
CREATE TABLE IF NOT EXISTS Patient (
  Pid INT NOT NULL,
  patName CHAR(25) NOT NULL,
  DOB date NOT NULL,
  gender CHAR(11) NOT NULL,
  address varchar(30) NOT NULL,
  PRIMARY KEY (Pid));
INSERT INTO Patient(Pid, patName, DOB, gender, address) values
(1, 'James Luben', '1995-08-31', 'M', '5400 E 21st St N KS');
INSERT INTO Patient(Pid, patName, DOB, gender, address) values
(2, 'Harry Potter', '2000-01-15', 'M', '1665 W Meadow KS');
INSERT INTO Patient(Pid, patName, DOB, gender, address) values
(3, 'Olivia Brad', '1992-05-10', 'F', '132 E Irving TX');
INSERT INTO Patient(Pid, patName, DOB, gender, address) values
(4, 'Mike Chen', '2002-11-23', 'M', '1456 E Downtown Seattle');
INSERT INTO Patient(Pid, patName, DOB, gender, address) values
(5, 'Charlotte Ray', '1998-09-23', 'F', '1832 San Jose CA');
CREATE TABLE IF NOT EXISTS Hospital(
	Hid int NOT NULL,
    Hname VARCHAR(30) NOT NULL,
    Hlocation VARCHAR(25) NOT NULL,
    Htype VARCHAR(15) NOT NULL,
    PRIMARY KEY(Hid));
INSERT INTO Hospital(Hid, Hname, Hlocation, Htype) values
(1, 'Wesley', 'Wichita KS', 'Trauma Center');
INSERT INTO Hospital(Hid, Hname, Hlocation, Htype) values
(2, 'Ku Hospital', 'Kansas City Mi', 'Children');
INSERT INTO Hospital(Hid, Hname, Hlocation, Htype) values
(3, 'Medical city Hospital', 'Dallas TX', 'GastroEntrology');
INSERT INTO Hospital(Hid, Hname, Hlocation, Htype) values
(4, 'Apollo', 'Chicago IL','Spine and Ortho');
INSERT INTO Hospital(Hid, Hname, Hlocation, Htype) values
(5, 'Northwestern Hospital', 'Chicago IL', 'Cardio Vascular');

CREATE TABLE IF NOT EXISTS Doctor(
	Eid int NOT NULL,
    DocName CHAR(20) NOT NULL,
    specialization VARCHAR(15) NOT NULL,
    hospitalId int NOT NULL,
    PRIMARY KEY(Eid),
    FOREIGN KEY (hospitalId) REFERENCES Hospital(Hid)
    ON UPDATE CASCADE ON DELETE RESTRICT);
INSERT INTO Doctor(Eid, DocName, specialization, hospitalId) values
(1, 'Jim', 'Cardiology', 1);
INSERT INTO Doctor(Eid, DocName, specialization, hospitalId) values
(2, 'John', 'Dermatology', 2);
INSERT INTO Doctor(Eid, DocName, specialization, hospitalId) values
(3, 'Wiiliam', 'General Surgery', 2);
INSERT INTO Doctor(Eid, DocName, specialization, hospitalId) values
(4, 'Lucas', 'Anesthesiology', 3);
INSERT INTO Doctor(Eid, DocName, specialization, hospitalId) values
(5, 'Henry', 'Neurosurgery', 3);

CREATE TABLE IF NOT EXISTS Disease(
	Did int NOT NULL,
    Dname VARCHAR(20) NOT NULL,
    PRIMARY KEY(DId));
INSERT INTO Disease(Did, Dname) values
(1, 'tuberculosis');
INSERT INTO Disease(Did, Dname) values
(2, 'Influenza');
INSERT INTO Disease(Did, Dname) values
(3, 'malaria');
INSERT INTO Disease(Did, Dname) values
(4, 'small pox');
INSERT INTO Disease(Did, Dname) values
(5, 'cancer');

CREATE TABLE IF NOT EXISTS Consults(
	Cid int NOT NULL,
    Pid INT NOT NULL,
    Eid int NOT NULL,
    disId int NOT NULL,
    consultDate DATE,
    medication varchar(20) DEFAULT NULL,
    PRIMARY KEY(Cid),
    FOREIGN KEY (Pid) REFERENCES Patient(Pid)
    ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (Eid) REFERENCES Doctor(Eid)
    ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (disId) REFERENCES Disease(Did)
    ON UPDATE CASCADE ON DELETE RESTRICT);
INSERT INTO Consults(Cid, Pid, Eid, DisId, consultDate, medication) values
(1, 3, 3, 5, '2021-08-12', 'Dolo 650'); 
INSERT INTO Consults(Cid, Pid, Eid, DisId, consultDate, medication) values
(2, 3, 4, 2, '2023-02-14', 'Razo D');
INSERT INTO Consults(Cid, Pid, Eid, DisId, consultDate, medication) values
(3, 4, 5, 1, '2008-03-21', 'Supradyn'); 
INSERT INTO Consults(Cid, Pid, Eid, DisId, consultDate, medication) values
(4, 1, 2, 3, '2019-05-22', 'Fepanil 500');
INSERT INTO Consults(Cid, Pid, Eid, DisId, consultDate, medication) values
(5, 4, 2, 1, '2022-11-12', 'Alez-L');     