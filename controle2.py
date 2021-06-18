#!/usr/bin/python3

import os, subprocess,time,asyncio,concurrent.futures
import scapy.all as sm

timeMax=300
serviceName = "BCOMM_BASETES"

nssmFolder = "C:\\Users\\SUPPORT_COMMERCIAL\\Downloads\\nssm-2.24-101-g897c7ad\\win64"

ret = subprocess.run(
	os.path.join(nssmFolder, "nssm.exe") + " status " + serviceName, capture_output=True
)

a = str(ret.stdout.decode("utf-8")).replace("\r", "").replace("\n", "")

if a == "SERVICE_RUNNING":
	print("l.19")


async def checkingProcess():
	print("\ncheckingProcess=================")
	ret = subprocess.run(
		os.path.join(nssmFolder, "nssm.exe") + " status " + serviceName, capture_output=True
	)
	
	return str(ret.stdout.decode("utf-8")).replace("\r", "").replace("\n", "")


def fun():
	print("maco")
	time.sleep(5)

def wiresharking(chrono):
	print(chrono) 
	def callback(pkt):

		print("\n\n\ncb=============")
		tmp=pkt.sprintf("\nSource :: Ether:%Ether.src% IP:%IP.src% =======> Destination :: Ether:%Ether.dst% IP:%IP.dst%")
		print("l.42")
		print("pkt",tmp)

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

def wrap_future(asyncio_future):
    def done_callback(af, cf):
        try:
            cf.set_result(af.result())
        except Exception as e:
            af.set_exception(e)

    concur_future = concurrent.futures.Future()
    asyncio_future.add_done_callback(
        lambda f: done_callback(f, cf=concur_future))
    return concur_future

def main():
	async def  functionn():
		chrono=Chrono()
		returnValue=await checkingProcess()

		with concurrent.futures.ThreadPoolExecutor() as executor:

			while (returnValue=="SERVICE_RUNNING" and chrono.chrono<=timeMax):

			
				executor.submit(wiresharking,chrono)
				await asyncio.sleep(1)

				chrono.checkingTime()
				print("chrono",chrono.chrono)

				returnValue=await checkingProcess()

		
				while returnValue!="SERVICE_RUNNING":
					print("ERREUR : service stoppé !")
					returnValue = await checkingProcess()

		# print("\n\n============jesors================\n\n")

		while returnValue!="SERVICE_RUNNING":

			print("ERREUR :  service stoppé !")

			returnValue = await checkingProcess()
			while (returnValue=="SERVICE_RUNNING" and chrono.chrono<=timeMax):

				wiresharking(chrono)
				chrono.checkingTime()
				returnValue=await checkingProcess()

				while chrono>=timeMax:
					wiresharking(chrono)
					print("frozen")
					chrono.checkingTime()

		while chrono.chrono>=timeMax:
			wiresharking(chrono)
			print("frozen")
			chrono.checkingTime()
	asyncio.run(functionn())



if __name__ == "__main__":
	main()
