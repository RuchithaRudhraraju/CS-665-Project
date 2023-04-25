#Patient Table
CREATE TABLE IF NOT EXISTS Patient (
  Pid INT NOT NULL,
  patName CHAR(25) NOT NULL,
  DOB date NOT NULL,
  gender CHAR(11) NOT NULL,
  address varchar(30) NOT NULL,
  PRIMARY KEY (Pid));

#Hospital Table
CREATE TABLE IF NOT EXISTS Hospital(
	Hid int NOT NULL,
    Hname VARCHAR(30) NOT NULL,
    Hlocation VARCHAR(25) NOT NULL,
    Htype VARCHAR(15) NOT NULL,
    PRIMARY KEY(Hid));

#Doctor Table
CREATE TABLE IF NOT EXISTS Doctor(
	Eid int NOT NULL,
    DocName CHAR(20) NOT NULL,
    specialization VARCHAR(15) NOT NULL,
    hospitalId int NOT NULL,
    PRIMARY KEY(Eid),
    FOREIGN KEY (hospitalId) REFERENCES Hospital(Hid)
    ON UPDATE CASCADE ON DELETE RESTRICT);

#Disease Table
CREATE TABLE IF NOT EXISTS Disease(
	Did int NOT NULL,
    Dname VARCHAR(20) NOT NULL,
    PRIMARY KEY(DId));

#Consults Table
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