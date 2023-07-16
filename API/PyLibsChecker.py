﻿# -*- coding: UTF-8 -*-
## Developed by: QaYe<qadary-yemen>

import sys,os
import subprocess
pyPath=sys.prefix
PV=sys.version.split()

def SL(fPath=f"python{PV[0]}{PV[1]}._pth", sPath="Lib/site-packages"):
	try:
		import QOAI
		Paths = QOAI.__path__[0]
		del QOAI
	except ImportError:
		__main_path__ = os.path.dirname(__file__)
		file_name = __file__.split("/")[-1]
		Paths = os.getcwd()

	fPath = os.path.join(f"{pyPath}/{fPath}")
	import codecs as cds

	if not os.path.exists(fPath):
		return f"!! Not: {fPath}"
		

	with cds.open(fPath, "a+b", encoding="utf-8") as F:
		F.seek(1) # Move the file pointer to the beginning of the file

		if not sPath in F.read():
			F.writelines(f"\n{sPath}")
			Added = False
		else:
			Added = True

		F.close()

	return [Added,(f"OK. {sPath} has been added to: {fPath} configuration." if Added == True else os.environ.update({'PYTHONPATH':f"{os.path.join(pyPath,sPath)}:{os.environ.get('PYTHONPATH', '')}"}))]

def IIL(ln="", lfn="", im=True,sP='Lib/site-packages',MN='QOAI',Rs=False):
	try:
		import importlib as IL
		PM=sys.modules
		il = IL.import_module(ln)
		if(PM.get(ln)==None): print(f"{ln} imported.")
	except ModuleNotFoundError as exMessage:
		if im == True:
			print(f"Some required libraries are not installed! Trying to auto install: {exMessage.name} now... please wait.")
			try:
				IOS = subprocess.Popen(["python", "-m", "pip", "install", f"{exMessage.name if lfn == '' else lfn}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				_, error = IOS.communicate()

				if IOS.returncode == 0:
					print(f"Installation of library is done; waiting until reimport {ln} to  app.")
					if(SL(sPath=sP)[0]==False):
						#import sys,os
						if(Rs==True):
							os.system(f"{sys.prefix}/python -m {MN}")
							sys.exit()
						else:
							sys.path.append(os.path.join(pyPath,sP))
					return IIL(ln=ln, lfn=lfn, im=im)
				else:
					print(f"Could not installation library: {exMessage.name}; Error: {error.decode('utf-8')}")
					
			except FileNotFoundError as exMessage1:
				print(f"{exMessage1}    {pyPath}")

			except Exception as exMessage1:
				print(exMessage1)
		return [False, exMessage.name]
	else:
		return [True, il]

li = {"True": list(), "False": list()}
def CL(ln):
	global li

	if ln.count(",") != 0:
		for n in ln.split(","):
			print(f"Checking: {n} library.")
			cl = IIL(n)
			if cl[0] == True:
				li["True"].append(cl[1])
				print(f"{n} is installed.")
			elif cl[0] == False:
				li["False"].append(cl[1])
				print(f"{n} is not installed.")
			sleep(0.2)

	return li

if(__name__ == "__main__"):
	l = input("1. one library, 2. multiple libraries, 0 to exit.")

	if l == "1":
		IIL(input("Library name: "))
	elif l == "2":
		CL(input("Library names: "))
	else:
		exit(input("Thank you for using Qadary-Yemen's library. Press Enter to quit."))