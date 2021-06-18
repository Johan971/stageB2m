#!/usr/bin/python3

import os, subprocess, concurrent.futures,time
import scapy.all as sm

timeMax=5
serviceName = "BCOMM_BASETES"

nssmFolder = "C:\\Users\\SUPPORT_COMMERCIAL\\Downloads\\nssm-2.24-101-g897c7ad\\win64"

ret = subprocess.run(
	os.path.join(nssmFolder, "nssm.exe") + " status " + serviceName, capture_output=True
)

a = str(ret.stdout.decode("utf-8")).replace("\r", "").replace("\n", "")


if a == "SERVICE_RUNNING":
	print("ook")


def checkingProcess():
	print("\ncheckingProcess=================")
	ret = subprocess.run(
		os.path.join(nssmFolder, "nssm.exe") + " status " + serviceName, capture_output=True
	)
	
	return str(ret.stdout.decode("utf-8")).replace("\r", "").replace("\n", "")

class Chrono():
	def __init__(self):
		self.initialisation= time.time()
		self.chrono=1.1

	def checkingTime(self):
		self.chrono= time.time() - self.initialisation

	def reinit(self):
		self.initialisation=time.time()


def wiresharking(chrono):
	# print(chrono) #blocked after
	def callback(pkt):
		chrono=Chrono()

		while(chrono.chrono<=timeMax):


			tmp=pkt.sprintf("\nSource :: Ether:%Ether.src% IP:%IP.src% =======> Destination :: Ether:%Ether.dst% IP:%IP.dst%")
			print("pkt",tmp)

			if (tmp!=""):
				print("reinit")
				chrono.reinit()
		

	sm.sniff(prn= callback,filter = 'dst port 12005')
	sm.sniff(prn= callback,filter = 'dst port 12006')

	return 1

def main():
	chrono=Chrono()
	
	checkProcess = checkingProcess()
	# sniffing=executor.submit(wiresharking)
	l=[]
	returnValue = checkProcess
	# ret2=sniffing.result()
	with concurrent.futures.ThreadPoolExecutor() as executor:

		while (returnValue=="SERVICE_RUNNING" and chrono.chrono<=timeMax):

			print("\ndebutBoucle ret puis chrono",returnValue,chrono.chrono)
			sniffing=executor.submit(wiresharking,chrono)
			# blocked
			# ret2=sniffing.result
			chrono.checkingTime()
			# print("chrono",chrono.chrono)
			# print("lourd")
			print("\nleger")
			
			while(checkProcess.done()!=True):
				print("l.86")
				print(checkProcess)
				time.sleep(0.1)

			object_methods = [method_name for method_name in dir(checkProcess) ]
			# print(object_methods)

			if checkProcess.done():
				print("ookkkkk")
				print(checkProcess)
			returnValue = checkProcess.result()
			print("doesn't exist")
			print(checkProcess.result())
			while returnValue!="SERVICE_RUNNING":
				print("ERrREUR : service stoppé !")
				checkProcess = executor.submit(checkingProcess)
				returnValue = checkProcess.result()

	print("\n\n============jesors================\n\n")
	if(chrono.chrono>=timeMax):
		print("frozen")
		return -1
	while returnValue!="SERVICE_RUNNING":
		print("ERREUR :  service stoppé !")
		checkProcess = executor.submit(checkingProcess)
		returnValue = checkProcess.result
		while (returnValue=="SERVICE_RUNNING" and chrono.chrono<=timeMax):
			temps1=time.time()
			sniffing=executor.submit(wiresharking(temps1))
			ret2=sniffing.result()
			chrono=time.time() - temps1

			if chrono>timeMax:
				print("frozen")
			checkProcess = executor.submit(checkingProcess)
			returnValue = checkProcess.result
	if chrono>=timeMax:
		print("frozen")

if __name__ == "__main__":
	main()

# x = threading.Thread(target=checkingProcess)
# x.start()


# class myThread1(threading.Thread):
#   def __init__(self, name):
#       threading.Thread.__init__(self)
#       self.name = name

#   def run(self):
#       ret = subprocess.run(
#           os.path.join(nssmFolder, "nssm.exe") + " status " + serviceName, capture_output=True
#       )
#       return str(ret.stdout.decode("utf-8")).replace("\r", "").replace("\n", "")


# class myThread2(threading.Thread):
#   def __init__(self, name):
#       threading.Thread.__init__(self)
#       self.name = name
#   def run(self):
#       # Watching packets on 12005 & 12006
#       print("je watch")


# checkingProcess= myThread1("checkingProcess")

# otherVerif= myThread2("otherVerif")

# checkingProcess.start()
# otherVerif.start()

# checkingProcess.join()
# otherVerif.join()