import sqlite3
import numpy as np
"""Portion implemented by professor A.Carpenter as a guideline"""
# database file connection
database = sqlite3.connect("assignment7.db")

# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers
cursor = database.cursor()

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
ID 		INT 	PRIMARY KEY 	NOT NULL,
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
ID 		INT 	PRIMARY KEY 	NOT NULL,
NAME		TEXT	NOT NULL,
SURNAME		TEXT 	NOT NULL,
TITLE		TEXT 	NOT NULL,
OFFICE		TEXT 	NOT NULL,
EMAIL		text	NOT NULL)
;"""

# execute the statement
cursor.execute(sql_command)

# Student list
cursor.execute("""INSERT INTO STUDENT VALUES(00010001, 'Isaac', 'Newton', 1668, 'BSAS', 'newtoni');""")
cursor.execute("""INSERT INTO STUDENT VALUES(00010002, 'Marie', 'Curie', 1903, 'BSAS', 'curiem');""")
cursor.execute("""INSERT INTO STUDENT VALUES(00010003, 'Nikola', 'Tesla', 1878, 'BSEE', 'telsan');""")
cursor.execute("""INSERT INTO STUDENT VALUES(00010004, 'Thomas', 'Edison', 1879, 'BSEE', 'notcool');""")
cursor.execute("""INSERT INTO STUDENT VALUES(00010005, 'John', 'von Neumann', 1923, 'BSCO', 'vonneumannj');""")
cursor.execute("""INSERT INTO STUDENT VALUES(00010006, 'Grace', 'Hopper', 1928, 'BCOS', 'hopperg');""")
cursor.execute("""INSERT INTO STUDENT VALUES(00010007, 'Mae', 'Jemison', 1981, 'BSCH', 'jemisonm');""")
cursor.execute("""INSERT INTO STUDENT VALUES(00010008, 'Mark', 'Dean', 1979, 'BSCO', 'deanm');""")
cursor.execute("""INSERT INTO STUDENT VALUES(00010009, 'Michael', 'Faraday', 1812, 'BSAS', 'faradaym');""")
cursor.execute("""INSERT INTO STUDENT VALUES(00010010, 'Ada', 'Lovelace', 1832, 'BCOS', 'lovelacea');""")

# Instructor list
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020001, 'Joseph', 'Fourier', 'Full Prof.', 1820, 'BSEE', 'fourierj');""")
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020002, 'Nelson', 'Mandela', 'Full Prof.', 1994, 'HUSS', 'mandelan');""")
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020003, 'Galileo', 'Galilei', 'Full Prof.', 1600, 'BSAS', 'galileig');""")
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020004, 'Alan', 'Turing', 'Associate Prof.', 1940, 'BSCO', 'turinga');""")
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020005, 'Katie', 'Bouman', 'Assistant Prof.', 2019, 'BCOS', 'boumank');""")
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020006, 'Daniel', 'Bernoulli', 'Associate Prof.', 1760, 'BSME', 'bernoullid');""")

# Admin list
cursor.execute("""INSERT INTO ADMIN VALUES(00030001, 'Barack', 'Obama', 'President', 'Dobbs 1600', 'obamab');""")
cursor.execute("""INSERT INTO ADMIN VALUES(00030002, 'Malala', 'Yousafzai', 'Registrar', 'Wentworth 101', 'yousafzaim');""")

# QUERY FOR ALL
print("Entire Student table")
cursor.execute("""SELECT * FROM STUDENT""")
query_result = cursor.fetchall()

for i in query_result:
	print(i)

# QUERY FOR ALL
print("Entire Instructor table")
cursor.execute("""SELECT * FROM INSTRUCTOR""")
query_result = cursor.fetchall()

for i in query_result:
	print(i)

# QUERY FOR ALL
print("Entire Admin table")
cursor.execute("""SELECT * FROM ADMIN""")
query_result = cursor.fetchall()

for i in query_result:
	print(i)
# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
database.commit()

##############################################################################




#query each course for the department and query the result to match instructor to the course





'''
cursor.execute("""INSERT INTO COURSES VALUES('Rewrite Everything With Sin Functions ', 							'31798', 	'BSEE', 	'Joseph Fourier',     '12:00 pm - 12:50pm',		'MTR',	'Summer 2020',	'4 Credits');""")
cursor.execute("""INSERT INTO COURSES VALUES('A Winner Is a Dreamer Who Never Gives Up',   					'31039', 	'HUSS', 	'Nelson Mandela', 		'10:00 am - 12:50 pm', 	'TR',		'Summer 2020',	'4 Credits');""")
cursor.execute("""INSERT INTO COURSES VALUES('Become the Father of Observational Astronomy', 				'31748', 	'BSAS', 	'Galileo Galilei',    '9:30  am - 10:50 am',  'WF',		'Summer 2020',	'4 Credits');""")
cursor.execute("""INSERT INTO COURSES VALUES('Cryptanalysis: Send Me a Message I Cant Decrypt',			'31431', 	'BSCO',		'Alan Turing',				'11:00 am - 12:20 pm',	'WF',		'Summer 2020',	'4 Credits');""")
cursor.execute("""INSERT INTO COURSES VALUES('Black Holes Imagery:Getting Yall Out of The Dark',		'31739',	'BCOS',		'Katie Bouman',				'1:00 pm - 2:50 pm',		'MF',		'Summer 2020',	'4 Credits');""")

#query each course for the department and query the result to match instructor to the course
cursor.execute("""	SELECT COURSES.TITLE, INSTRUCTOR.NAME, INSTRUCTOR.SURNAME
													FROM COURSES, INSTRUCTOR 
													WHERE INSTRUCTOR.DEPT =  COURSES.DEPT;""")
query_result = cursor.fetchall()
print('Printing the query result')
for i in query_result:
	print(i)

'''
# close the connection


def update_table():
	cursor.execute("""UPDATE ADMIN SET TITLE = 'Past President' WHERE EMAIL = 'obamab';""")

	cursor.execute("""SELECT * FROM ADMIN""")
	query_result = cursor.fetchall()
	print('Printing the update result')
	for i in query_result:
		print(i)

	database.commit()

def remove_instructor():
	cursor.execute("""DELETE FROM INSTRUCTOR WHERE ID = 00020001 ;""")
	cursor.execute("""SELECT * FROM INSTRUCTOR""")
	query_result = cursor.fetchall()
	if query_result !=None:
		print('Printing professors after removal of Fourier')
		for i in query_result:
			print(i)



def fetch_one_flag():
	cursor.execute("""SELECT COURSES.TITLE, INSTRUCTOR.NAME, INSTRUCTOR.SURNAME
													FROM COURSES, INSTRUCTOR 
													WHERE INSTRUCTOR.DEPT = 'Gibberish';""")
	query_result = cursor.fetchone()

	if query_result != None:

		print('Printing the result')
		for i in query_result:
			print(i)

	else:
		print('There are no professors for the course')



def insert_parameter():
	ID = ''
	gradyear= ''
	choice = ''
	choice=input('Pick which academic body you would like to input: Student (1), Instructor (2), Administrator (3)')

	if (choice == '1'):
		while (not isinstance(ID,int)):
			ID = input("Enter ID of student:")

			if (ID.isdigit()):
					ID = int(ID)
			else:
				print('ID can only be numerical')

	name =	input("Enter name of student:")
	surname= input("Enter surname of student:")

	while (not isinstance(gradyear,int)):
		gradyear =	input('Enter the gradyear')

		if (gradyear.isdigit()):
			gradyear = int(gradyear)
		else:
			print('Grad year can only be numerical')

	major = input ("Enter major of student:")
	count = 0
	while (count!=4):

		for i in range(len(major)):
			count = count + 1

		if (count!=4):
			print('Major must have four initials')
			count = 0
		else:
			pass
	email=input('Enter username')
	cursor.execute("""INSERT INTO STUDENT VALUES('%d', '%s', '%s', '%d','%s','%s');""" % (ID, name,surname, gradyear, major, email))

	if (choice=='2'	):

		name  =	input("Enter name of instructor:")
		surname  	=	input("Enter last name of instructor:")
		title 		= input("Enter title of of instructor:")
		office		= input("Enter title of of instructor:")
		email			= input('Enter username')

		cursor.execute("""INSERT INTO INSTRUCTOR VALUES('%s', '%s', '%s', '%s, %s');""" % (name, surname, title, office, email))

#administrator
	if (choice=='3'	):
		while (not isinstance(ID,int)):
			ID = input("Enter ID of student:")

			if (ID.isdigit()):
					ID = int(ID)
			else:
				print('ID can only be numerical')

		name  		=	input("Enter name of admin:")
		surname  	=	input("Enter last name of admin:")
		title 		= input("Enter title of of admin:")
		office		= input("Enter title of of admin:")
		email			= input('Enter username')

		cursor.execute("""INSERT INTO ADMIN VALUES('%s', '%s', '%s', '%s', %s, %s);""" % (ID, name, surname,title, office,email))
		database.commit()


def search_dpt_professor():

	cursor.execute("""SELECT COURSES.TITLE, INSTRUCTOR.NAME, INSTRUCTOR.SURNAME
														FROM COURSES, INSTRUCTOR 
														WHERE INSTRUCTOR.DEPT =  COURSES.DEPT;""")
	query_result = cursor.fetchall()
	print('Printing the query result')
	for i in query_result:
		print(i)
	database.commit()



def create_table():
	#Portion from now on describes the courses database, implementation RB
	sql_command = """CREATE TABLE COURSES (  
	TITLE					TEXT 									NOT NULL,
	CRN						CHAR(4)	PRIMARY KEY		NOT NULL,
	DEPT					TEXT 									NOT NULL,
	INSTRUCTOR		TEXT 									NOT NULL,
	TIME					TEXT 									NOT NULL,
	DAYS_OF_WEEK	TEXT									NOT NULL,
	SEMESTER			TEXT									NOT NULL,
	CREDITS				TEXT									NOT NULL)
	;"""

	#create table
	cursor.execute(sql_command)
	cursor.execute("""INSERT INTO COURSES VALUES('Rewrite Everything With Sin Functions ', 							'31798', 	'BSEE', 	'Joseph Fourier',     '12:00 pm - 12:50pm',		'MTR',	'Summer 2020',	'4 Credits');""")
	cursor.execute("""INSERT INTO COURSES VALUES('A Winner Is a Dreamer Who Never Gives Up',   					'31039', 	'HUSS', 	'Nelson Mandela', 		'10:00 am - 12:50 pm', 	'TR',		'Summer 2020',	'4 Credits');""")
	cursor.execute("""INSERT INTO COURSES VALUES('Become the Father of Observational Astronomy', 				'31748', 	'BSAS', 	'Galileo Galilei',     '9:30  am - 10:50 am',  'WF',		'Summer 2020',	'4 Credits');""")
	cursor.execute("""INSERT INTO COURSES VALUES('Cryptanalysis: Send Me a Message I Cant Decrypt',			'31431', 	'BSCO',		'Alan Turing',				'11:00 am - 12:20 pm',	'WF',		'Summer 2020',	'4 Credits');""")
	cursor.execute("""INSERT INTO COURSES VALUES('Black Holes Imagery:Getting Yall Out of The Dark',		'31739',	'BCOS',		'Katie Bouman',				'1:00 pm - 2:50 pm',		'MF',		'Summer 2020',	'4 Credits');""")
	database.commit()

def print_all():

		# QUERY FOR ALL
	print("Entire table")
	cursor.execute("""SELECT * FROM STUDENT""")
	query_result = cursor.fetchall()

	for i in query_result:
		print(i)

	# QUERY FOR ALL
	print("Entire table")
	cursor.execute("""SELECT * FROM INSTRUCTOR""")
	query_result = cursor.fetchall()

	for i in query_result:
		print(i)

	# QUERY FOR ALL
	print("Entire table")
	cursor.execute("""SELECT * FROM ADMIN""")
	query_result = cursor.fetchall()

	for i in query_result:
		print(i)



######################################################################################################################################################
'''main body'''

print('Creating table...')
create_table()
print('Updating table....')
update_table()



print('Removing instructor....')
remove_instructor()

print('Searching professor in department the specific courses')
search_dpt_professor()

print('Flagging.....')
fetch_one_flag()

print('Insert parameter')
insert_parameter()



print('Printing all....')
print_all()


database.commit()
database.close()
