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
DAYOFWEEK	TEXT 	NOT NULL,
SEMESTER	TEXT 	NOT NULL,
YEAR		INT 	NOT NULL,
CREDITS		INT		NOT NULL)
;"""
# execute the statement
cursor.execute(sql_command)

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
    """INSERT INTO COURSE VALUES('ELEC3225', 123456, 'BSEE', 'TBD', '8:00-9:50AM', 'MWF', 'Summer', 2020, 4);""")
cursor.execute(
    """INSERT INTO COURSE VALUES('ENGR5500', 654321, 'HUSS', 'TBD', '11:00-12:50PM', 'MW', 'Fall', 2019, 4);""")
cursor.execute(
    """INSERT INTO COURSE VALUES('ELEC4300', 035621, 'BSAS', 'TBD', '8:00-9:20AM', 'TTR', 'Fall', 2019, 3);""")
cursor.execute(
    """INSERT INTO COURSE VALUES('ELEC3250', 567890, 'BSCO', 'TBD', '1:00-3:50PM', 'WF', 'Spring', 2020, 3);""")
cursor.execute(
    """INSERT INTO COURSE VALUES('ELEC4500', 982543, 'BSME', 'TBD', '2:00-2:50PM', 'MT', 'Fall', 2019, 4);""")

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

    def login(self):
        while True:
            authorization = False
            acct = input("Is this your first time logging in(Y/N)? ")
            if acct == "Y":
                type = input("Are you student, instructor or admin?")
                email = input("Enter your email address? ")
                id = input("Enter your ID Number? ")
                username = input("Create a username: ")
                while True:
                    password = getpass.getpass(prompt="Create your password: ", stream=None)
                    pw = getpass.getpass(prompt="Re-enter your password: ", stream=None)
                    if password == pw:
                        cursor.execute(
                            """INSERT INTO USER VALUES('%s', '%s','%s', '%s','%s');""" % (id, email, username, password, type))
                        print("Account successfully created")
                        return authorization is True
                    elif password != pw:
                        print("Passwords do not match")

            elif acct == "N":
                username = input("Enter your username: ")
                password = getpass.getpass(prompt="Enter your password: ", stream=None)
                # Query for login
                cursor.execute(
                    """SELECT ID FROM USER WHERE USERNAME = ('%s') AND PASSWORD = ('%s');""" % (username, password))
                query_result = cursor.fetchall()
                try:
                    if query_result[0] != 0:
                        print("Login Successful")
                        for i in query_result:
                            print(i)
                            return authorization is True
                except IndexError:
                    print("Incorrect Username or password")
            else:
                print("Invalid Argument")

    def printAll(self):
        print("First Name:" + self.firstName)
        print("Last Name:" + self.lastName)
        print("ID Number:" + self.iD)

    def searchallCourses(self):
        print("This is the search all courses function")
        print("All Available Course Titles and Corresponding CRNs")
        cursor.execute("""SELECT TITLE, CRN FROM COURSE""")
        query_result = cursor.fetchall()
        for i in query_result:
            print(i)


class Student(User):
    def __init__(self, fname, lname, idNum):
        super().__init__(fname, lname, idNum)

    def searchCourses(self):
        print("This is the search courses function")

    def add_dropCourse(self):
        print("This is the add/drop courses function")

    def printSched(self):
        print("This is the print schedule function")

class Admin(User):
    def __init__(self, fname, lname, idNum):
        super().__init__(fname, lname, idNum)

    def add_removeCourse(self):
        while True:
            print("confirm credentials for admin use")
            username = input("Enter your username: ")
            password = getpass.getpass(prompt="Enter your password: ", stream=None)
            # Query for login
            cursor.execute(
                """SELECT ID FROM USER WHERE USERNAME = ('%s') AND PASSWORD = ('%s') AND TYPE = 'admin';""" % (username, password))
            query_result = cursor.fetchall()
            try:
                if query_result[0] != 0:
                    ans = input("Would you like to add or remove a course(1 to add, 2 to remove)? ")
                    if ans == "1":
                        title = input("Course Title: ")
                        crn = input("Course CRN #: ")
                        dept = input("Course Department: ")
                        prof = input("Course Professor Name: ")
                        time = input("Course time(e.g 2:00-2:50PM): ")
                        days = input("Course days of the week(Letters only): ")
                        semester = input("Course Semester: ")
                        year = input("Course Year: ")
                        credit = input("Credits of Course:")
                        cursor.execute(
                            """INSERT INTO COURSE VALUES('%s', '%s', '%s', '%s','%s', '%s', '%s','%s', '%s');""" % (
                                title, crn, dept, prof, time, days, semester, year, credit))
                    elif ans == "2":
                        try:
                            courseId = input("Enter the CRN for the course that you would like to remove: ")
                            cursor.execute("""DELETE FROM COURSE WHERE CRN= """ + str(courseId))
                        except sqlite3.OperationalError:
                            print("Course does not exist")
                break
            except IndexError:
                print("Authorization failed")


    def add_removeUser(self):
        print("This is the remove user function")

    def force_add_removeStudent(self):
        print("This is the add/remove student function")

    def searchCourses(self):
        print("This is the search course function")

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
            print("No Roster found")

    def printSchedule(self):
        print("This is the print schedule function")

    def searchCourses(self):
        print("This is the print course function")
    def assembleRoster(self):
        while True:
            crn = input("Enter the crn to Create Course Roster: ")
            # Check to see if course exist
            cursor.execute(
                """SELECT TITLE FROM COURSE WHERE CRN = ('%s');""" % (crn))
            query_result = cursor.fetchall()
            try:
                if query_result[0] != 0:
                    print("Course Found")
                    while True:
                        studid= input("Enter iD of Student you would like to add to roster?(Q to quit)")
                        if studid == "Q":
                            break
                        else:
                            cursor.execute(
                                """SELECT NAME,SURNAME FROM STUDENT WHERE ID = ('%s');""" % (studid))
                            query_result = cursor.fetchall()
                            try:
                                if query_result[0] != 0:
                                    cursor.execute("""INSERT INTO ROSTER VALUES('%s', '%s');""" % (crn, studid))
                                    print("Student found and added to Roster")
                            except IndexError:
                                print("Student does not exist/ID is invalid")
                    break
            except IndexError:
                print("Course does not exist/ID is invalid")

def main():
    '''
    # User Interface
    print("Hello, Welcome to the CURSE Program")
    firstname = input("What is your first name?")
    lastname = input("What is your last name?")
    ident = input("What is your ID Number?")

    student1 = Student(firstname, lastname, ident)
    print(student1.lastName)
    student1.searchallCourses()
    student1.printAll()

    instructor1 = Instructor("Aaron", "Carpenter", 456789)
    instructor1.assembleRoster()
    instructor1.printRoster()

    admin1 = Admin("Michael", "Jordan", 232323)
    #admin1.add_removeUser()
    admin1.add_removeCourse()'''
    admin1 = Admin("Michael", "Jordan", 232323)
    admin1.login()
    admin1.add_removeCourse()


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
        time = input("Course time(e.g 2:00-2:50PM): ")
        days = input("Course days of the week(Letters only): ")
        semester = input("Course Semester: ")
        year = input("Course Year: ")
        credit = input("Credits of Course:")
        cursor.execute(
            """INSERT INTO COURSE VALUES('%s', '%s', '%s', '%s','%s', '%s', '%s','%s', '%s');""" % (
            title, crn, dept, prof, time, days, semester, year, credit))
'''