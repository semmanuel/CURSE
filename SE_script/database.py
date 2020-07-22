import sqlite3
# database file connection
database = sqlite3.connect("CURSE.db")
# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers
cursor = database.cursor()
######################################################################
# SQL command to create a table in the database
sql_command = """CREATE TABLE USER (  
ID		INT 	PRIMARY KEY 	NOT NULL,
NAME	    TEXT	NOT NULL,
SURNAME	    TEXT	NOT NULL,
EMAIL	    TEXT	NOT NULL,
USERNAME	TEXT	NOT NULL,
PASSWORD	TEXT	NOT NULL,
TYPE        TEXT    NOT NULL)
;"""

# execute the statement
cursor.execute(sql_command)

######################################################################
# SQL command to create a table in the database
sql_command = """CREATE TABLE STUDENT (  
ID 		INT 	PRIMARY KEY 	NOT NULL,
NAME		TEXT	NOT NULL,
SURNAME		TEXT 	NOT NULL,
GRADYEAR	INT 	NOT NULL,
MAJOR		CHAR(4) NOT NULL,
EMAIL		text	NOT NULL)
;"""

# execute the statement
cursor.execute(sql_command)
######################################################################
# SQL command to create a table in the database
sql_command = """CREATE TABLE INSTRUCTOR (  
ID 			INT 	PRIMARY KEY 	NOT NULL,
NAME		TEXT	NOT NULL,
SURNAME		TEXT 	NOT NULL,
TITLE		TEXT 	NOT NULL,
HIREYEAR	INT 	NOT NULL,
DEPT		CHAR(4) NOT NULL,
EMAIL		text	NOT NULL)
;"""

# execute the statement
cursor.execute(sql_command)

######################################################################
# SQL command to create a table in the database
sql_command = """CREATE TABLE ADMIN (  
ID 			INT 	PRIMARY KEY 	NOT NULL,
NAME		TEXT	NOT NULL,
SURNAME		TEXT 	NOT NULL,
TITLE		TEXT 	NOT NULL,
OFFICE		TEXT 	NOT NULL,
EMAIL		TEXT	NOT NULL)
;"""

# execute the statement
cursor.execute(sql_command)

######################################################################
# SQL command to create a table in the database
sql_command = """CREATE TABLE COURSE (  
TITLE		TEXT 	NOT NULL,
CRN 		CHAR(4) 	PRIMARY KEY 	NOT NULL,
DEPT		CHAR(4)	NOT NULL,
INSTRUCTOR	TEXT 	NOT NULL,
TIME		TEXT 	NOT NULL,
DAYS_OF_WEEK	TEXT 	NOT NULL,
SEMESTER	TEXT 	NOT NULL,
YEAR		INT 	NOT NULL,
CREDITS		INT		NOT NULL)
;"""
# execute the statement
cursor.execute(sql_command)

###################################################################
# SQL command to create a table in the database
sql_command = """CREATE TABLE ROSTER (
CRN 		CHAR(4) 	NOT NULL,
ID      	INT		NOT NULL,
FOREIGN KEY (CRN) REFERENCES COURSE(CRN),
FOREIGN KEY (ID) REFERENCES STUDENT(ID),
UNIQUE (CRN, ID))
;"""
# execute the statement
cursor.execute(sql_command)
###################################################################
# Portion from now on describes the SCHEDULE DATABASE, implementation RB
sql_command = """CREATE TABLE SCHEDULE (  
TITLE			TEXT 					NOT NULL,
CRN				CHAR(4)	PRIMARY KEY		NOT NULL,
DEPT			TEXT 					NOT NULL,
INSTRUCTOR		TEXT 					NOT NULL,
TIME			TEXT 					NOT NULL,
DAYS_OF_WEEK	TEXT					NOT NULL,
SEMESTER		TEXT					NOT NULL,
YEAR        TEXT          NOT NULL,
CREDITS			TEXT					NOT NULL)
;"""
# create table
cursor.execute(sql_command)
###################################################################
# Student list
cursor.execute("""INSERT INTO STUDENT VALUES(00010001, 'ISAAC', 'NEWTON', 1668, 'BSAS', 'newtoni');""")

cursor.execute("""INSERT INTO STUDENT VALUES(00010002, 'MARIE', 'CURIE', 1903, 'BSAS', 'curiem');""")

cursor.execute("""INSERT INTO STUDENT VALUES(00010003, 'Nikola', 'TESLA', 1878, 'BSEE', 'telsan');""")

cursor.execute("""INSERT INTO STUDENT VALUES(00010004, 'THOMAS', 'EDISON', 1879, 'BSEE', 'notcool');""")

cursor.execute("""INSERT INTO STUDENT VALUES(00010005, 'JOHN', 'VON NEUMANN', 1923, 'BSCO', 'vonneumannj');""")

cursor.execute("""INSERT INTO STUDENT VALUES(00010006, 'GRACE', 'HOPPER', 1928, 'BCOS', 'hopperg');""")

cursor.execute("""INSERT INTO STUDENT VALUES(00010007, 'MAE', 'JEMISON', 1981, 'BSCH', 'jemisonm');""")

cursor.execute("""INSERT INTO STUDENT VALUES(00010008, 'MARK', 'DEAN', 1979, 'BSCO', 'deanm');""")

cursor.execute("""INSERT INTO STUDENT VALUES(00010009, 'MICHAEL', 'FARADAY', 1812, 'BSAS', 'faradaym');""")

cursor.execute("""INSERT INTO STUDENT VALUES(00010010, 'ADA', 'LOVELACE', 1832, 'BCOS', 'lovelacea');""")

cursor.execute("""INSERT INTO STUDENT VALUES(00010011, 'ZACH', 'JERSEY', 1976, 'BSME', 'jerseyz');""")

