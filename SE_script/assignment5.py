import sqlite3
import getpass

# import curse_people
"""Portion implemented by professor A.Carpenter as a guideline"""
# database file connection
database = sqlite3.connect("Database.db")

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
cursor.execute(
  """INSERT INTO INSTRUCTOR VALUES(00020001, 'Joseph', 'Fourier', 'Full Prof.', 1820, 'BSEE', 'fourierj');""")
cursor.execute(
  """INSERT INTO INSTRUCTOR VALUES(00020002, 'Nelson', 'Mandela', 'Full Prof.', 1994, 'HUSS', 'mandelan');""")
cursor.execute(
  """INSERT INTO INSTRUCTOR VALUES(00020003, 'Galileo', 'Galilei', 'Full Prof.', 1600, 'BSAS', 'galileig');""")
cursor.execute(
  """INSERT INTO INSTRUCTOR VALUES(00020004, 'Alan', 'Turing', 'Associate Prof.', 1940, 'BSCO', 'turinga');""")
cursor.execute(
  """INSERT INTO INSTRUCTOR VALUES(00020005, 'Katie', 'Bouman', 'Assistant Prof.', 2019, 'BCOS', 'boumank');""")
cursor.execute(
  """INSERT INTO INSTRUCTOR VALUES(00020006, 'Daniel', 'Bernoulli', 'Associate Prof.', 1760, 'BSME', 'bernoullid');""")

# Admin list
cursor.execute("""INSERT INTO ADMIN VALUES(00030001, 'Barack', 'Obama', 'President', 'Dobbs 1600', 'obamab');""")
cursor.execute(
  """INSERT INTO ADMIN VALUES(00030002, 'Malala', 'Yousafzai', 'Registrar', 'Wentworth 101', 'yousafzaim');""")

# Portion from now on describes the COURSES DATABASE, implementation RB
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

# create table
cursor.execute(sql_command)
cursor.execute(
  """INSERT INTO COURSES VALUES('Rewrite Everything With Sin Functions ', 							'31798', 	'BSEE', 	'Joseph Fourier',     '12:00 pm - 12:50pm',		'MTR',	'Summer 2020',	'4 Credits');""")
cursor.execute(
  """INSERT INTO COURSES VALUES('A Winner Is a Dreamer Who Never Gives Up',   					'31039', 	'HUSS', 	'Nelson Mandela', 		'10:00 am - 12:50 pm', 	'TR',		'Summer 2020',	'4 Credits');""")
cursor.execute(
  """INSERT INTO COURSES VALUES('Become the Father of Observational Astronomy', 				'31748', 	'BSAS', 	'Galileo Galilei',     '9:30  am - 10:50 am',  'WF',		'Summer 2020',	'4 Credits');""")
cursor.execute(
  """INSERT INTO COURSES VALUES('Cryptanalysis: Send Me a Message I Cant Decrypt',			'31431', 	'BSCO',		'Alan Turing',				'11:00 am - 12:20 pm',	'WF',		'Summer 2020',	'4 Credits');""")
cursor.execute(
  """INSERT INTO COURSES VALUES('Black Holes Imagery:Getting Yall Out of The Dark',		'31739',	'BCOS',		'Katie Bouman',				'1:00 pm - 2:50 pm',		'MF',		'Summer 2020',	'4 Credits');""")
database.commit()

# Portion from now on describes the SCHEDULE DATABASE, implementation RB
sql_command = """CREATE TABLE SCHEDULE (  
TITLE					TEXT 									NOT NULL,
CRN						CHAR(4)	PRIMARY KEY		NOT NULL,
DEPT					TEXT 									NOT NULL,
INSTRUCTOR		TEXT 									NOT NULL,
TIME					TEXT 									NOT NULL,
DAYS_OF_WEEK	TEXT									NOT NULL,
SEMESTER			TEXT									NOT NULL,
CREDITS				TEXT									NOT NULL)
;"""

# create table
cursor.execute(sql_command)
cursor.execute(
  """INSERT INTO SCHEDULE VALUES('Rewrite Everything With Sin Functions ', 							'31798', 	'BSEE', 	'Joseph Fourier',     '12:00 pm - 12:50pm',		'MTR',	'Summer 2020',	'4 Credits');""")
cursor.execute(
  """INSERT INTO SCHEDULE VALUES('A Winner Is a Dreamer Who Never Gives Up',   					'31039', 	'HUSS', 	'Nelson Mandela', 		'10:00 am - 12:50 pm', 	'TR',		'Summer 2020',	'4 Credits');""")
