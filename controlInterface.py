#!/usr/bin/python3

import os, subprocess, concurrent.futures

serviceName = "BCOMM_BASETES"

nssmFolder = "C:\\Users\\SUPPORT_COMMERCIAL\\Downloads\\nssm-2.24-101-g897c7ad\\win64"

ret = subprocess.run(
	os.path.join(nssmFolder, "nssm.exe") + " status " + serviceName, capture_output=True
)

a = str(ret.stdout.decode("utf-8")).replace("\r", "").replace("\n", "")


if a == "SERVICE_RUNNING":
	print("ook")


def checkingProcess():
	ret = subprocess.run(
		os.path.join(nssmFolder, "nssm.exe") + " status " + serviceName, capture_output=True
	)
	return str(ret.stdout.decode("utf-8")).replace("\r", "").replace("\n", "")

def wiresharking():
	return print("je wire")


with concurrent.futures.ThreadPoolExecutor() as executor:
	checkProcess = executor.submit(checkingProcess)
	# sniffing12005=executor.submit(wiresharking)

	returnValue = checkProcess.result()
	# ret2=sniffing12005.result()
	while returnValue=="SERVICE_RUNNING":
		sniffing12005=executor.submit(wiresharking)
		ret2=sniffing12005.result()
		print(returnValue)


# x = threading.Thread(target=checkingProcess)
# x.start()


# class myThread1(threading.Thread):
# 	def __init__(self, name):
# 		threading.Thread.__init__(self)
# 		self.name = name

# 	def run(self):
# 		ret = subprocess.run(
# 			os.path.join(nssmFolder, "nssm.exe") + " status " + serviceName, capture_output=True
# 		)
# 		return str(ret.stdout.decode("utf-8")).replace("\r", "").replace("\n", "")


# class myThread2(threading.Thread):
# 	def __init__(self, name):
# 		threading.Thread.__init__(self)
# 		self.name = name
# 	def run(self):
# 		# Watching packets on 12005 & 12006
# 		print("je watch")


# checkingProcess= myThread1("checkingProcess")

# otherVerif= myThread2("otherVerif")

# checkingProcess.start()
# otherVerif.start()

# checkingProcess.join()
# otherVerif.join()