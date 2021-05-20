# Author: Paal Kobbeltvedt

import os, signal
import subprocess
import sys
import time
import psutil




class Executor:

	def __init__(self, path, programs, timeOut):
		self.timeOut = timeOut
		self.path = path
		self.programs = programs



	def execute(self):
		# Create a infinite loop
		while True:
			# Iterate over the files to execude
			for i in range(len(self.programs)):
				self.startProgram(self.programs[i])
				# Sleep for X-seconds before executing next file
				self.sleep()
				# Terminate the program 
				self.exitProgram(self.programs[i])


	def startProgram(self, name):
		print("Starting program " + name)
		cmd = self.path + name
		pid = subprocess.Popen(cmd)



	def sleep(self):
		print("Sleeping for " + str(self.timeOut) + " seconds")
		time.sleep(self.timeOut)

	def exitProgram(self, name):
		id = self.getProcessId(name)
		print("Terminating program " + name + " with ProcessId " + str(id))
		# add Try/Catch
		os.kill(id, signal.SIGTERM)


	def getProcessId(self, name):
		# Iterate over all running process
		for proc in psutil.process_iter():
		    try:
		        # Get process name & pid from process object.
		        processName = proc.name()
		        processID = proc.pid
		        if name == processName:
		        	return processID
		    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
		        pass

		# Could not find the process running
		return None
