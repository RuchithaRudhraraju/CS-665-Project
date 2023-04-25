The intention of "hospital management system" database is to store information about the prime entities of any hospital.

The schema of the database is provided below:
Patient(Pid, patName, DOB, gender, address)
Hospital(Hid, Hname, Hlocation, Htype)
Doctor(Eid, DocName, specialization, hospitalId)
Disease(Did, Dname)
Consults(Cid , Pid, Eid, disId, consultDate, medication)


Table	   Primary Key	   Foreign Key

Patient	   Pid	
Hospital   Hid	
Doctor	   Eid	           hospitalId
Disease	   Did	
Consults   Cid	           Pid, Eid, disId

The following trigger is used for foreign keys: 
ON UPDATE CASCADE ON DELETE RESTRICT

Functional Dependencies for the tables:
	Patient :  Pid → patName, DOB, gender, address
	Hospital: Hid → Hname, Hlocation, Htype
	Doctor: Eid → DocName, specialization, hospitalId
	Disease: Did → Dname
	Consults: Cid → Pid, Eid, disId, consultDate, medication

According to the functional dependencies, the tables are in 3NF form.

Sample Data for the tables:

Patient table:
 Pid  patName          DOB               gender          address
 1    James Luben     1995-08-31          M              5400 E 21st St N KS
 2    Harry Potter    2000-01-15          M              1665 W Meadow KS


Hospital Table:
Hid    Hname         Hlocation         Htype
1      Apollo         Wichita           Trauma Center
2      Wesley         Texas             Children

Doctor Table:
Eid   DocName    specialization   hospitalId
1     Jungkook    Cardiology        2
2     LeeMinHo    ENT               3

Disease Table:
Did    Dname
1      Fever
2      Cold

Consults Table:
Cid   Pid   Eid    disId    consultDate    medication
1      3       2        1    1999-08-25     Dolo
2      1       3        2    2023-02-14     Supradyn



