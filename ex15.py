#imports argument variables from sys library
from sys import argv
#unpacks argv into script name and first variable which actually is the users filename
script, filename = argv
#uses inbuilt function open to open 'filename' and assigns the string to txt variable
txt = open(filename)
# prints a line telling you your filename and then uses an inbuilt command read on txt variable without any parameters. This reads the file content
print "Here's your file %r: " % filename
print txt.read()
# prints a line and prompts user to retype in the filename. The filenmane is stored in a new variable
print "Type the filename again: "
file_again = raw_input("> ")
# again employs the inbuilt open command and assigns the returned string to a new variable
txt_again = open(file_again)
# again employs the inbuilt read command on the new variable and prints
print txt_again.read()
