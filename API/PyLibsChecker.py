# -*- coding: UTF-8 -*-
#Python Libraries manager.
## Developed by: QaYe<qadary-yemen> @2023


import sys,os,subprocess

pyPath=sys.prefix
PV=sys.version.split()
cwd=os.getcwd().replace("\\","/")
PM=cwd.split("/")[-1] #Import name of Director as Module Name

def SL(fPath=f"python{PV[0]}{PV[1]}._pth", sPath="Lib/site-packages",MN=PM):
	try:
		exec(f"import {MN} as Module")
		Paths = Module.__path__[0].replace("\\","/")
		exec(f"del {MN}")
	except ImportError:
		__main_path__ = os.path.dirname(__file__)
		file_name = __file__.replace("\\","/").split("/")[-1]
		Paths = cwd

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

Libs={} #store Libs whin imported as Name for Key and Module in Value
def IIL(ln="", lfn="", im=True,sP='Lib/site-packages',MN=PM,Rs=False):
	try:
		if(ln or lfn):
			import importlib as IL
			il = (Libs.get(ln) if Libs.get(ln)!=None else IL.import_module(ln))
		else:
			return IIL(ln=input("Library Name: "), lfn=input("Library FullName optional."), im=True,sP='Lib/site-packages',MN=PM,Rs=False)
	except ModuleNotFoundError as exMessage:
		if im == True:
			print(f"\n required  Library : {exMessage.name} . are not installed! Trying to auto installing  now... please wait.")
			try:
				IOS = subprocess.Popen(["python", "-m", "pip", "install", f"{exMessage.name if lfn == '' else lfn}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				_, error = IOS.communicate()

				if IOS.returncode == 0:
					print(f"Installation of library : {lfn} is done; waiting until reimport {ln} to  app.")
					if(SL(sPath=sP,MN=MN)[0]==False):
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
			except Exception as exMessage0:
				print(exMessage0)
		return [False, exMessage.name]
	else:
		if(Libs.get(ln)==None and il):
			Libs.update({ln:il})
			print(f"{ln} imported.")
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
		