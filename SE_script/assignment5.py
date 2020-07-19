import sqlite3
import getpass

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
CRN 		INT 	PRIMARY KEY 	NOT NULL,
DEPT		CHAR(4)	NOT NULL,
INSTRUCTOR	TEXT 	NOT NULL,
TIME		TEXT 	NOT NULL,
DAYs_OF_WEEK	TEXT 	NOT NULL,
SEMESTER	TEXT 	NOT NULL,
YEAR		INT 	NOT NULL,
CREDITS		INT		NOT NULL)
;"""
# execute the statement
cursor.execute(sql_command)
####################################################################
# SQL command to create a table in the database
sql_command = """CREATE TABLE ROSTER (
CRN 		INT 	NOT NULL,
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
sql_command = """CREATE TABLE INSTRUCTOR_SCHEDULE (  
TITLE			TEXT 					NOT NULL,
CRN				CHAR(4)	PRIMARY KEY		NOT NULL,
DEPT			TEXT 					NOT NULL,
INSTRUCTOR		TEXT 					NOT NULL,
TIME			TEXT					NOT NULL,
DAYS_OF_WEEK	TEXT					NOT NULL,
SEMESTER		TEXT					NOT NULL,
CREDITS			TEXT					NOT NULL)
;"""

cursor.execute(sql_command)
###################################################################
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

cursor.execute("""INSERT INTO STUDENT VALUES(00010011, 'Zach', 'Jersey', 1976, 'BSME', 'jerseyz');""")

cursor.execute("""INSERT INTO STUDENT VALUES(00010012, 'George', 'Floyd', 2020, 'BSEE', 'floydg');""")
#database.commit()

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

# Debating on having theses lines or not
'''cursor.execute(
  """INSERT INTO COURSE VALUES('Rewrite Everything With Sin Functions ', 							'31798', 	'BSEE', 	'Joseph Fourier',     '12:00 pm - 12:50pm',		'MTR',	'Summer', '2020',	'4 Credits');""")
cursor.execute(
  """INSERT INTO COURSE VALUES('A Winner Is a Dreamer Who Never Gives Up',   					'31039', 	'HUSS', 	'Nelson Mandela', 		'10:00 am - 12:50 pm', 	'TR',		'Summer', '2020',	'4 Credits');""")
cursor.execute(
  """INSERT INTO COURSE VALUES('Become the Father of Observational Astronomy', 				'31748', 	'BSAS', 	'Galileo Galilei',     '9:30  am - 10:50 am',  'WF',		'Summer', '2020',	'4 Credits');""")
cursor.execute(
  """INSERT INTO COURSE VALUES('Cryptanalysis: Send Me a Message I Cant Decrypt',			'31431', 	'BSCO',		'Alan Turing',				'11:00 am - 12:20 pm',	'WF',		'Summer', '2020',	'4 Credits');""")
cursor.execute(
  """INSERT INTO COURSE VALUES('Black Holes Imagery:Getting Yall Out of The Dark',		  '31739',	'BCOS',		'Katie Bouman',				'1:00 pm - 2:50 pm',		'MF',		'Summer', '2020',	'4 Credits');""")
#database.commit()
'''

# Instructor Schedule
cursor.execute(
  """INSERT INTO INSTRUCTOR_SCHEDULE VALUES('Rewrite Everything With Sin Functions ', 							'31798', 	'BSEE', 	'Joseph Fourier',     '12:00 pm - 12:50pm',		'MTR',	'Summer 2020',	'4 Credits');""")
cursor.execute(
  """INSERT INTO INSTRUCTOR_SCHEDULE VALUES('A Winner Is a Dreamer Who Never Gives Up',   					'31039', 	'HUSS', 	'Nelson Mandela', 		'10:00 am - 12:50 pm', 	'TR',		'Summer 2020',	'4 Credits');""")
cursor.execute(
  """INSERT INTO INSTRUCTOR_SCHEDULE VALUES('Become the Father of Observational Astronomy', 				'31748', 	'BSAS', 	'Galileo Galilei',     '9:30  am - 10:50 am',  'WF',		'Summer 2020',	'4 Credits');""")
cursor.execute(
  """INSERT INTO INSTRUCTOR_SCHEDULE VALUES('Cryptanalysis: Send Me a Message I Cant Decrypt',			'31431', 	'BSCO',		'Alan Turing',				'11:00 am - 12:20 pm',	'WF',		'Summer 2020',	'4 Credits');""")
cursor.execute(
  """INSERT INTO INSTRUCTOR_SCHEDULE VALUES('Black Holes Imagery:Getting Yall Out of The Dark',		'31739',	'BCOS',		'Katie Bouman',				'1:00 pm - 2:50 pm',		'MF',		'Summer 2020',	'4 Credits');""")
database.commit()
'''
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

# QUERY FOR ALL
print("Entire Course table")
cursor.execute("""SELECT * FROM COURSE""")
query_result = cursor.fetchall()
for i in query_result:
    print(i)

# Potential Instructors matched with the course
cursor.execute(
    """SELECT COURSE.TITLE,COURSE.DEPT, NAME, SURNAME FROM COURSE, INSTRUCTOR WHERE COURSE.DEPT = INSTRUCTOR.DEPT;""")
# Check for professor
query_result = cursor.fetchall()
try:
    if query_result[0] != 0:
        print("Potential Instructors for each Course: ")
        for i in query_result:
            print(i)
except IndexError:
    print("No Instructors found for courses")

# Query for Course Titles and CRN
print("All Available Course Titles and Corresponding CRNs")
cursor.execute("""SELECT TITLE, CRN FROM COURSE""")
query_result = cursor.fetchall()
for i in query_result:
    print(i)

# Remove instructor
cursor.execute("""DELETE FROM INSTRUCTOR WHERE ID= 00020004""")

# QUERY FOR Instructor
print("Entire Instructor table")
cursor.execute("""SELECT * FROM INSTRUCTOR""")
query_result = cursor.fetchall()
for i in query_result:
    print(i)

# Update ADMIN
cursor.execute("""UPDATE ADMIN SET TITLE= 'Past President' WHERE ID= 00030001""")
# QUERY FOR ALL
print("Entire Admin table")
cursor.execute("""SELECT * FROM ADMIN""")
query_result = cursor.fetchall()
for i in query_result:
    print(i)
'''
class User:
    def __init__(self, fname: str, lname, idNum):
        self.firstName = fname
        self.lastName = lname
        self.iD = idNum

    def setFirstname(self, fname):
        self.firstName = fname

    def getFirstname(self):
        return self.firstName

    def setLastname(self, lname):
        self.lastName = lname

    def getLastname(self):
        return self.lastName

    def setId(self, idNum):
        self.iD = idNum

    def getId(self):
        return self.iD


    def printAll(self):
        print("First Name:" + self.firstName)
        print("Last Name:" + self.lastName)
        print("ID Number:" + self.iD)

    def searchallCourses(self):
        print("This is the search all courses function")
        print("All Available Course Titles and Corresponding CRNs")
        cursor.execute("""SELECT * FROM COURSE""")
        query_result = cursor.fetchall()
        for i in query_result:
            print(i)

    def searchCourses(self):
        print('You are searching for courses.')
        while True:
            print(
            'Here are the parameters one can search for course: title, crn, dept, instructor, time, days_of_week, semester, credits  ')
            param = input('Which parameter you want to search by or enter q to quit:\n')
            param = param.upper()  # make sure the user input will always match comparison
            if param == "TITLE":
                while True:
                    user_input = input('Enter Title of the course or q to quit:\n')
                    cursor.execute("""  SELECT * 
                                       FROM COURSE
                                       WHERE TITLE='%s';""" % (user_input))
                    query_result = cursor.fetchall() #technically should be fetch all in case there are many sections of a course
                    if query_result!=[]:
                        print('Printing the query result')
                        for i in query_result:
                            print(i)
                    elif user_input=='q' or user_input=='Q':
                        break
                    else:
                        print('Title does not exist')

            elif param == "CRN":
                while True:
                    user_input = input('Enter CRN of the course or q to quit:\n')
                    if len(user_input) == 4 and user_input.isdigit():
                        cursor.execute("""  SELECT * 
                                         FROM COURSE
                                         WHERE CRN='%s';""" % (user_input))
                        query_result = cursor.fetchall()
                        if query_result!=[]:
                            print('Printing the query result')
                            for i in query_result:
                                print(i)

                        else:
                            print('CRN does not exist')

                    elif user_input=='q' or user_input=='Q':
                        break
                    else:
                        print('CRN can only have size digit of 4')

            elif param == "DEPT" or param=='DEPARTMENT':
                while True:
                    user_input = input('Enter Department of the course or q to quit:\n')
                    user_input=user_input.upper()
                    if len(user_input) == 4:
                        cursor.execute("""  SELECT * 
                                         FROM COURSE
                                         WHERE DEPT='%s';""" % (user_input))
                        query_result = cursor.fetchall()            #this case use fetchall because there could be many courses in the same department
                        if query_result!=[]:
                            print('Printing the query result')
                            for i in query_result:
                                print(i)
                        else:
                            print('Department not listed')
                    elif user_input=='q' or user_input=='Q':
                        break
                    else:
                        print("Department can only have 4 letters")

            elif param == "INSTRUCTOR":
                while True:
                    user_input = input('Enter Instructor of the course or q to quit:\n')
                    user_input=user_input.upper() #NEED TO CRAFT AN ALGORITHM TO CAPITALIZE THE FIRST AND LAST NAME
                    cursor.execute("""  SELECT *            
                                     FROM COURSE
                                     WHERE INSTRUCTOR='%s';""" % (user_input))
                    query_result = cursor.fetchall()
                    if query_result!=[]:
                        print('Printing the query result')
                        for i in query_result:
                            print(i)
                    elif user_input=='q' or user_input=='Q':
                        break
                    else:
                        print('Instructor not listed')

            elif param == "TIME":
                while True:
                    user_input = input('Enter Time of the course or q to quit:\n')
                    cursor.execute("""  SELECT * 
                                     FROM COURSE
                                     WHERE TIME='%s';"""% (user_input))
                    query_result = cursor.fetchall()

                    if query_result!=[]:
                        print('Printing the query result')
                        for i in query_result:
                            print(i)
                    elif user_input=='q' or user_input=='Q':
                        break
                    else:
                        print('Time not listed')

            elif param == "DAYS_OF_WEEK":
                while True:
                    user_input = input('Enter Days of Week of the course or q to quit:\n')
                    cursor.execute("""  SELECT * 
                                     FROM COURSE
                                   WHERE DAYS_OF_WEEK='%s';""" % (user_input))
                    query_result = cursor.fetchall()
                    if query_result!=[]:
                        print('Printing the query result')
                        for i in query_result:
                            print(i)
                    elif user_input=='q' or user_input=='Q':
                        break
                    else:
                        print('Days_of_week not listed')

            elif param == "SEMESTER":
                while True:
                    user_input = input('Enter Semester of the course or q to quit:\n')
                    user_input=user_input.upper()
                    cursor.execute("""  SELECT * 
                                     FROM COURSE
                               WHERE SEMESTER='%s';""" % (user_input))
                    query_result = cursor.fetchall()
                    if query_result!=[]:
                        print('Printing the query result')
                        for i in query_result:
                            print(i)
                    elif user_input=='q' or user_input=='Q':
                        break
                    else:
                        print('Semester does not exist')

            elif param == "CREDITS" or param=='CREDIT':
                while True:
                    user_input = input('Enter the number of credits of the course or q to quit:\n')
                    cursor.execute("""  SELECT * 
                                     FROM COURSE
                                 WHERE CREDITS='%s';""" % (user_input))
                    query_result = cursor.fetchall()
                    if query_result!=[]:
                        print('Printing the query result')
                        for i in query_result:
                            print(i)
                    elif user_input=='q' or user_input=='Q':
                        break
                    elif not user_input.isnumeric() and (not user_input=='q' or not user_input=='Q'):
                        print('Credits have to be numbers')
                    else:
                        print('Credits not listed')
            elif param == "q" or param=='Q':
                break

class Student(User):
    def __init__(self, fname, lname, idNum):
        super().__init__(fname, lname, idNum)

    def add_dropCourse(self):
        # Add or drop courses as a student, depending on crn_parameter
        print('You can add or drop courses.')
        print('Use the crn, to add or drop course')
        while (True):
            ch = input('Will you 0) add or 1) drop course or q) quit :\n')
            if ch=='q'or ch=='Q':
                break
            elif ch == '0':
                while (True):
                    user_input = input('Add the course CRN or press q to quit:\n')
                    if (len(user_input) == 4 and user_input.isdigit() and (user_input!='q'or user_input!='Q')):  # crn cannot be greater that 4 digits nor can it include other characters but numbers
                        cursor.execute("""SELECT * 
                                     FROM COURSE
                                     WHERE CRN='%s';""" % (user_input))
                        query_result = cursor.fetchone()  # always fetching one rather than all with the assumption that there is no repeating CRN, so if it exists it will only once
                        cursor.execute("""  SELECT * 
                                   FROM SCHEDULE
                                   WHERE CRN='%s';""" % (user_input))
                        query_result1 = cursor.fetchone()
                        if query_result != query_result1:           #after searching in both tables, if they are different then schedule does not have the course


                            #check if there are other courses with the same time
                            course_time,course_days=query_result[4],query_result[5]

                            #unlike the query_result, the query_result1 might have an empty tuple from querying
                            #So it is needed to handle it
                            if query_result1!= None:
                                schedule_time,schedule_days=query_result1[4],query_result1[5]
                            else:
                                schedule_time,schedule_days='',''

                            if (course_time != schedule_time) and (course_days!=schedule_days):
                                result=[
                                (query_result[0],  #TITLE
                                query_result[1],    #CRN
                                query_result[2],    #DEPT
                                query_result[3],    #INSTRUCTOR
                                query_result[4],    #TIME
                                query_result[5],    #DAYS_OF_WEEK
                                query_result[6],    #SEMESTER
                                query_result[7],    #YEAR
                                query_result[8] )]  #CREDITS

                                sql_command = """INSERT INTO SCHEDULE(TITLE,CRN,DEPT,INSTRUCTOR, TIME,DAYS_OF_WEEK, SEMESTER, YEAR, CREDITS) VALUES(?,?,?,?,?,?,?,?,?)"""
                                cursor.executemany(sql_command, result)
                                print('Course added to schedule')
                                database.commit()
                            else:
                                print('You have a time conflict with:')
                                cursor.execute("""SELECT * 
                                     FROM COURSE, SCHEDULE
                                     WHERE COURSE.TIME = SCHEDULE.TIME AND COURSE.DAYS_OF_WEEK = SCHEDULE.DAYS_OF_WEEK;""")
                                query_result = cursor.fetchall()
                                for i in query_result:
                                    print(i)
                                #break
                        elif query_result==None and query_result1==None:
                            print('There are no courses with the given CRN in the system')
                            #break

                        else:
                            print('You have already registered for the class with CRN:%s' % user_input)
                    elif(user_input=='q'or user_input=='Q'):
                        break
                    else:
                        print("The CRN should only be digits and be 4.")

            elif ch == '1':
                while True:
                    user_input = input('Remove the course CRN or press q to quit:\n')
                    if (len(user_input) == 4 and user_input.isdigit() and (user_input!='q'or user_input!='Q')):
                        cursor.execute("""  SELECT * 
                                        FROM COURSE
                                        WHERE CRN='%s';""" % (user_input))
                        query_result = cursor.fetchone()
                        cursor.execute('''  SELECT * 
                                       FROM SCHEDULE
                                       WHERE CRN='%s';''' % (user_input))

                        query_result1 = cursor.fetchone()
                        if ((query_result!=None) and (query_result == query_result1)):
                            for i in query_result():
                                sql_command = """DELETE FROM SCHEDULE VALUES(TITLE,CRN, DEPT,INSTRUCTOR, TIME, DAYS_OF_WEEK, SEMESTER, YEAR, CREDITS) VALUES(%s,%s,%s,%s,%s,%s)"""
                                cursor.executemany(sql_command, query_result)
                            print('Course removed')
                            database.commit()
                        elif query_result!=None and query_result!=query_result1:
                            print('You are not registered for the class with CRN:',user_input)
                            break

                        elif query_result==query_result1 and query_result==None:
                                print('There are no courses with the given CRN in the system')
                                #break
                    elif(user_input=='q'or user_input=='Q'):
                        break
                    else:
                        print("The CRN should only be digits and be 4.")


    def printSched(self):
        Stu_iD= input("Enter your student id:\n")
        cursor.execute(
            """SELECT ROSTER.CRN, COURSE.TITLE, COURSE.TIME, COURSE.INSTRUCTOR FROM ROSTER,COURSE WHERE ROSTER.CRN= COURSE.CRN AND ROSTER.ID= (%s) ORDER BY COURSE.TITLE;""" %(Stu_iD))
        query_result = cursor.fetchall()
        if query_result != []:
            print("Schedule: \n")
            for i in query_result:
                print(i)
        else:
            print('There are no courses in the schedule\n')

class Admin(User):
    def __init__(self, fname, lname, idNum):
        super().__init__(fname, lname, idNum)

    def add_removeCourse(self):
        while True:
            print("confirm credentials for admin use\n")
            username = input("Enter your username: \n")
            password = getpass.getpass(prompt="Enter your password: \n", stream=None)
            # Query for login
            cursor.execute(
                """SELECT ID FROM USER WHERE USERNAME = ('%s') AND PASSWORD = ('%s') AND TYPE = 'ADMIN';""" % (username, password))
            query_result = cursor.fetchall()
            try:
                if query_result[0] != 0:

                    print("Authorization Successful")
                    ans = input("Would you like to add or remove a course(1 to add, 2 to remove)? \n")
                    if ans == "1":
                        title = input("Course Title: \n")
                        crn = input("Course CRN #: \n")
                        dept = input("Course Department: \n")
                        prof = input("Course Professor Name: \n")
                        time = input("Course time(e.g 2:00-2:50PM): \n")
                        days = input("Course days of the week(Letters only): \n")
                        semester = input("Course Semester: \n")
                        year = input("Course Year: \n")
                        credit = input("Credits of Course:\n")
                        cursor.execute(
                            """INSERT INTO COURSE VALUES('%s', '%s', '%s', '%s','%s', '%s', '%s','%s', '%s');""" % (
                                title, crn, dept, prof, time, days, semester, year, credit))
                    elif ans == "2":
                        try:

                            courseId = input("Enter the CRN for the course that you would like to remove: \n")
                            cursor.execute("""DELETE FROM COURSE WHERE CRN= ('%s')""" %(courseId))
                        except sqlite3.OperationalError:
                            print("Course does not exist\n")
                break
            except IndexError:
                print("Authorization failed")

    def add_removeUser(self):
        while True:
            print("confirm credentials for admin use\n")
            username = input("Enter your username: \n")
            password = getpass.getpass(prompt="Enter your password: \n", stream=None)
            # Query for login
            cursor.execute(
                """SELECT ID FROM USER WHERE USERNAME = ('%s') AND PASSWORD = ('%s') AND TYPE = 'ADMIN';""" % (
                username, password))
            query_result = cursor.fetchall()
            try:
                if query_result[0] != 0:
                    print("Authorization Successful")
                    ans = input("Would you like to add or remove a student or instructor(1 to add, 2 to remove)? \n")
                    if ans == "1":
                        option = input("Would you like to add a student or instructor(i for instructor, s for student)? \n")
                        option = option.upper()
                        if option == "I":
                            try:
                                instructor_id = input("Instructor iD: \n")
                                first_name = input("Instructor First Name: \n")
                                last_name = input("Instructor Last Name: \n")
                                Title = input("Instructor title: \n")
                                hireYear = input("Instructor hireYear: \n")
                                DEPT = input("Instructor Department: \n")
                                email = input("Instructor Email: \n")
                                cursor.execute(
                                    """INSERT INTO INSTRUCTOR VALUES('%s', '%s', '%s', '%s','%s', '%s','%s');""" % (
                                        instructor_id, first_name, last_name, Title, hireYear, DEPT, email))
                            except sqlite3.IntegrityError:
                                print("Instructor already exist")
                        elif option == "S":
                            try:
                                student_id = input("Student iD: \n")
                                firstname = input("Student First Name: \n")
                                lastname = input("Student Last Name: \n")
                                gradyear = input("Student Graduation Year: \n")
                                major = input("Student Major: \n")
                                email = input("Student Email: \n")
                                cursor.execute(
                                    """INSERT INTO STUDENT VALUES('%s', '%s', '%s', '%s','%s', '%s');""" % (
                                        student_id, firstname, lastname, gradyear, major, email))
                            except sqlite3.IntegrityError:
                                print("Student already exist")
                    elif ans == "2":
                        option = input(
                            "Would you like to remove a student or instructor(i for instructor, s for student)? \n")
                        option = option.upper()
                        if option == "I":
                            try:
                                Inst_Id = input("Enter the ID for the Instructor that you would like to remove: \n")
                                cursor.execute("""DELETE FROM INSTRUCTOR WHERE ID= ('%s')""" % (Inst_Id))
                            except sqlite3.OperationalError:
                                print("Instructor does not exist\n")
                        elif option == "S":
                            try:
                                studentId = input("Enter the ID for the Student that you would like to remove: \n")
                                cursor.execute("""DELETE FROM STUDENT WHERE ID= ('%s')""" % (studentId))
                            except sqlite3.OperationalError:
                                print("Student does not exist\n")
                break
            except IndexError:
                print("Authorization failed")

    def searchRoster(self):
        print("This is the search roster function")

    def printCourse(self):
        print("This is the print course function")

    def printRoster(self):
        print("This is the print roster function")

class Instructor(User):
    def __init__(self, fname, lname, idNum):
        super().__init__(fname, lname, idNum)

    def printRoster(self):
        crn = input("Enter CRN to print Roster: ")
        cursor.execute(
            """SELECT ROSTER.ID, STUDENT.NAME, STUDENT.SURNAME FROM ROSTER,STUDENT WHERE ROSTER.ID= STUDENT.ID AND ROSTER.CRN= (%s) ORDER BY STUDENT.NAME;""" %(crn))
        # Check for Roster
        query_result = cursor.fetchall()
        try:
            if query_result[0] != 0:
                print("Roster with Student Name/ID for Course " + crn)
                for i in query_result:
                    print(i)
        except IndexError:
            print("No Roster found\n")
    def printSchedule(self):
        cursor.execute("""SELECT * SCHEDULE""")
        query_result = cursor.fetchall()
        if query_result != []:
            for i in query_result:
                print(i)
        else:
            print('There are no courses in the schedule\n')
    '''Printing all the courses schedule present in the database'''

    def assembleRoster(self):
        while True:
            crn = input("Enter the crn to Create Course Roster: \n")
            # Check to see if course exist
            cursor.execute(
                """SELECT TITLE FROM COURSE WHERE CRN = ('%s');""" % (crn))
            query_result = cursor.fetchall()
            try:
                if query_result[0] != 0:
                    print("Course Found\n")
                    while True:
                        studid= input("Enter iD of Student you would like to add to roster?(Q to quit)\n")
                        studid= studid.upper()
                        if studid == "Q":
                            break
                        else:
                            cursor.execute(
                                """SELECT NAME,SURNAME FROM STUDENT WHERE ID = ('%s');""" % (studid))
                            query_result = cursor.fetchall()
                            try:
                                if query_result[0] != 0:
                                    cursor.execute("""INSERT INTO ROSTER VALUES('%s', '%s');""" % (crn, studid))
                                    print("Student found and added to Roster\n")
                            except IndexError:
                                print("Student does not exist/ID is invalid\n")
                    break
            except IndexError:
                print("Course does not exist/ID is invalid\n")

def login():
    while True:
        acct = input("Is this your first time logging in(Y/N)? \n")
        acct = acct.upper()
        if acct == "Y":
            while True:
                type = input("Are you student, instructor or admin? \n")
                type = type.upper()
                if type == 'STUDENT' or type == 'INSTRUCTOR' or type == 'ADMIN':
                    break
                elif type != 'STUDENT' or type != 'INSTRUCTOR' or type != 'ADMIN':
                    print("Invalid argument\n")
            fname = input("Enter your first name? \n")
            lname = input("Enter your last name? \n")
            email = input("Enter your email address? \n")
            id = input("Enter your ID Number? \n")
            username = input("Create a username: \n")
            while True:
                password = getpass.getpass(prompt="Create your password: \n", stream=None)
                pw = getpass.getpass(prompt="Re-enter your password: \n", stream=None)
                if password == pw:
                    cursor.execute(
                        """INSERT INTO USER VALUES('%s', '%s', '%s', '%s','%s', '%s','%s');""" % (id, fname, lname, email, username, password, type))
                    print("Account successfully created\n")
                    authorization = True
                    return fname, lname, id, type
                elif password != pw:
                    print("Passwords do not match \n")

        elif acct == "N":
            username = input("Enter your username: \n")
            password = getpass.getpass(prompt="Enter your password: \n", stream=None)
            # Query for login
            cursor.execute(
                """SELECT ID, NAME, SURNAME, TYPE FROM USER WHERE USERNAME = ('%s') AND PASSWORD = ('%s');""" % (username, password))
            query_result = cursor.fetchall()
            try:
                if query_result[0] != 0:
                    print("Login Successful \n")
                    for i in query_result:
                        print(i)

                idNumber = query_result[0][0]
                first_name = query_result[0][1]
                last_name = query_result[0][2]
                TYPE = query_result[0][3]
                print(first_name)
                print(last_name)
                return first_name, last_name, idNumber,TYPE
            except IndexError:
                print("Incorrect Username or password\n")
        else:
            print("Invalid Argument\n")
def main ():
    print('Welcome to CURSE!')
    while True:
        print('Please log in:')
        first_name, last_name, idNumber, TYPE = login()
        if TYPE == 'STUDENT':
            student = Student(first_name, last_name, idNumber)
            while True:
                option = input(
                    'Would you like to: 1)add or drop course, 2) search course by parameter 3) print schedule 4) search all courses 5) Log Out: \n')

                if option == '1':
                    student.add_dropCourse()
                elif option == '2':
                    student.searchCourses()
                elif option == '3':
                    student.printSched()
                elif option == '4':
                    student.searchallCourses()
                elif option == '5':
                    print("Thank you using CURSE!")
                    break
                elif option != '1' or option != '2' or option != '3' or option != '4' or option != '5':
                    print('Invalid numbering try again:\n')

        elif (TYPE == 'INSTRUCTOR'):
            instructor = Instructor(first_name, last_name, idNumber)
            while True:
                option = input('Would you like to 1) print schedule, 2) print roster, 3) assemble roster 4) Search all courses 5) Search Course by parameter 6) Log out: \n')

                if option == '1':
                    instructor.printSchedule()
                elif option == '2':
                    instructor.printRoster()
                elif option == '3':
                    instructor.assembleRoster()
                elif option == '4':
                    instructor.searchallCourses()
                elif option == '5':
                    instructor.searchCourses()
                elif option == '6':
                    print("Thank you using CURSE!\n")
                    break
                elif option != '1' or option != '2' or option != '3' or option != '4' or option != '5' or option != '6':
                    print('Invalid numbering try again:\n')

        elif (TYPE == 'ADMIN'):
            admin = Admin(first_name, last_name, idNumber)
            while True:
                option = input('Would you like to: 1)add or remove course from the system 2)add or remove instructors/students 3) Search all courses 4) Search Course by parameter 5) Log Out: \n')
                if (option == '1'):
                    admin.add_removeCourse()
                elif option == '2':
                    admin.add_removeUser()
                elif option == '3':
                    admin.searchallCourses()
                elif option == '4':
                    admin.searchCourses()
                elif option == '5':
                    print("Thank you using CURSE!\n")
                    break
                elif option != '1' or option != '2' or option != '3' or option != '4' or option != '5':
                    print('Invalid numbering try again:\n')

        elif TYPE != 'STUDENT' or TYPE != 'INSTRUCTOR' or TYPE != 'ADMIN':
            print(TYPE, 'is invalid. Try again')

        choice = input("Would you like to log back in?(Y/N) \n")
        choice = choice.upper()
        if choice == 'Y':
            pass
        elif choice == 'N':
            break
if __name__ == "__main__":
    main()

# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
database.commit()

# close the connection
database.close()

'''
######################################################################
# Functions for future use
def queryAll(tableName):
    print("Entire " + tableName + " table")
    cursor.execute("""SELECT * FROM """ + tableName)
    query_result = cursor.fetchall()
    for i in query_result:
        print(i)
def remove(tableName, primaryKey):
    cursor.execute("""DELETE FROM """ + tableName + """ WHERE ID= """ + primaryKey)
def update(tableName, columnName, newValue, primaryKey):
    cursor.execute(
        """UPDATE """ + tableName + """ SET""" + columnName + """= """ + newValue + """WHERE ID= """ + primaryKey)
def insert(type, tableName):
    if type == 1:
        fname = input("First name: ")
        lname = input("Last name: ")
        id = input("ID: ")
        gradyear = input("Graduation Year: ")
        major = input("Major: ")
        email = input("email(Everything before @): ")
        cursor.execute("""INSERT INTO STUDENT VALUES('%s', '%s', '%s', '%s','%s', '%s');""" % (
        fname, lname, id, gradyear, major, email))
    elif type == 2:
        fname = input("Instructor First name: ")
        lname = input("Instructor Last name: ")
        id = input("ID: ")
        title = input("Title: ")
        dept = input("Department: ")
        email = input("email(Everything before @): ")
        hireyear = input("Year Hired: ")
        cursor.execute(
            """INSERT INTO INSTRUCTOR VALUES('%s', '%s', '%s', '%s','%s', '%s','%s');""" % (
            fname, lname, id, title, dept, email, hireyear))
    elif type == 3:
        fname = input("Admin First name: ")
        lname = input("Admin Last name: ")
        id = input("ID: ")
        title = input("Title: ")
        email = input("email(Everything before @): ")
        office = input("Office Number: ")
        cursor.execute(
            """INSERT INTO ADMIN VALUES('%s', '%s', '%s', '%s','%s', '%s);""" % (
            fname, lname, id, title, office, email))
    elif type == 4:
        title = input("Course Title: ")
        crn = input("Course CRN #: ")
        dept = input("Course Department: ")
        prof = input("Course Professor Name: ")
        time = inpu
t("Course time(e.g 2:00-2:50PM): ")
        days = input("Course days of the week(Letters only): ")
        semester = input("Course Semester: ")
        year = input("Course Year: ")
        credit = input("Credits of Course:")
        cursor.execute(
            """INSERT INTO COURSE VALUES('%s', '%s', '%s', '%s','%s', '%s', '%s','%s', '%s');""" % (
            title, crn, dept, prof, time, days, semester, year, credit))
'''


