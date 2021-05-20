from Executor import *



# Use global variables for now

# Path to executables
path = "C:/Windows/System32/" 
# name of programs to run (name.exe)
programs = ["notepad.exe"]
# how many seconds to run a program, before running next
# one week = 604800
timeOut = 5



if __name__ == '__main__':
	ex = Executor(path, programs, timeOut)
	ex.execute()