cursor.execute(
  """INSERT INTO SCHEDULE VALUES('Become the Father of Observational Astronomy', 				'31748', 	'BSAS', 	'Galileo Galilei',     '9:30  am - 10:50 am',  'WF',		'Summer 2020',	'4 Credits');""")
cursor.execute(
  """INSERT INTO SCHEDULE VALUES('Cryptanalysis: Send Me a Message I Cant Decrypt',			'31431', 	'BSCO',		'Alan Turing',				'11:00 am - 12:20 pm',	'WF',		'Summer 2020',	'4 Credits');""")
cursor.execute(
  """INSERT INTO SCHEDULE VALUES('Black Holes Imagery:Getting Yall Out of The Dark',		  '31739',	'BCOS',		'Katie Bouman',				'1:00 pm - 2:50 pm',		'MF',		'Summer 2020',	'4 Credits');""")
database.commit()

sql_command = """CREATE TABLE INSTRUCTOR_SCHEDULE (  
TITLE					TEXT 									NOT NULL,
CRN						CHAR(4)	PRIMARY KEY		NOT NULL,
DEPT					TEXT 									NOT NULL,
INSTRUCTOR		TEXT 									NOT NULL,
TIME					TEXT 									NOT NULL,
DAYS_OF_WEEK	TEXT									NOT NULL,
SEMESTER			TEXT									NOT NULL,
CREDITS				TEXT									NOT NULL)
;"""

cursor.execute(sql_command)
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

'''Class CURSE_PEOPLE'''
'''The curse_people class holds functions 
    which are inherited by student, instructor and administrator'''


class Curse_people:
  def __init__(self, fname: str, lname: str,
               idn: str) -> None:  # the colon notation allows stay on top of the datatupes meant to be passed in

    self.first_name = fname
    self.last_name = lname
    self.id = idn

  def __del__(self):
    del self

  def set_first_name(self, fname: str) -> None:
    self.first_name = fname

  def set_all(self, fname: str, lname: str, idn: str) -> None:
    self.first_name = fname
    self.last_name = lname
    self.id = idn
    self.first_name = fname

  def print_all(self) -> None:
    if (not self.first_name) or (not self.last_name) or (not self.id):
      print(self.first_name + " Make sure every slot is filled")

    else:
      print('Entity is: ' + self.first_name + ' ' + self.last_name + ' , with ID: ' + self.id)

  def set_last_name(self, lname):
    self.last_name = lname

  def set_id(self, ID):
    self.id = ID

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



'''Inheritance Student class'''


