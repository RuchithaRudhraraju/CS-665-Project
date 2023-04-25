CRUD Operations

Patient Table

INSERT INTO Patient (Pid, patName, DOB, gender, address)
VALUES (9, 'John Doe', '1990-05-15', 'M', '123 Main St.');

SELECT * FROM Patient WHERE Pid = 9;

UPDATE Patient SET address = '456 Elm St.' WHERE DOB= '1990-05-15';

DELETE FROM Patient WHERE patName= 'John Doe';


Hospital Table

INSERT INTO Hospital (Hid, Hname, Hlocation, Htype)
VALUES (10, 'Vista Hospitals', '108 West St.', 'General');

SELECT * FROM Hospital WHERE Hid = 10;

UPDATE Hospital SET Hlocation = '456 Elm St.' WHERE Hname='Vista Hospitals';

DELETE FROM Hospital WHERE Htype='General';


Doctor Table

INSERT INTO Doctor (Eid, DocName, specialization, hospitalId)
VALUES (11, 'Dr. Smith', 'Cardiology', 10);

SELECT * FROM Doctor WHERE Eid = 11;

UPDATE Doctor SET specialization = 'Oncology' WHERE DocName= 'Dr. Smith';

DELETE FROM Doctor WHERE specialization= 'Cardiology';


Disease Table

INSERT INTO Disease (Did, Dname)
VALUES (12, 'Hepatitis');

SELECT * FROM Disease WHERE Did = 12;

UPDATE Disease SET Dname = 'Diabetes' WHERE Did = 12;

DELETE FROM Disease WHERE Dname= 'Diabetes';


Consults Table 

INSERT INTO Consults (Cid, Pid, Eid, disId, consultDate, medication)
VALUES (8, 9, 11, 12, '2022-01-01', 'Insulin');

SELECT * FROM Consults WHERE Cid = 8;

UPDATE Consults SET medication = 'Metformin' WHERE Cid = 8;

DELETE FROM Consults WHERE medication= 'Metformin;
