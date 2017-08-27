################################  Python Cheat Sheet ####################################

# Made this doc while learning python. Hopefully it will be useful to those learning or
# in need of a python reference. It is a work in progress. It's best when opened with a 
# text editor that applies colorscheme so that it's not so boring to look at :).

from datetime import date, time, datetime, timedelta
import os
from os import path

### Variables ###
#-----------------------------  Variables  ---------------------------------------------#
# Declaration
test = "A";
print test	

# Re-declaration of other types!
test = 0; 
print test

	
#global var = 0 # makes a variable global when defined from within a function

#del var # deletes a variable in realtime

#to convert int to string	str(123)



#-----------------------------  Functions  ----------------------------------------------#
					# functions in python are objects
def someFunction():
   print ("--- functions ---\n\n")
	
someFunction()			# executes function
print someFunction()		# executes function and prints return value ( or None )
print someFunction		# prints location of someFunction

def multiply(arg, x=1):		# Args can have default values
   return arg*x

print multiply(16)			# All return the same answer, python interpreter
print multiply(4,4)			# can figure out which variables are which, if you 
print multiply(x=2, arg=8)		# supply the names. Order doesn't matter

def add(*args):			# variable number of args can be provided with use of *
   result = 0;
   for x in args:
      result = result + x
   return result

print add(1, 2, 3, 4, test, 6) 

#-----------------------------  Loops and Logic  ----------------------------------------#
x, y = 1, 1

if ( x < y ):			# All this can be condensed into one line in the form of
	print (" x < y ")	# A if C else B, like so:
elif ( y > x ):
	print (" x > y ")
else:
	print (" x = y ")

print (" x < y ") if ( x < y ) else (" x = y ?") 
	
# There are only two loop control structures in python:
while ( x < 5 ):
   print x
   x = x + 1

for x in range(5, 10):
   print x

arr = ["one","two","three","four"]	# Iterating through an array
for item in arr:
   if (item == "four"): break		# break terminates the loop
   if (1 == 3): continue		# continue skips the current iteration and 
   print item				# continues the loop

for index, item in enumerate(arr):	# Use enumerate to iterate with an index
   print index, item


#-----------------------------  Classes  -------------------------------------------------#

class classExample():			# class construction
   def method1(self):
      print ("--- classes ---")		# methods work the same as functions, but have a
  					# fancy name, cuz OOP 
   def method2(self, arg):
      print (arg + "!")

class inheritance(classExample):	# Inheritance
   def method1(self):			# Override inherited methods in child classes
      classExample.method2(self,"manual")	# Call methods from the parent class
      print ("override")	
   
c = classExample()			# class instantiation
c.method1()
c.method2("success")

c2 = inheritance()
c2.method1()
c2.method2("yay pythonz!")

#-----------------------------  Date and Time  -----------------------------#

today = date.today()
print ("Today is ", today, "Parts: ", today.day, today.month, today.year, today.weekday())
print ("Current Time: ", datetime.time(datetime.now()) )
print ("Date & Time: ", datetime.now())

# Format strings for time, lowercase: abbreviated, uppercase: full
print (datetime.now().strftime("%a, %d %B %Y"))	# %y - year	%a - weekday
						# %b - month	%d - day
# Format date according to locale setting	# %c - locale date and time
						# %x - locale's date
						# %X - locale's time
# Time Formatting	# %I/%H - 12/24 Hour
	# %M - minute	# %S - second		# %p - locales AM or PM

#--- Timedelta Objects ---# 	A timedelta contains a specified amount of time, that 
			# facilitates mathematical operations, counting down, etc.
example = timedelta(days=365, hours=5, minutes=1)
print ("In one year, it will be: " + str(datetime.now() + timedelta(days=365)))

#-----------------------------  Read/Write Files  ----------------------------------------#

f = open("test.txt", "w+") 	# w -write overwrites current file, r -read, a -append
f.write("File has been written")

f = open("test.txt","r")
if f.mode == 'r':		# Check to make sure file was opened
   print f.read()

fl = f.readlines()		# Creates a list of lines in file that can be iterrated 
f.close()

print os.name;

path.exists("test.txt")		# Returns boolean if file exists, if file
path.isfile("test.txt")		# is a file, or if is
path.isdir("test.txt")		# a directory


print ("test.txt's path: " + str(path.realpath("textfile.txt")))
print ("test.txt's path and name: " + str(path.split(path.realpath("textfile.txt"))))

print (time.ctime(path.getmtime("test.txt"))			# get modification time
print (datetime.datetime.fromtimestamp(path.getmtime("test.txt")))# system format

# useful calculation:
print ("File was modified " + str( datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("test.txt") + " ago")

#-----------------------------    -----------------------------#
######################################################################################