class Curse_student(Curse_people):
  def __init__(self, fname: str, lname: str, idn: str) -> None:  # inheritance from parent class
    Curse_people.__init__(self, fname, lname, idn)

  '''Student course search: it is used to search via a certain parameter'''

  def search_course(self) -> None:
    print('You are searching for courses.')
    print(
      'Here are the parameters one can search for course: title, crn, dept, instructor, time, days of the week, semester, credits  ')
    param = input('Which parameter you want to search by:')
    param = param.upper()  # make sure the user input will always match comparison
    while True:
      if param == "TITLE":
        user_input = input('Enter Title of the course')
        cursor.execute(''' SELECT * 
                         FROM COURSES
                         WHERE TITLE=%s );''' % (user_input))
        query_result = cursor.fetchall()
        print('Printing the query result')
        for i in query_result:
          print(i)

      elif param == "CRN":
        user_input = input('Enter CRN of the course')
        cursor.execute('''  SELECT * 
                         FROM COURSES
                         WHERE CRN=%s );''' % (user_input))
        query_result = cursor.fetchall()
        print('Printing the query result')
        for i in query_result:
          print(i)

      elif param == "DEPT":
        (user_input) = ('Enter Department of the course')
        cursor.execute('''  SELECT * 
                         FROM COURSES
                         WHERE DEPT=%s );''' % (user_input))
        query_result = cursor.fetchall()
        print('Printing the query result')
        for i in query_result:
          print(i)

      elif param == "INSTRUCTOR":
        user_input = input('Enter Instructor of the course')
        cursor.execute('''  SELECT * 
                         FROM COURSES
                         WHERE INSTRUCTOR=%s );''' % (user_input))
        query_result = cursor.fetchall()
        print('Printing the query result')
        for i in query_result:
          print(i)

      elif param == "TIME":
        user_input = input('Enter Time of the course')
        cursor.execute('''  SELECT * 
                         FROM COURSES
                         WHERE TIME=%s );''' % (user_input))
        query_result = cursor.fetchall()
        print('Printing the query result')
        for i in query_result:
          print(i)

      elif param == "DAYS_OF_WEEK":
        user_input = input('Enter Days of Week of the course')
        cursor.execute('''  SELECT * 
                         FROM COURSES
                       WHERE DAYS_OF_WEEK=%s);''' % (user_input))
        query_result = cursor.fetchall()
        print('Printing the query result')
        for i in query_result:
          print(i)

      elif param == "SEMESTER":
        user_input = input('Enter Semester of the course')
        cursor.execute('''  SELECT * 
                         FROM COURSES
                   WHERE SEMESTER=%s );''' % (user_input))
        query_result = cursor.fetchall()
        print('Printing the query result')
        for i in query_result:
          print(i)

      elif param == "CREDITS":
        user_input = input('Enter CRN of the course')
        cursor.execute('''  SELECT * 
                         FROM COURSES
                     WHERE CREDITS=%s );''' % (user_input))
        query_result = cursor.fetchall()
        print('Printing the query result')
        for i in query_result:
          print(i)

      else:
        print('The parameter has to match with the options. Please try again or quit.')
      database.commit()
      break

  def add_vs_drop_course(self) -> None:
    # Add or drop courses as a student, depending on crn_parameter
    print('You can add or drop courses.')
    print('Use the crn, to add or drop course')
    ch = input('Will you 0) add or 1) drop course or q) quit :')

    if ch == '0':
      user_input = input('Add the course CRN:')
      while True:
        if len(
                user_input) == 4 & user_input.isdigit():  # crn cannot be greater that 4 digits nor can it include other characters but numbers
          cursor.execute('''  SELECT * 
                         FROM COURSES
                         WHERE CRN=%s);''' % (user_input))
          query_result = cursor.fetchone()  # always fetching one rather than all with the assumption that there is no repeating CRN, so if it exists it will only once
          cursor.execute('''  SELECT * 
                       FROM SCHEDULE
                       WHERE CRN=%s);''' % (user_input))
          query_result1 = cursor.fetchone()
          if query_result != query_result1:
            cursor.execute('''  SELECT * 
                         FROM COURSES, SCHEDULE
                         WHERE COURSES.TIME = SCHEDULE.TIME AND COURSES.DAYS_OF_WEEK = SCHEDULE=DAYS_OF_WEEK);''')
            query_result2 = cursor.fetchone()
            if query_result2 != None:
              for i in query_result():
                sql_command = """INSERT INTO SCHEDULE VALUES(TITLE,CRN, DEPT,INSTRUCTOR, TIME, DAYS_OF_WEEK, SEMESTER, CREDITS) VALUES(%s,%s,%s,%s,%s,%s)"""
                cursor.executemany(sql_command, query_result)
            else:
              print('You have a time conflict')
              cursor.execute("""SELECT * 
                         FROM COURSES, SCHEDULE
                         WHERE COURSES.TIME = SCHEDULE.TIME AND COURSES.DAYS_OF_WEEK = SCHEDULE = AYS_OF_WEEK);""")
              query_result = cursor.fetchall()
              for i in query_result:
                print(i)

          else:
            print('You have already registered for the class with CRN:%s' % user_input)
        else:
          print('The CRN should only be digits and be 4 : %s' % user_input)

    elif ch == '1':
      user_input = input('Remove the course CRN:')
      if len(user_input) == 4 & user_input.isdigit():
        cursor.execute('''  SELECT * 
                        FROM COURSES
                        WHERE CRN=%s);''' % (user_input))
        query_result = cursor.fetchone()
        cursor.execute('''  SELECT * 
                       FROM SCHEDULE
                       WHERE CRN=%s);''' % (user_input))

        query_result1 = cursor.fetchone()
        if query_result == query_result1:
          for i in query_result():
            sql_command = """DELETE FROM SCHEDULE VALUES(TITLE,CRN, DEPT,INSTRUCTOR, TIME, DAYS_OF_WEEK, SEMESTER, CREDITS) VALUES(%s,%s,%s,%s,%s,%s)"""
            cursor.executemany(sql_command, query_result)
        else:
          print('You are not registered for the class with CRN:%s' % user_input)
      else:
        print('The CRN should only be digits and be 4 : %s' % user_input)

    elif ch == 'q' or ch == 'Q':
      pass
    else:
      print('Only options are 1)add 2)remove q)quit')

  '''Printing the schedule based on classes present in the database'''

  def print_schedule(self) -> None:
    cursor.execute("""SELECT * SCHEDULE""")
    query_result = cursor.fetchall()
    if query_result != []:
      for i in query_result:
        print(i)
    else:
      print('There are no courses in the schedule')

  '''Printing all the courses schedule present in the database'''

  def print_all_courses(self):
    cursor.execute("""SELECT * COURSES""")
    query_result = cursor.fetchall()
    if query_result != []:
      for i in query_result:
        print(i)
    else:
      print('There are no courses currently')



  # UN/LINKING STUDENTS TO COURSE
  # REMOVE/ADD COURSES TO THE SYSTEM




