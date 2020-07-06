import sqlite3
class Curse_people:
  def __init__(self, fname: str, lname:str, idn:str)->None:   # constructor

    self.first_name = fname                             #the colon notation allows to specify the type
    self.last_name = lname
    self.id = idn

  def __del__(self):
    del self


  def set_first_name(self,fname:str)->None:
    self.first_name = fname

  def set_all(self, fname: str, lname:str, idn:str)->None:
    self.first_name = fname
    self.last_name = lname
    self.id = idn
    self.first_name = fname


  def print_all(self)->None:
    if (not self.first_name) or (not self.last_name) or (not self.id):
      print(self.first_name +" Make sure every slot is filled")

    else:
      print('Entity is: ' + self.first_name + ' ' +self.last_name+ ' , with ID: '+ self.id)

  def set_last_name(self,lname):
    self.last_name = lname
  def set_id(self,ID):
    self.id = ID

class Curse_student(Curse_people):
  def __init__(self, fname:str, lname:str, idn:str)->None:        #inheritance from parent class
    Curse_people.__init__(self, fname, lname, idn)

  def search_course(self)->None:
    print(self.first_name + ' Searched for a course')

  def add_vs_drop_course(self, ch:int)->None:

    if  ch=='0':
      print(self.first_name +' Has added the course')
    elif ch=='1':
      print(self.first_name +' Has dropped the course')
    elif  ch!='0' or ch != '1':
      print('Choices need to be between 0 and 1')

  def print_schedule(self)->None:
    print(self.first_name +' Schedule accessed')


class Curse_instructor(Curse_people):
  def __init__(self, fname:str, lname:str, idn:str)->None:           #inheritance from parent class
    Curse_people.__init__(self, fname, lname, idn)

  def i_search_course(self)->None:
    print(self.first_name +' Course Searched')

  def print_roster(self)->None:
    print(self.first_name +' Roster printed')

  def i_print_schedule(self)->None:
    print( self.first_name +' Schedule accessed')

class Curse_admin(Curse_people):
  def __init__(self, fname:str, lname:str, idn:str)->None:              #inheritance from parent class
    Curse_people.__init__(self, fname, lname, idn)

  def f_add_vs_drop_course(self,ch:int)->None:
    if  ch == '0':
      print(self.first_name + ' Has added the course')
    elif ch == '1':
      print(self.first_name +'Has dropped the course')
    elif not  ch!='0' or ch != '1':
      print('Choices need to be between 0 and 1')

  def add_vs_remove_users(self,ch:int)->None:

    if ch== '0':
      print(self.first_name + ' Has added an user')
    elif  ch == '1':
      print( self.first_name + ' Has removed an user')
    elif  ch!='0' or ch != '1':
      print('Choices need to be between 0 and 1')

  def a_print_schedule(self)->None:
    print(self.first_name + ' Schedule accessed')

  def search_vs_print_rosters (self,ch:int)->None:

    if ch == '0':
      print(self.first_name + ' Has search for course')
    elif ch == '1' :
      print(self.first_name +' Has print a roster')
    elif ch!='0' or ch != '1':
      print('Choices need to be between 0 and 1')

  def print_courses(self)->None:
    print(self.first_name + ' Printed courses')

  def student_override(self):
    print(self.first_name + ' Student override')


database = sqlite3.connect("assignment7.db")
  def menu(self):
    print("Welcome to CURSE!")
    username = input("Please enter your login:")
    cursor = database.cursor()




user_input = '0'
user	= Curse_people("Dani", "Ojeda", "90812")
user.print_all ()

print('Now changing parameters')
user.set_first_name('Angel')
user.set_last_name('Moreno')
user.set_id('0921773')
user.print_all()

user.set_all('Soraia','Ramos','01291')
user.print_all()

student  = Curse_student("sofia", "j", "021")
student.print_all ()

while True:
  user_input = input("Enter value to add or drop class: ")
  if user_input == '-1':
    break
  student.add_vs_drop_course(user_input)

student.search_course ()


instructor  = Curse_instructor("susan", "Vaz", "97123")
instructor.print_all()

instructor.i_search_course()
instructor. i_print_schedule()
instructor. print_roster()

admin  = Curse_admin("jorja", "smith", "821231")
admin.print_all()

while True:
  user_input = input("Enter value to add or drop class admin: ")
  if user_input == '-1':
    break
  admin.f_add_vs_drop_course(user_input)

while True:
  user_input = input("Enter value to add or remove users admin: ")
  if user_input == '-1':
    break
  admin.add_vs_remove_users(user_input)

while True:
  user_input = input("Enter value to search or print rosters admin: ")
  if user_input == '-1':
    break
  admin.search_vs_print_rosters(user_input)

admin.print_courses     ()
admin.a_print_schedule  ()
admin.student_override  ()