cursor.execute("""INSERT INTO STUDENT VALUES(00010012, 'GEORGE', 'FLOYD', 2020, 'BSEE', 'floydg');""")

# Roster Table
cursor.execute("""INSERT INTO ROSTER VALUES ('1235', '00010002');""")

cursor.execute("""INSERT INTO ROSTER VALUES ('4553', '00010005');""")

cursor.execute("""INSERT INTO ROSTER VALUES ('6543', '00010003');""")

cursor.execute("""INSERT INTO ROSTER VALUES ('0998', '00010000');""")

cursor.execute("""INSERT INTO ROSTER VALUES ('3456', '00010001');""")
# Instructor list
cursor.execute(
    """INSERT INTO INSTRUCTOR VALUES(00020001, 'Joseph', 'Fourier', 'Full Prof.', 1820, 'BSEE', 'fourierj');""")
cursor.execute(
    """INSERT INTO INSTRUCTOR VALUES(00020002, 'Nelson', 'Mandela', 'Full Prof.', 1994, 'HUSS', 'mandelan');""")
cursor.execute(
    """INSERT INTO INSTRUCTOR VALUES(00020003, 'Galileo', 'Galilei', 'Full Prof.', 1600, 'BSAS', 'galileig');""")
cursor.execute(
    """INSERT INTO INSTRUCTOR VALUES(00020004, 'Alan', 'Turing', 'Associate Prof.', 1940, 'BSCO', 'turinga');""")
cursor.execute(
    """INSERT INTO INSTRUCTOR VALUES(00020005, 'Katie', 'Bouman', 'Assistant Prof.', 2019, 'BSEE', 'boumank');""")
cursor.execute(
    """INSERT INTO INSTRUCTOR VALUES(00020006, 'Daniel', 'Bernoulli', 'Associate Prof.', 1760, 'BSME', 'bernoullid');""")

# Admin list
cursor.execute("""INSERT INTO ADMIN VALUES(00030001, 'Barack', 'Obama', 'President', 'Dobbs 1600', 'obamab');""")
cursor.execute(
    """INSERT INTO ADMIN VALUES(00030002, 'Malala', 'Yousafzai', 'Registrar', 'Wentworth 101', 'yousafzaim');""")

# Course List
cursor.execute(
    """INSERT INTO COURSE VALUES('ELEC3225', '1235', 'BSEE', 'TBD', '8:00-9:50AM', 'MWF', '', '2020', '4 ');""")
cursor.execute(
    """INSERT INTO COURSE VALUES('ENGR5500', '6543', 'HUSS', 'TBD', '11:00-12:50PM', 'MW', 'Fall', '2019', '4 ' );""")
cursor.execute(
    """INSERT INTO COURSE VALUES('ELEC4300', '0356', 'BSAS', 'TBD', '8:00-9:20AM', 'TTR', 'Fall', '2019', '3 ');""")
cursor.execute(
    """INSERT INTO COURSE VALUES('ELEC3250', '5678', 'BSCO', 'TBD', '1:00-3:50PM', 'WF', 'Spring', '2020', '3 ');""")
cursor.execute(
    """INSERT INTO COURSE VALUES('ELEC4500', '9825', 'BSME', 'TBD', '2:00-2:50PM', 'MT', 'Fall', '2019', '4 ');""")
cursor.execute(
    """INSERT INTO COURSE VALUES('DUMMY', 'VARIABLE', 'DUMMY', 'VARIABLE', '8am', 'DUMMY', 'VARIABLE', 'VARIABLE', '');""")
cursor.execute(
  """INSERT INTO COURSE VALUES('Rewrite Everything With Sin Functions ',            '3178', 	'BSEE', 	'JOSEPH FOURIER', '12:00 pm - 12:50pm',		'MTR',	'Summer', '2020',	'4 Credits');""")
cursor.execute(
  """INSERT INTO COURSE VALUES('A Winner Is a Dreamer Who Never Gives Up',          '3139', 	'HUSS', 	'NELSON MANDELA', '10:00 am - 12:50 pm', 	'TR',		'Summer', '2020',	'4 Credits');""")
cursor.execute(
  """INSERT INTO COURSE VALUES('Become the Father of Observational Astronomy',      '3148', 	'BSAS', 	'JOSEPH FOURIER', '9:30  am - 10:50 am',  'WF',		'Summer', '2020',	'4 Credits');""")
cursor.execute(
  """INSERT INTO COURSE VALUES('Cryptanalysis: Send Me a Message I Cant Decrypt',   '3143', 	'BSCO',		'ALAN TURING',	'11:00 am - 12:20 pm',	'WF',		'Summer', '2020',	'4 Credits');""")
cursor.execute(
  """INSERT INTO COURSE VALUES('Black Holes Imagery:Getting Yall Out of The Dark', '3739',	    'BCOS',		'JOSEPH FOURIER',	'1:00 pm - 2:50 pm',		'MF',		'Summer', '2020',	'4 Credits');""")

cursor.execute(
  """INSERT INTO USER VALUES('364670','ELIJAH', 'MCCAIN', '123@BLM.edu', 'equality123','pain','STUDENT');""")
cursor.execute(
  """INSERT INTO USER VALUES('332123', 'BREONNA', 'TAYLOR', '134@BLM.edu', 'arrestthecopsthatkilledbreonnataylor',  'blm','STUDENT');""")
cursor.execute(
  """INSERT INTO USER VALUES('123456','GEORGE','FLOYD',	'3243@BLM.edu',	'forjustice','gonetoosoon','ADMIN');""")
cursor.execute(
  """INSERT INTO USER VALUES('876543', 'MICHAEL', 'JORDAN','23@aj.com',	'mj23','gamble','INSTRUCTOR');""")

database.commit()