class Curse_instructor(Curse_people):
  def __init__(self, fname: str, lname: str, idn: str) -> None:  # inheritance from parent class
    Curse_people.__init__(self, fname, lname, idn)

  def i_search_course(self) -> None:
    print(self.first_name + ' Course Searched')

  def print_instructor_schedule(self):
    cursor.execute('''  SELECT * 
                     FROM INSTRUCTOR_SCHEDULE);''')
    query_result = cursor.fetchall()
    if query_result != []:
      for i in query_result:
        print(i)

    else:
      print('There are no courses currently in the schedule')

  # PRINT ROSTER

  def print_roster(self):
    cursor.execute('''  SELECT * 
                       FROM STUDENT);''')
    query_result = cursor.fetchall()
    if query_result != []:
      for i in query_result:
        print(i)


class Curse_admin(Curse_people):
  def __init__(self, fname: str, lname: str, idn: str) -> None:  # inheritance from parent class
    Curse_people.__init__(self, fname, lname, idn)

  def f_add_vs_drop_course(self, ch: int) -> None:
    if ch == '0':
      print(self.first_name + ' Has added the course')
    elif ch == '1':
      print(self.first_name + 'Has dropped the course')
    elif not ch != '0' or ch != '1':
      print('Choices need to be between 0 and 1')

  def add_vs_remove_users(self, ch: int) -> None:
    if ch == '0':
      print(self.first_name + ' Has added an user')
    elif ch == '1':
      print(self.first_name + ' Has removed an user')
    elif ch != '0' or ch != '1':
      print('Choices need to be between 0 and 1')

  def a_print_schedule(self) -> None:
    print(self.first_name + ' Schedule accessed')

  def search_vs_print_rosters(self, ch: int) -> None:
    if ch == '0':
      print(self.first_name + ' Has search for course')
    elif ch == '1':
      print(self.first_name + ' Has print a roster')
    elif ch != '0' or ch != '1':
      print('Choices need to be between 0 and 1')

  def print_courses(self) -> None:
    print(self.first_name + ' Printed courses')

  def student_override(self):
    print(self.first_name + ' Student override')


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




def main():
  # Invoke main
  print('Welcome to CURSE! What would you like to do?')

  type = input('Please specify if you are a student, instructor or administrator:').upper()
  while (type!='STUDENT' or type!='INSTRUCTOR' or type!='ADMINISTRATOR'):
    print(type,'is invalid. Try again')
    type = input('Please specify if you are a student, instructor or administrator:').upper()

  if (type =='STUDENT'):
    print('Please log in:')
    Curse_people.login()
    option = input('Would you like to: 1)add or drop course, 2) search course 3) print schedule 4) print all courses' )
    while(option!='1'or option!='2' or option!='3' or option!='4'):
     option=input('Invalid numbering try again:')
    if option=='1':
      Curse_student.add_vs_drop_course()
    elif option =='2':
      Curse_student.search_course()
    elif option =='3':
      Curse_student.print_schedule()
    elif option =='4':
      Curse_student.print_all_courses()

  elif(type =='INSTRUCTOR'):
    print('Please log in:')
    Curse_people.login()
    option = input('Would you like to 1) print schedule')
    while (option!='1'):
      option=input('Invalid numbering try again:')

    if option =='1':
      Curse_instructor.print_instructor_schedule()

  elif (type == 'ADMINISTRATOR'):
    print('Please log in:')
    Curse_people.login()

    option = input('Would you like to: 1)add or drop course, or 2)add or remove course from the system')
    while(option!='1'or option=='2'):
      option=input('Invalid numbering try again:')
    if (option=='1'):
      Curse_admin.f_add_vs_drop_course()
    elif(option =='2'):
      Curse_admin.add_removeCourse()




#executing the code
main()
database.commit()
