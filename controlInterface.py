#!/usr/bin/python3

import os, subprocess,time,asyncio,concurrent.futures
import scapy.all as sm

timeMax=5
serviceName = "BCOMM_BASETES"

nssmFolder = "C:\\Users\\SUPPORT_COMMERCIAL\\Downloads\\nssm-2.24-101-g897c7ad\\win64"

# ret = subprocess.run(
# 	os.path.join(nssmFolder, "nssm.exe") + " status " + serviceName, capture_output=True
# )

# a = str(ret.stdout.decode("utf-8")).replace("\r", "").replace("\n", "")

# if a == "SERVICE_RUNNING":
# 	# print("l.19")

async def checkingProcess():
	# print("\ncheckingProcess=================")
	ret = subprocess.run(
		os.path.join(nssmFolder, "nssm.exe") + " status " + serviceName, capture_output=True
	)
	
	return str(ret.stdout.decode("utf-8")).replace("\r", "").replace("\n", "")


def wiresharking(chrono):
	def callback(pkt):
		# print("\n\n\ncb=============")
		tmp=pkt.sprintf("\nSource :: Ether:%Ether.src% IP:%IP.src% =======> Destination :: Ether:%Ether.dst% IP:%IP.dst%")
		# print("l.42")
		# print("pkt",tmp)

		if (tmp!=""):
			print("reinit")
			chrono.reinit()
		

	sm.sniff(prn= callback,filter = 'dst port 12005')
	sm.sniff(prn= callback,filter = 'dst port 12006')
	return 1

class Chrono():
	def __init__(self):
		self.initialisation=time.time()
		self.chrono=1.1

	def checkingTime(self):
		self.chrono= time.time() - self.initialisation

	def reinit(self):
		self.initialisation=time.time()

def main():
	async def  functionn():
		chrono=Chrono()
		returnValue=await checkingProcess()

		with concurrent.futures.ThreadPoolExecutor() as executor:

			while (returnValue=="SERVICE_RUNNING" and chrono.chrono<=timeMax):

				executor.submit(wiresharking,chrono)
				await asyncio.sleep(0.5)
				chrono.checkingTime()
				print("chrono",chrono.chrono)
				returnValue=await checkingProcess()
				print("l.93")

				while returnValue!="SERVICE_RUNNING":
					print("ERREUR : service stoppé !")
					chrono.reinit()
					returnValue = await checkingProcess()

			if(chrono.chrono>=timeMax):
				chronoDrama=Chrono()
				chrono.reinit()
				while(chrono.chrono>=timeMax):
					print("\n\n=====FROZEN=====")
					chronoDrama.checkingTime()
					await asyncio.sleep(0.5)
					executor.submit(wiresharking,chrono)
				print("\ninexistant")
			print("\ninexistant??")
			# print("\n\n============jesors================\n\n")

		with concurrent.futures.ThreadPoolExecutor() as executor:

			while returnValue!="SERVICE_RUNNING":

				print("ERREUR :  service stoppé !")
				chrono.reinit()
				returnValue = await checkingProcess()

				while (returnValue=="SERVICE_RUNNING" and chrono.chrono<=timeMax):

					executor.submit(wiresharking,chrono)
					await asyncio.sleep(0.5)
					chrono.checkingTime()
					print("chrono",chrono.chrono)
					returnValue=await checkingProcess()
					print("l.93")

				while chrono.chrono>=timeMax:
					wiresharking(chrono)
					print("=====Frozen=====")
					chrono.checkingTime()
	asyncio.run(functionn())



if __name__ == "__main__":
	main()
