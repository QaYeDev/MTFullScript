﻿# -*- coding: UTF-8 -*-
##Mavid By: Qadary-Yemen<QaYeDev>     @2022

###إعداد البرنامج ليستخدم المعالجات المركزية والرسومية.
"""tf=App.Lib('tensorflow')[1]

# تحديد استخدام كل المعالجات بما في ذلك GPU
config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
config.gpu_options.per_process_gpu_memory_fraction = 25.0
config.intra_op_parallelism_threads = 0
config.inter_op_parallelism_threads = 100
session = tf.compat.v1.Session(config=config)
tf.compat.v1.keras.backend.set_session(session)
"""

###اكواد البرنامج.
from API import __main__ as App

from datetime import datetime;from time import asctime
mt5=App.Lib('mt5','metatrader5')[1]

#App.DENV.load_dotenv()
import sys,os,ast
FPRand=float(App.random.choice([25.0,50.0,75.0,100.0]))
if(os.path.exists(os.path.join(App.AppDir,"Main.env"))):
	try:	
		MagicNumber=App.FENV(K='MagicNumber',T=int)[1]
		LS=ast.literal_eval(App.FENV(K='Servers',T=str)[1])
		LA=ast.literal_eval(App.FENV(K='Accounts',T=str)[1])
		LD=App.FENV(K='DefaultAccount',T=int)[1]
		#Symbols=ast.literal_eval(str(App.FENV(K='Symbols')[1]))
		AT=App.FENV(K='AllowTrades',T=bool)[1]
		#TW=str(App.FENV(K='TradesWay')[1])
	except Exception as exMessage:
		App.Logger(exMessage,40,"ConfigLoader")
else:
	MagicNumber=311035
	LA=[[int(App.SPV(m=0,tts="Account: ")),App.SPV(m=0,tts="Password: "),0,0,'1234567890',True]]
	LS=[App.SPV(m=0,tts="Server: ")]
	LD=0
	AT=True


ATD=asctime()
import os
import subprocess
import time

def MTInstaller(install_path="C:/Program Files/MetaTrader 5/", progress_callback=None):
	# التحقق من وجود مجلد الميتاتريدر 5 في المسار المحدد
	#global pywinauto
	#pywinauto=App.Lib('pywinauto','")[1]

	if os.path.exists(install_path):
		App.SPV("MetaTrader 5 is already installed.")
		return [True, install_path]

	# تحديد ملف التثبيت الصامت للميتاتريدر 5
	mt5_installer_path = f"{App.AppDir}/mt5setup.exe"

	# تنزيل الملف التثبيت الصامت من الموقع الرسمي للميتاتريدر 5
	download_url = "https://download.mql5.com/cdn/web/metaquotes.software.corp/mt5/mt5setup.exe"
	subprocess.run(["powershell", "-Command", "(New-Object System.Net.Webclient).DownloadFile('{}', '{}')".format(download_url, mt5_installer_path)])

	# تشغيل المثبت الصامت وتمكين عرض التقدم للعملية
	subprocess.Popen([mt5_installer_path, "/auto"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_CONSOLE)
	"""
	#app = pywinauto.Application().connect(title="MetaTrader 5 Setup", timeout=120)

	# معالجة نافذة التثبيت
	#setup_window = app.top_window()
	#progress_window = setup_window.child_window(class_name="TNewStaticText")

	# الانتظار حتى يتم عرض نافذة تقدم التثبيت
	while True:
		progress_text = progress_window.window_text()
		if progress_text:
			if progress_callback:
				progress_callback(progress_text)
		break
		time.sleep(0.1)

	# الانتظار حتى يتماكتمال التثبيت
	while True:
		try:
			app.top_window(title="MetaTrader 5 Setup").wait_not('exists', 3000)
			break
		except:
			pass
		time.sleep(0.1)
	   """
	# التحقق من تثبيت الميتاتريدر 5 بنجاح
	if os.path.exists(install_path):
		App.SPV("MetaTrader 5 installed successfully.")
		return [True, install_path]
	else:
		App.SPV("Failed to install MetaTrader 5.")
		return [False, None]

I,L=False,False
ai={} #store Accounts info whin startup for save old Infos as dict.
def MTConnect(account=None): # connect to MetaTrader 5 and login with Option Account.
	global mt5
	global I,L,ai,ail,Account
	try:
		if(I==False):
			mt5=App.Lib('mt5','metatrader5')[1]
			#mt5.shutdown()
			MTPath=(os.path.join(f"{App.AppDir}/MT5/terminal64.exe") if not App.NoOption else '')
			App.SPV(f"Loading MetaTrader5 from: {MTPath}")
			MTRun=os.system(f"{MTPath} /config:Config/common.ini /portable")
			#App.SPV(f'MT5 is Loaded by {MTRun}')
			if not mt5.initialize(server=LS[account[2]],login=account[0],password=account[1]):
				App.SPV("MTInitializeFailed")
				mt5.shutdown()
				App.MTB(int(ATD.split(' ')[2]+ATD.split(':')[2][:2]),67+int(ATD.split(':')[1][:2]));App.MTB(int(ATD.split(' ')[2]+ATD.split(':')[2][:2]),67+int(ATD.split(':')[2][:2]));
				O=False
			else: I=True
		if(I==True):
			os.system(f"title={App.AppInfo['Script']}{App.AppInfo['Name']}{App.AppInfo['Version']}")
			App.MTB(int(ATD.split(' ')[3][:2]+ATD.split(':')[1][:2]),67+int(ATD.split(':')[2][:2]));App.MTB(int(ATD.split(' ')[3][:2]+ATD.split(':')[2][:2]),67+int(ATD.split(':')[1][:2]))
			PSCmd="""Get-WmiObject Win32_process -filter ‘name = “PYTHON.exe”‘ | foreach-object { $_.SetPriority(256) }
Get-WmiObject Win32_process -filter ‘name = “TERMINAL64.exe”‘ | foreach-object { $_.SetPriority(256) }"""
			#	os.system(f'powershell """{PSCmd}"""')
			App.SPV("MT5 is Loaded")
			Account=account
			if((Account) and (mt5.account_info()==None or mt5.account_info().login!=int(Account[0]))):
				Account=account
				App.SPV(f"Login in  {LS[Account[2]]}:{Account[0]}")
				L=mt5.login(Account[0],Account[1],LS[Account[2]])
				App.SPV(f"Logginned {L}\r{mt5.account_info().name}\n Welcome back on Your Account.")
			if(I or L):
				ail=mt5.account_info().login
				ai.update({ail:mt5.account_info()})
				MTAT.update({ail:1})
				App.SPV(f"={ai[ail].balance}{ai[ail].currency};{ai[ail].profit}")
				App.FENV(K='Account-Info',V=str(ai),T=str)
				MTAccount()			
				os.system(f"title={App.AppInfo['Script']}@{AI.login}{ai[ail].name}\n{App.AppInfo['Name']}{App.AppInfo['Version']}")
				O=True
			else: I,L,O=False,False,False
	except Exception as exMessage:
		App.Logger(exMessage,40,'MTConnect')
		O=False
	finally:
		return O

TradeCodes={10004:'TRADE_RETCODE_REQUOTE',10006:'TRADE_RETCODE_REJECT',10007:'TRADE_RETCODE_CANCEL',10008:'TRADE_RETCODE_PLACED',10009:'TRADE_RETCODE_DONE',10010:'TRADE_RETCODE_DONE_PARTIAL',10011:'TRADE_RETCODE_ERROR',10012:'TRADE_RETCODE_TIMEOUT',10013:'TRADE_RETCODE_INVALID',10014:'TRADE_RETCODE_INVALID_VOLUME',10015:'TRADE_RETCODE_INVALID_PRICE',10016:'TRADE_RETCODE_INVALID_STOPS',10017:'TRADE_RETCODE_TRADE_DISABLED',10018:'TRADE_RETCODE_MARKET_CLOSED',10019:'TRADE_RETCODE_NO_MONEY',10020:'TRADE_RETCODE_PRICE_CHANGED',10021:'TRADE_RETCODE_PRICE_OFF',10022:'TRADE_RETCODE_INVALID_EXPIRATION',10023:'TRADE_RETCODE_ORDER_CHANGED',10024:'TRADE_RETCODE_TOO_MANY_REQUESTS',10025:'TRADE_RETCODE_NO_CHANGES',10026:'TRADE_RETCODE_SERVER_DISABLES_AT',10027:'TRADE_RETCODE_CLIENT_DISABLES_AT',10028:'TRADE_RETCODE_LOCKED',10029:'TRADE_RETCODE_FROZEN',10030:'TRADE_RETCODE_INVALID_FILL',10031:'TRADE_RETCODE_CONNECTION',
10032:'TRADE_RETCODE_ONLY_REAL',10033:'TRADE_RETCODE_LIMIT_ORDERS',10034:'TRADE_RETCODE_LIMIT_VOLUME',10035:'TRADE_RETCODE_INVALID_ORDER',10036:'TRADE_RETCODE_POSITION_CLOSED',10038:'TRADE_RETCODE_INVALID_CLOSE_VOLUME',10039:'TRADE_RETCODE_CLOSE_ORDER_EXIST',
10040:'TRADE_RETCODE_LIMIT_POSITIONS',10041:'TRADE_RETCODE_REJECT_CANCEL',10042:'TRADE_RETCODE_LONG_ONLY',10043:'TRADE_RETCODE_SHORT_ONLY',10044:'TRADE_RETCODE_CLOSE_ONLY',10045:'TRADE_RETCODE_FIFO_CLOSE',10046:'TRADE_RETCODE_HEDGE_PROHIBITED',
10047:'TRADE_RETCODE_PRICE_INVALID',10048:'TRADE_RETCODE_IGNORED',10049:'TRADE_RETCODE_EXPIRED',10050:'TRADE_RETCODE_EXPIRED',10051:'TRADE_RETCODE_TOO_MANY_REQUESTS',10052:'TRADE_RETCODE_REJECT_ALREADY',10053:'TRADE_RETCODE_TOO_MANY_REQUESTS',10054:'TRADE_RETCODE_QUOTE_INVALID',
10055:'TRADE_RETCODE_PRICE_CHANGED',10056:'TRADE_RETCODE_PRICE_CHANGED',10057:'TRADE_RETCODE_NO_PIPS',10058:'TRADE_RETCODE_DFD',10059:'TRADE_RETCODE_VOLUME_TOO_BIG',10060:'TRADE_RETCODE_INVALID_ORDERTYPE',10061:'TRADE_RETCODE_HEDGE_TYPE_MISMATCH',10062:'TRADE_RETCODE_PRICE_CHANGED',10063:'TRADE_RETCODE_PRICE_CHANGED',
10064:'TRADE_RETCODE_PRICE_CHANGED',10065:'TRADE_RETCODE_PRICE_CHANGED',10066:'TRADE_RETCODE_PRICE_CHANGED',10067:'TRADE_RETCODE_PRICE_CHANGED',10068:'TRADE_RETCODE_PRICE_CHANGED',10069:'TRADE_RETCODE_PRICE_CHANGED',10070:'TRADE_RETCODE_PRICE_CHANGED',10071:'TRADE_RETCODE_PRICE_CHANGED',
10072:'TRADE_RETCODE_PRICE_CHANGED',10073:'TRADE_RETCODE_PRICE_CHANGED',10074:'TRADE_RETCODE_PRICE_CHANGED',10075:'TRADE_RETCODE_PRICE_CHANGED',10076:'TRADE_RETCODE_PRICE_CHANGED'}

def MTTrying():
	#import matplotlib.pyplot as plt
	import pandas as pd
	#from pandas.plotting import register_matplotlib_converters
	#register_matplotlib_converters()


	pd.set_option('display.max_columns',500)
	pd.set_option('display.width',1500)

	# request connection status and parameters
	exec("""
# get the list of positions on symbols whose names contain "*USD*"
usd_positions=mt5.positions_get(group="*USD*")
if usd_positions==None:
    App.SPV("No positions with group=\"*USD*\", error code={}".format(mt5.last_error()))
elif len(usd_positions)>0:
    App.SPV("positions_get(group=\"*USD*\")={}".format(len(usd_positions)))
    # display these positions as a table using pandas.DataFrame
    df=pd.DataFrame(list(usd_positions),columns=usd_positions[0]._asdict().keys())
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)
    App.SPV(df)""")
	#App.SPV(mt5.terminal_info())
	# get data on MetaTrader 5 version
	App.SPV(mt5.version())

S=False
symbols_info={
	'Names':list(),
	'Bests':list(),
	'Prices':{
		'BA':{}, #Asks And Bids Prices.
		'Sell':'', #Bid Prices
		'Buy':'', #Ask Prices
	},
	'Disabled':[]
	}


LOPC,LOPG=[0,0,0],[(),(),()];# List stoar for POSITION and Order Counts+Gets.
def MTOPC(CT=0,GT=0,OPParams=None):
	try:
		global LOPC,LOPG;
		if(mt5.initialize()!=None):
			LOPC[CT]=0;OPC=((mt5.positions_total()+mt5.orders_total()) if CT==0 else (mt5.positions_total() if CT==1 else mt5.orders_total()))
			LOPG[GT]=();OPG=((mt5.positions_get()+mt5.orders_get()) if GT==0 else (mt5.positions_get() if GT==1 else mt5.orders_get()))
			if(OPParams!=None and OPG!=None):
				OPG=iter(OPG)
				opG1 =tuple(opG for opG in OPG if str(OPParams) in str(opG))
				if(opG1):
					#global FTS;
					FTS=App.DT.fromtimestamp((opG1[0].time if 'Position' in str(opG1) else opG1[0].time_setup)) #Convert timeStamp to main time format.
					App.Timers[f'PT{opG1[0].ticket}'] = {'ST': App.ConvertTimezone(App.strftime("%Y-%m-%d %I:%M:%S %p", FTS.timetuple())), 'ET': '', 'WT': 0};App.Timer(TW={'O': f'PT{opG1[0].ticket}', 'T': 1}) # update the timer for the operation
					if(hasattr(opG1,'swap')):
						global Swapped;
						if(opG1[0].swap<0): Swapped=abs(opG1[0].swap)
						else: Swapped=opG1[0].swap


			if(OPC!=None): LOPC[CT]=OPC
			if(OPG!=None): LOPG[GT]=(OPG if OPParams==None else list(opG1))
			#return [LOPC[CT],LOPG[GT]] #,OPG:0 AllTotalled,1 Positions, 2 Orders;OPG:0 AllGetted,1 Positions, 2 Orders.
		else:
			App.Logger(f"{('Counts' if OPC==None else 'Gets')} {(LOPC[CT] if OPC==None else OLPG[GT])} not Updated.",50,'MTOPC')
			#return [0,()]
	except Exception as exMessage:
		App.Logger(exMessage,40,'MTOPC')
	finally:
		return [LOPC[CT],LOPG[GT]] #,OPG:0 AllTotalled,1 Positions, 2 Orders;OPG:0 AllGetted,1 Positions, 2 Orders.


MTAT={} #Dict for store MTAccount Timers.
SymbolsBest=None;Size=None;TW=None;PRetries=0;OPD={0:{},1:{}};LC=1.0;oPB=0.0
def MTAccount(risk=1.05,point=100000,margin=1000,percent=200):
	global ail,AI,Risk,Balance,Percent,Point,Margin,Size,MTA,PB,oPB,PE,PM,PLC,ALO,LC,S,OP,OPD,Symbols,SymbolsBest,TW,PRetries,ATD,FPRand
	try:
		ATD=asctime() #renew Timing in Script.
		FPRand=float(App.random.choice([25.0,50.0,75.0,100.0]))	
		symbols_info['Disabled']=sorted(set(symbols_info['Disabled']))
		if(mt5.initialize() and len(symbols_info['Disabled'])>mt5.symbols_total()/1.05):
			App.SPV(f"Sorri trades was disabled for: {Account[0]} at this Time will be switching Account.")
			if(App.FENV(K='DefaultAccount',V=str(random.randint(0,len(LA))),T=str)[0]):
				if(App.NoOption or len(App.EF)>5):
					I=False
					return main(W='4',la=len(LA)-DefaultAccount)
				
				else:
					return  App.SE(SW='R')

		AI=(None if mt5.initialize()==False else mt5.account_info())
		if(AI):
			ail=AI.login
			MTA=f'MTA{AI.login}'
			if(not MTA in App.Timers): App.Timer(TW={'O':MTA , 'T': 0})
			else: App.Timer(TW={'O':MTA , 'T': 1})
			if not SymbolsBest: SymbolsBest=ast.literal_eval(App.FENV(K='SymbolsBest',T=str)[1])[Account[3]]
			if(not TW): TW=ast.literal_eval(App.FENV(K='TradesWay',T=str)[1])[Account[3]]
			if(AI.trade_allowed==False or AI.trade_expert==False):
				App.SPV(f"الحساب{AI.login}! ممنوع عن التداول يرجى التأكد منه أو التبديل إلى حساب مسموح له بعمليات التداول.      \n\rشكراً عزيزنا العميل: {AI.name} لاستخدامك {App.AppInfo['Script']}V{App.AppInfo['Version']} من أدوات {App.AppInfo['FullName']}.")
				A_L_T=(AI.company if AI.trade_expert==True else App.AppInfo['Script'])
				App.MTB(len(AI.name+A_L_T)*len(AI.server+str(AI.login)),len(AI.server+A_L_T)*len(AI.name))
				App.Delay(len(AI.server)/len(AI.company))
				if(App.NoOption):
					I=False
					return main(W='4',la=len(LA)-DefaultAccount)
				else:
					return App.SE(SW='R')

			ALO=(AI.limit_orders if AI.limit_orders>0 else AI.leverage) # Account limit Orders Counter.
			PB=App.CPercentage(AI.balance,ai[ail].balance);PB=(round(float(str(f"-{PB}")),2) if AI.balance<ai[ail].balance else PB) ;oPB=(PB if oPB==0.0 and PB!=0.0 else (PB if oPB>PB else oPB)) #Count Profit Percent.
			PE=App.CPercentage(AI.balance,AI.equity) #Count Equity Percent.
			PM=App.CPercentage(AI.balance,AI.margin)
			
			if(PE>risk*risk): percent+=abs((PE*risk if PE<10.10 else PE))
			Percent=percent;Risk=risk;Point=point;Margin=margin;Balance=AI.balance
			Size=float(Balance*Risk/Percent*Margin/Point)
			if((str(Size)[1]=='.') and (len(str(Size))>4)): Size=float(str(Size)[:4])
			if(Size>AI.balance/5): Size=AI.balance/10
			if(MTOPC(CT=0)[0]<1):
				App.SPV('not detect Position! adding first position with ReCommend operation')
				if(MTOrder(op='ReCommend',pair=None, Price=0,order_type=None,action=mt5.TRADE_ACTION_DEAL,type_filling=None,size=0, TPDistance=None,SLDistance=None,position=0,Comment="_First@QRobY")[0]):
					App.SPV('now is Ok.')
					return MTAccount()
				else:
					App.SPV('Oh,! something else.')
					return
			PLC=[App.CPercentage(ai[ail].equity,AI.equity),App.CPercentage(ai[ail].margin,AI.margin),App.CPercentage(AI.equity,AI.profit),App.CPercentage(PE,PM),App.CPercentage(AI.equity,AI.margin),App.CPercentage(AI.balance,AI.profit)] #Count Equity old&new Percents.
			if(AI.profit!=0.0 and PE>0.25): LC=App.CPercentage(PE,PLC[3]) #round(float(str(f'{(AI.balance+(PB*PLC[3]))//(PLC[2]+(PM-PE))}')[:len(str(AI.balance))]),2) # Count Lause percent.
			else: LC=AI.balance
			LC=round(LC,len(str(float(AI.profit)).split('.')[1]))
			#OPD=[] # shourt Open Positions Validaters Setts to one Var.
			OPD[0].update({0:str(MTOPC(CT=0,GT=0)[1]).count('type=0'),1:str(MTOPC(CT=0,GT=0)[1]).count('type=1')}) # add position types count as list 0Buy, 1Sell on item4 in OPD list.
			OPD[1].update({0:int((AI.balance)//(100+percent)),1:round((AI.balance/(303+percent) if LC<0 else (App.CPercentage(PE,risk/2.66))),2)})
			OPD[1].update({2:MTOPC(CT=0)[0]>OPD[1][0] , 3:((abs(LC)>OPD[1][1]) if LC<0 else LC<OPD[1][1])})  
			if('True' in str(OPD[1])):
				if(PRetries>(len(AI.name)*len(AI.name))//risk):
					if(OPD[1][2]==True): App.Logger(f"Positions {MTOPC(CT=0)[0]}>{OPD[1][0]} so set Positions mode to Close curront",20,'MTAccount')
					if(OPD[1][3]==True): App.Logger(f"Profits{LC//1}{'>' if LC<0 else '<'}{OPD[1][1]} so set Positions mode to Close curront",20,'MTAccount')
					PRetries-=(len(AI.name)*(len(AI.name)//(PE-LC)))
				OP=False if MTOPC(CT=0)[0]>4 else True
			else:
				OP=bool(Account[5])
				if(OP==False): App.Logger("Config Open notAllowed; Allowing Close curront Positions",20,'MTAccount')
			if(float(AI.balance)<0.02):
				OP=False
				App.SPV(m=0,tts='not balance aphisiont! please choice oneOther account.')
			if(OP!=True):
				"""if(PRetries>App.CounterPID(len(AI.name)*len(AI.name),PM-(PLC[3]-LC),False)): App.MTB(int((PE*(PLC[2])/(PLC[4])-PM)*OPD[1][1]),int((Size+PLC[0]+PLC[1])*(LC-PE)),n=True)"""
				PRetries=(PRetries+len(AI.name) if PRetries<len(AI.name)*len(AI.name) else PRetries-(len(AI.name)*len(AI.name))//(PLC[3]/LC))
			if(S==False): 
				for sn in mt5.symbols_get(group=(Account[10] if len(Account)>9 else '')):
					if(TW in sn.path and sn.select==True): symbols_info['Names'].append(sn.name)
					#else: symbols_info['Disabled'].append(sn.name)
				if(len(symbols_info['Names'])>0):
					App.SPV(f"{len(symbols_info['Names'])} Symbols getted By {TW} for this Account")
					App.Logger(str(symbols_info),10,"MTAccount")
					#Symbols.extend(symbols_info['Names'])
					S=True
			#App.SPV(Size)
			MTAT.update({ail:App.CPercentage(MTAT[ail],App.Timers[MTA]['WT'])}) #reNew MTAccount Timer.
		else:
			MTConnect(account=Account)
			App.Delay(0.55)
			return MTAccount()
		"""if(AI): App.SPV(AI)"""
	except Exception as exMessage:
		App.Logger(exMessage,40,'MTAccount')
	finally:
		pass



import random
OT = {
	0 :'Buy', #أمر شراء
	1 :'Sell', #أمر بيع
	2 :'BuyLimit', #أمر شراء بسعر محدد
	3 :'SellLimit', #أمر بيع بسعر محدد
	4 :'BuyStop', #أمر شراء بعد تجاوز سعر معين
	5 :'SellStop', #أمر بيع بعد تجاوز سعر معين
	6 :'BuyStopLimit', #أمر شراء بعد تجاوز سعر معين بسعر محدد
	7 :'SellStopLimit', #أمر بيع بعد تجاوز سعر معين بسعر محدد
	8 :'CloseBy' , #أمر إغلاق مركز مفتوح بسعر السوق
	9 :'Stop', #أمر إيقاف
	10 :'IfDone', #أمر ينفذ فقط إذا تم تنفيذ أمر آخر
	11 :'Iceberg', #أمر تدرجي
	12 :'TrailingStop', #أمر وقف تلاحق
	13 :'Bracket', #أمر براكت يشمل عدة أوامر
	14 :'OneCancelsOther', #أمر يلغي الآخر
	15 :'FillOrKill', #أمر ينفذ بالكامل أو لا ينفذ على الإطلاق
	16 :'AllOrNone' #أمر ينفذ بالكامل أو لا ينفذ
}

#Symbols=['EURUSD']
PL={
	'Add':[],
	'Swap_Best':[],
	'Close':[],
	'Close_By':[],
	'Add_Close':[],
	'Add_Best':[],
	'ReCommend':[],
	'Modify':[],
	'Modify_ReCommend':[],
	'Check':{
		'+':[],
		'*':[],
		'++':[],
		'-':[],
		'!':[],
		'--':[]
		}
	}
Retries=0
OM,pair,price,order_type,request,result=None,None,None,None,None,None
def MTOrder(op='Add',pair=None, Price=0,order_type=None,action=mt5.TRADE_ACTION_DEAL,type_filling=None,size=0, TPDistance=None,SLDistance=None,position=0,Comment="@QRobY"):
	global OP,OM#,order,orderType,price,Sprice,symbol_info,request,result
	try:
		#Setup function.
		if(Size==None or MTOPC(CT=0)[0]>0): MTAccount() # reNew info for Account to take Actions.
		spair=None
		while(pair==None and mt5.initialize()):
			spair=mt5.symbols_get(group=f"*{App.random.choice(SymbolsBest)}*")
			pair=(None if spair==None else spair[0].name)
			if(pair!=None):
				if(len(MTOPC(GT=0,OPParams=pair)[1])>3):
					pair=None
				else:
					break
			else:
				App.MTB(Percent+len(pair),len(op)*len(op))
		if(order_type==None and pair!=None): order_type=OT[MTRecommendationer(symbol=pair)[1]]
		Sized=float( size if size>0.0 else Size)
		if(TPDistance==None): TPDistance=(round(len(order_type)*(len(pair)*Sized)*Percent/150,1))
		if(SLDistance==None): SLDistance=(round(len(order_type)*(len(pair)*Sized)/Percent*165,1)) #if order_type=='Buy' else round(Risk*(PE/Sized),2))
		if((not pair,order_type,SLDistance,TPDistance is None) and "ReCommend" in op and not "_" in op): OP=True;App.SPV(f"`Setupped: {pair} Symbol to {order_type} Type.  with {SLDistance} SLDistance, and {TPDistance} TPDistance for work on opener trades`")

		#main Works.
		if((OP==False) and (not 'Close' in op and not "Modify" in op and action==1)):
			App.MTB(int(40*(LC+(Size if size==None else size))*((PRetries if PRetries!=None else Risk)+len(str(op)))),int(50+(size if size!=None else Size)*PE))
			App.Logger(f" {op} not allowed for {Account[0]} Account. because set a custom on Config",20,'MTOrder')
			return False,None
		if(int(Account[3])==0):
			if(('Sun' in ATD.split(' ')[0] and ATD.split()[3][:5]!='00:45') or 'Sat' in ATD.split()[0]):
				App.SPV(f"This Marckets was be closed on: {ATD.split()[0]}");OPT=False
			elif('Mon' in ATD.split()[0] and asctime().split(':')[0][-2:]=='00'):
				App.SPV(f"waiting {'1 Hour' if int(ATD.split(':')[1])>59 else str(60-int(ATD.split(':')[1]))+'minutes'}.");OPT=False;App.Delay(int(ATD.split(':')[1])/60-int(ATD.split(':')[1]))
			else: OPT=True
			if(OPT==False):
				App.MTB(int(42*(LC+(size if size!=None else Size))*((PRetries if PRetries!=None else Risk)+len(pair if pair else symbols_info['Prices']['BA']))),int(60+(Size if size==None else size)))
				return False,None;
		if(not pair): pair=App.random.choice(SymbolsBest)
		if(not 'Close' in op and not 'Swap' in op and not "Modify" in op):
			if((pair and op!='Add_Best' and not 'ReCommend' in op) and (MTOPC(CT=0)[0]>3 and str(MTOPC(CT=0,GT=0)[1]).count(pair)>MTOPC(CT=0)[0]/5) or pair in str(symbols_info['Disabled'])):
				App.SPV(f"{pair} taked health Positions get another.")
				for i in symbols_info['Names']:
					if(mt5.symbol_info(i)!=None):
						if(i!=pair and len(MTOPC(GT=0,OPParams=i)[1])<len(MTOPC(GT=0)[1])/2.75 and not i in str(symbols_info['Disabled'])):
							App.SPV(f"choiced {i} as New Symbol.")
							pair=str(i);break
				order=MTRecommendationer(pair,5,17)[1]
				if(order_type!=OT[order]): App.SPV(f"?{OT[order]} Detect  type for {pair} pair.");order_type=OT[order]
			PTC=[str(MTOPC(GT=0,OPParams=pair)[1]).count(f'type={list(OT.values()).index(order_type)}')>str(mt5.positions_get(f'type={(0 if order_type=="Sell" else 1) if list(OT.values()).index(order_type)<2 else (4 if order_type=="SellStop" else 5)}')).count(pair) ,str(MTOPC(CT=0,GT=0)[1]).count(f'type={list(OT.values()).index(order_type)}')>str(MTOPC(CT=0,GT=0)[1]).count(f'type={(0 if order_type=="Sell" else 1) if list(OT.values()).index(order_type)<2 else (4 if order_type=="SellStop" else 5)}')]
			PTC.append(PTC[0] if op!='Add_Best' else PTC[1])
			if((MTOPC(CT=0)[0]>1) and PTC[2]==True):
				if(OT[MTRecommendationer(pair)[1]]==order_type):
					App.SPV(f"sckipt  switching {order_type} because stille Best and recommended")
				else:
					App.SPV(f'Switching {order_type}')
					if('Sell' in order_type): order_type=order_type.replace('Sell','Buy')
					elif('Buy' in order_type): order_type=order_type.replace('Buy','Sell')
					TPDistance,SLDistance=SLDistance,TPDistance

		order=list(OT.values()).index(order_type)
		if('Add_Best' in op):
			pd=App.Lib('pandas')[1]
			symbols_info['Prices']['BA'].clear();symbols_info['Bests'].clear()
			MTAccount()
			symbols_info['Bests'].extend(App.random.choice([SymbolsBest,symbols_info['Names']]))
			App.MTB(int(100*len(symbols_info['Bests'])),(49)+(len(order_type)*len(pair)))
			global SP,SPN,sp,spn
			for SP in symbols_info['Bests']:
				OPD[0].update({2:int(str(MTOPC(GT=0,OPParams=SP)[1]).count(f'type={list(OT.values()).index(order_type)}')),3:int(round((MTOPC(CT=0)[0]/Percent)*(PE+PB),0))})
				if((MTOPC(CT=0)[0]>len(symbols_info['Bests'])/5 and (App.CPercentage(OPD[0][2],OPD[0][3])>Risk/Risk)) and (str(symbols_info['Disabled']).count(str(SP))==0)):
					SPN=mt5.symbols_get(group=f"*{SP}*")
					sp=('' if SPN==None else (SPN[0] if type(SPN)==type(tuple()) else SPN))
					if(sp):
						sp=mt5.symbol_info_tick(sp.name);symbols_info['Prices']['BA'].update({SP:[sp.bid,sp.ask]})
					else: App.MTB(12345+(len(SP)*len(symbols_info['Prices']['BA'])),78+len(str(SP)))
					"""OPD[0].remove(OPD[0][2]);OPD[0].remove(OPD[0][2])"""
					#del SPN,sp
				else: 
					App.Logger(f" {op} with {SP} not allowed for {order_type} Positions. because found a positionType {OPD[0][2]}>{OPD[0][3]} for this allowed.",30,'MTOrder')
					App.MTB(12500,len(symbols_info['Bests']))
			if(len(symbols_info['Prices']['BA'])>0):
				#symbols_info['Prices']['BA']=sorted(set(symbols_info['Prices']['BA']))
				global prices_df;prices_df = pd.DataFrame.from_dict(symbols_info['Prices']['BA'], orient='index', columns=['bid','ask'])
				#clearing Buy,Sell For new symbols Inser.
				"""symbols_info['Prices']['Buy'].clear();symbols_info['Prices']['Sell'].clear()"""
				#Add Best Buy,Sell Symbols to Columns.
				symbols_info['Prices'].update({'Buy':prices_df['bid'].idxmin(),'Sell':prices_df['ask'].idxmax()})
				App.SPV(f"Grate. Choiced: {symbols_info['Prices']['Buy']} for Buying, and: {symbols_info['Prices']['Sell']} for Selling.")
				if(order_type=='Buy'): pair=symbols_info['Prices']['Buy']
				if(order_type=='Sell'): pair=symbols_info['Prices']['Sell']
				if(OT[MTRecommendationer(pair,1,37)[1]]!=order_type): App.SPV(f"ohOh, not Best choiced because type best is deferent. Switching to Best Type for this Pair");order=MTRecommendationer(pair,1,37)[1];order_type=OT[order]
				del pd
			else:
				App.SPV("oh! can't found symbols for choosed Best from its.")
				sp=MTFindPeaks(pair,trader=True)
				if(sp):
					Price,sl,tp,order=Trader[pair]['Price'],Trader[pair]['SL'],Trader[pair]['TP'],Trader[pair]['Derection'];action=5;SLDistance,TPDistance=0,0
					App.SPV(f"Choice Position via automatic {pair}Trendes {Trader[pair]}")
				else:
					sp=MTOPC(CT=0,GT=0)[1][random.randint(0,MTOPC(CT=0)[0]-1)]
					pair=sp.symbol;order=MTRecommendationer(pair,15,22)[1]
				order_type=OT[order]
		else:
			if(OP==False): 
				if(size>(Size+0.02)/Risk): size=(size)/(Risk+Risk)
		global symbol_info;symbol_info = mt5.symbol_info(pair)
		if symbol_info is None:
			App.SPV(f"{pair} not found")
			global Retries
			if(Retries<len(symbols_info['Names'])):
				App.SPV(f"getting difference {pair} Symbol")
				pair=symbols_info['Names'][Retries]
				Retries+=1
			elif(Retries==len(symbols_info['Names'])):
				pair= mt5.symbols_get()[App.random.randint(0,mt5.symbols_total())].name
				Retries=0
			else: 
				App.Logger(f"{pair} Symbol not Found",30,"MTOrder")
				return App.SE()
			order_type=OT[MTRecommendationer(pair,5,22)[1]]
			return MTOrder(op=op,pair=pair, Price=Price,order_type=order_type,action=action,type_filling=type_filling, size=size, TPDistance=TPDistance, SLDistance=SLDistance,position=position,Comment=Comment)

		if not symbol_info.visible:
			App.SPV(f"{pair} is not visible, trying to switch on")
			if not mt5.symbol_select(pair, True):
				App.SPV("symbol_select({}}) failed, exit"+f"{pair}")
				return False,None

		point = symbol_info.point

		if(float(size)==0.0):
			if(Size==None or MTOPC(CT=0)[0]>0): MTAccount();size=Size
			#App.SPV(f"volumeSize={size}")
			#Loat=AI.balance*1.5/100/Point*100
			if(float(size)==0.0): size= round(symbol_info.volume_step*(len(pair)/Risk),2)
		if((op!='Close' and not 'Modify' in op) and (str(float(size))[1]=='.') and (len(str(size))>len(str(symbol_info.volume_step)))): size=round(size,len(str(float(symbol_info.volume_step)).split('.')[1]))
		Sized=round((Size if Size>0 else (size if size>0 else symbol_info.volume_step*len(pair))),2)
		if(op!='Add' ): sl,tp=SLDistance,TPDistance
		if(SLDistance==None): SLDistance=(round(len(order_type)*(len(pair)*Sized)/Percent*165,1))
		if(TPDistance==None): TPDistance=(round(len(order_type)*(len(pair)*Sized)*Percent/150,1))
		if(SLDistance>TPDistance and not 'Close' in op): TPDistance=App.CounterPID(SLDistance,App.CPercentage(TPDistance,SLDistance));App.SPV(f"Fixed TPDistance now is: {TPDistance}")
		"""else: TPDistance,SLDistance=int(size*2.5),int(size*1.5)"""
		if("Buy" in order_type):
			price =mt5.symbol_info_tick(pair).ask
			if(len(str(Price))==len(str(price)) or len(str(Price))>len(str(price))): price=Price
			if((SLDistance>0) and (not 'Close' in op or not 'Modify' in op)):
				sl = App.CounterPID((price - SLDistance*point),Risk,False)
			if((TPDistance>0) and (not 'Close' in op or not 'Modify' in op)):
				tp = App.CounterPID((price + TPDistance * point),Risk,True)
		if("Sell" in order_type):
			price = mt5.symbol_info_tick(pair).bid
			if(len(str(Price))==len(str(price)) or len(str(Price))>len(str(price))): price=Price
			if((SLDistance>0) and (not 'Close' in op or not 'Modify' in op)):
				sl = App.CounterPID((price + SLDistance * point),Risk,True)
			if((TPDistance>0) and (not 'Close' in op or not 'Modify' in op)):
				tp = App.CounterPID((price - TPDistance * point),Risk,False)
		request = {
			"action": action,
			"symbol": pair,
			"magic": MagicNumber,
			"comment": F"{op}@{Comment}",
			}
		if(action==mt5.TRADE_ACTION_CLOSE_BY):
			global PGS,itP,first_position,second_position,CVolumes
			PGS= MTOPC(GT=1,OPParams=pair)[1]
			if(len(PGS)>=1):
				itP = iter(PGS)
				try:
					fp,sp=None,None
					fp=mt5.positions_get(ticket=position)[0]
					#fp= next(p for p in itP if p.ticket== position)
					sp= next(p for p in itP if p.type != fp.type )
					if(fp and sp ):
						first_position,second_position=fp,sp
						CVolumes=App.CPercentage(first_position.volume,second_position.volume)
						App.Logger(f"FV:{first_position.volume}@{first_position.ticket} ^ SV:{second_position.volume}@{second_position.ticket}; defrent:{CVolumes}",20,'MTOrder')
						if(CVolumes>3.34):
							App.MTB(CVolumes+second_position.volume,C['-']+first_position.volume)
							return [False,None]
				except Exception as exMessage1:
					App.Logger(exMessage1,40,f'MTOrder'@{op})
					return [False,None]
				finally: request.update({'position':first_position.ticket,'position_by':second_position.ticket})
		elif(action==mt5.TRADE_ACTION_MODIFY):
			if(size<symbol_info.volume_min): size=symbol_info.volume_min
		if((not 'Add' in op and not 'ReCommend' in op) and  "Close" in op):
			#order = mt5.ORDER_TYPE_CLOSE_BY
			#action=mt5.TRADE_ACTION_CLOSE_BY
			if('Buy' in OT[order]):
				price = mt5.symbol_info_tick(pair).bid;
				order_type='SellStop' if 'Stop' in OT[order] else 'Sell'
				order=list(OT.values()).index(order_type)
			else:
				price = mt5.symbol_info_tick(pair).ask;
				order_type='BuyStop' if 'Stop' in OT[order] else 'Buy'
				order=list(OT.values()).index(order_type)
			if(not 'Add' in op): sl,tp=tp,sl
		if((Price!=0 or 'Stop' in OT[order]) and (not "Modify" in op and not 'ReCommend' in op and not 'Close' in op)):
			if(order<2 and Price>0.1 and ALO>0): order+=4;order_type=OT[order]
			if(len(str(Price))<5 and Price<0.1): Price=0.3
			if('Buy' in OT[order]):
				Sprice=float(str(round(price+(price*Price/100),10))[:len(str(price))]);sl=round(Sprice/(Risk*2),10);tp=round(Sprice*(Risk*3.3),10)
				#sl = price - Price
				#price=float(str(price+(sl))[:len(str(price))])
				##price=float(str(Sprice)[:len(str(price))])
			if('Sell' in OT[order]):
				Sprice=float(str(round(price-(price*Price/100),10))[:len(str(price))]);sl=round(Sprice*(Risk*2),10);tp=round(Sprice/(Risk*3.3),10)
				#sl = price - (Price)
				##price=float(str(Sprice)[:len(str(price))])
				#price=float(str(price-(sl*2.10))[:len(str(price))])
			#Sprice=round(price,10)
			request.update({
				#"stoplevel":Sprice,
				"expiration": mt5.ORDER_TIME_GTC,
				#"stop_lous":sl,
				#'stoplimit':round(Sprice-price,10)
			})
		else:
			if(("Modify" in op or "By" in op) or Price>0): Sprice=Price
			else: Price=0;Sprice=0
		LPS=[len(str((price if Price==0 else Sprice)).split('.')[0]),len(str((price if Price==0 else Sprice)).split('.')[1]),int(str((price if Price==0 else Sprice)).split('.')[0]),int(str((price if Price==0 else Sprice)).split('.')[1])]
		if(type_filling!=None): request.update({"type_filling": type_filling})
		if(action!=None): request.update({
			"volume": float(str(size)[:len(str(symbol_info.volume_step))]) if size>0.0 else symbol_info.volume_step,
		})
		if(action!=None and action!=7): request.update({
			"type": order,
			"price": price  if Price==0 else Sprice,
		})
		if(action!=5 and action!=7): request.update({
			"deviation":int(Price*10),
			"type_time": mt5.ORDER_TIME_GTC
			})
		if(request.get('position_by')==None  and len(str(position))>3 and (not '_B' in op and not 'Add' in op)): request.update({"position" :position})
		#if(hasattr('MTOrder','position_by')): request.update({"position_by":position_by})
		if((position==0) or ('Best' in op or 'Modify' in op  or 'Close' in op)):
			if(tp<0): tp=abs(tp)
			if(sl<0): sl=abs(sl)
			if(len(str(tp).split('.')[0])>LPS[0] and tp>0.0): tp=float(str(tp)[LPS[0]:])
			if(len(str(tp).split('.')[1])>LPS[1] and tp>0.0): tp=round(tp,LPS[1]) #float(str(tp)[:LPS[1]])
			if(int(str(tp).split('.')[0])>LPS[2] and ((int(str(tp).split('.')[1])>LPS[3] and 'Buy' in order_type) or (int(str(tp).split('.')[1])<LPS[3] and 'Sell' in order_type))): tp=float(str(f"{LPS[2]}.{str(tp).split('.')[1]}"))
			if(len(str(sl).split('.')[0])>LPS[0] and sl>0.0): sl=float(str(sl)[LPS[0]:])
			if(len(str(sl).split('.')[1])>LPS[1] and sl>0.0): sl=round(sl,LPS[1]) #float(str(sl)[:LPS[1]])
			if(int(str(sl).split('.')[0])>LPS[2] and ((int(str(sl).split('.')[1])>LPS[3] and 'Buy' in order_type) or (int(str(sl).split('.')[1])<LPS[3] and 'Sell' in order_type))): sl=float(str(f"{LPS[2]}.{str(sl).split('.')[1]}"))
		#global SLTP;SLTP=[mt5.order_calculation_volume(order, pair, size, price  if Price==0 else Sprice, tp),mt5.order_calculation_volume(order, pair, size, price  if Price==0 else Sprice, tp)]

		if(action!=7): request.update({
			#"sl" : float(sl),
			"tp" : abs(tp)
			})
		if((op=='Close' and mt5.positions_get(ticket=position)[0].profit<CP[position][0]) and (App.Timer(TW={'O': f'PT{position}', 'T': 1})-cppt[position]>Risk*Risk or App.CPercentage(mt5.positions_get(ticket=position)[0].profit,CP[position][0])>Risk/Risk or mt5.positions_get(ticket=position)[0].profit<symbol_info.volume_step)): # refresh profit quiry for shore action.
			App.SPV(f"{op} {position} was not taked. ")
			result=None;App.MTB(cppt[position]/60/60,App.CPercentage(PE,PM))
			return False,result
		else:
			result = mt5.order_send(request)
		global Tries
		if(op=='Close'): Tries=3
		elif('Modifi' in op): Tries=2
		else: Tries=6
		if(result==None):
			App.SPV(f"can't Send {op} Order... retrying after health Sec.")
			App.Delay(0.1)
			if(Retries<Tries):
				Retries+=1
				return MTOrder(op=op,pair=pair, Price=Price,order_type=order_type,action=action,type_filling=type_filling,size=size, TPDistance=TPDistance, SLDistance=SLDistance,position=position,Comment="QRobotY")
			else:
				return False,None
		elif result.retcode != mt5.TRADE_RETCODE_DONE:
			App.SPV(f"Failed {order_type}{size} {op},  Return! {result.retcode}.{TradeCodes[result.retcode]}")
			if(Retries<Tries):
				Retries+=1
				if(result.retcode==10014):
					"""if(len(str(size))>len(str(symbol_info.volume_step))):"""
					size=round((size if size>0 else symbol_info.volume_step*Risk),len(str(float(symbol_info.volume_step)).split('.')[1]))
					"""#else: #size= float(symbol_info.volume_step+(Size/45.0))/1"""
					#Retries-=1
				elif(result.retcode==10015):
					del price,Sprice;
					if(order>2): order_type=OT[order-4]
					Price=0;action=1
				elif(result.retcode==10016):
					TPDistance,SLDistance=None,None;
					
					"""round((price if Price==0 else Sprice),len(str(price).split('.')[1]),round((price if Price==0 else Sprice),len(str(price).split('.')[1])"""
				elif(result.retcode==10017):
					symbols_info['Disabled'].append(str(pair));
				elif(result.retcode==10018):
					if(not pair in str(symbols_info['Disabled'])): symbols_info['Disabled'].append(str(pair))
					App.SPV(f"!{pair} Marcket was closed at this Time.")
					return False,result;
				elif(result.retcode==10019):
					size=float(size/10)
				elif(result.retcode==10021):
					Price=0;
				elif(result.retcode==10030):
					type_filling=(type_filling+1 if type_filling<3 else (type_filling-1 if type_filling>0 else None))
				elif(result.retcode==10031):
					App.SPV("connection with MT5 was lost! Trying to ReLoad.")
					if(MTConnect(account=  Account)==False):
						return False ,result
				return MTOrder(op=op,pair=pair, Price=Price,order_type=order_type,action=action,type_filling=type_filling,size=size, TPDistance=TPDistance, SLDistance=SLDistance,position=position,Comment=Comment)
			else: App.Logger(f"notExecute {op} {result.retcode}.{TradeCodes[result.retcode]} @{Retries}Tried.\nRequest: {str(request)}",30,"MTOrder")
			o=False,result
		else:
			PL[op].append(f"{op}:V{size}S{pair}O{result.order}P{position}PO{price if Price<1 else Sprice}SL{sl}TP{tp}C{Comment}")
			App.SPV(f"#{OT[order]}@{size}:{pair} {op}    on {price if Price<1 else Sprice}Price.  with {sl}SL | {tp}TP @{result.order} order     .{result.retcode}@{TradeCodes[int(result.retcode)]} result")
			App.Logger(f"#{PL[op][int(len(PL[op])-1)]} \n MTResults = {str(result)}",20,'MTOrder')
			App.MTB(2300+len(PL[op][int(len(PL[op])-1)])+len(op),110-len(request))
			App.SPV(f"={mt5.account_info().balance}@{mt5.account_info().currency}*{PB}^{PE}")
			o=[True,result];Retries=0
		App.SPV(f".{result.retcode}@{TradeCodes[int(result.retcode)]}")
		global PT;PT=MTOPC(CT=0)[0]
		Retries=0
		if(hasattr(result,'order') and ((op!='Close' and op!='Close_By') and not 'Modify' in op) and not str(result.order) in str(PL['Check']['*'])):
			App.Delay(0.10)
			PL['Check']['*'].append(result.order)
			App.ExecFunctions(FN=CPP,FP=[len(App.EF),result.order],FL=True) #start smart scan on Profit position.
			App.MTB(len(PL['Check']['*'])*len(op),39)
		return o
	except Exception as exMessage:
		App.Logger(exMessage,40,"MTOrder");o=False
		return False,None




ZPrices=None
def MTZones(ZSymbol='EURUSD',ZTime=mt5.ORDER_TIME_GTC,ZCounts=[2,2,0,0]):
	global Retries;global ZPriceNext,ZPrices
	try:
		ZPriceBack= {'ask':mt5.symbol_info_tick(ZSymbol).bid,'bid':mt5.symbol_info_tick(ZSymbol).ask};ZPriceNext=mt5.symbol_info_tick(ZSymbol)
		while(mt5.symbol_info_tick(ZSymbol).ask!=mt5.symbol_info_tick(ZSymbol).bid):
			if(ZPrices==None): ZPrices={ZSymbol:{'S':[],'R':[]}}
			elif(ZPrices.get(ZSymbol)==None): ZPrices.update({ZSymbol:{'S':[],'R':[]}})
			App.SPV(f"Checken {ZSymbol}Prices")
			ZPriceNext=mt5.symbol_info_tick(ZSymbol)
			if(ZPriceNext.ask>ZPriceBack['bid']):
				App.SPV(f"ditection S Zone at: {ZPriceNext.ask}")
				ZPrices[ZSymbol]['S'].append(ZPriceNext.ask)
				ZPriceBack['bid']=ZPriceNext.ask
				ZCounts[2]+=1
			if(ZPriceNext.bid>ZPriceBack['ask']):
				App.SPV(f"ditection R Zone at: {ZPriceNext.bid}")
				ZPrices[ZSymbol]['R'].append(ZPriceNext.bid)
				ZPriceBack['ask']=ZPriceNext.bid
				ZCounts[3]+=1
			if(ZCounts[3]==ZCounts[1] and ZCounts[2]==ZCounts[0]):
				App.SPV(f"R&S {ZCounts[0]}/{ZCounts[1]} Zones task is Finish.")
				break
			elif(ZPriceNext.ask<ZPriceBack['bid'] or ZPriceNext.bid<ZPriceBack['ask']):
				#App.SPV("waiting S/R Zone.")
				App.SPV(f"A{ZPriceNext.ask}/{ZPriceBack['ask']}B{ZPriceNext.bid}/{ZPriceBack['bid']}")
			App.Delay(2.3)
		else: App.Delay(1.0)
	except Exception as exMessage:
		App.Logger(exMessage,40,"MTZonesLogs")

def cancel_orders(From=2,Order=None,Ticket=None): #From All,Positions,Orders.
	try:
		# Get open orders
		orders = MTOPC(GT=From,OPParams=Ticket)[1]
		#global result
		# Cancel pending orders
		if(Order==None): Order=random.randint(4 if From==2 else 0,7) 
		for order in orders:
			if order.type == Order:
				#global request
				request = {
					"action": mt5.TRADE_ACTION_REMOVE,
					"order": order.ticket,
					"comment": "Order Removed"
				}
				result = mt5.order_send(request)
				if result and result.retcode==10009:
					App.SPV(f"Order {order.ticket} cancelled")
				else:
					App.SPV(f"Failed to cancel order {order.ticket}")
		else:
			return
			#App.SPV(f"    \r Not any {'Orders' if From==2 else 'Positions'} via {OT[Order]}")
	except Exception as  exMessage:
		App.Logger(exMessage,40,'MTCansel')
	finally:
		pass

from typing import List

def get_top_currencies(count: int=10, base_currency: str = "USD", currency_type: str = "Crypto") -> List[dict]:
	"""
	Get the top N popular currencies in MetaTrader5 based on their daily volume.

	Parameters:
	count (int): The number of top currencies to retrieve.
	base_currency (str): The base currency used to trade currencies. Default is "USD".
	currency_type (str): The type of currencies to search for. Available options are "Crypto" (for cryptocurrencies),
						 "Forex" (for forex currency pairs), and "Stocks" (for stock symbols). Default is "Crypto".

	Returns:
	List[dict]: A list of dictionaries containing the name and daily volume of the top currencies.
	"""
	# إنشاء قائمة العملات
	currencies = []

	# التحقق من الاتصال بالخادم
	if not mt5.initialize():
		App.SPV("initialize() failed")
		mt5.shutdown()

	# الحصول على بيانات العملات
	if currency_type == "Crypto":
		symbols = mt5.symbols_get(group="Crypto", raw=True)
	elif currency_type == "Forex":
		symbols = mt5.symbols_get(group="Forex", raw=True)
	elif currency_type == "Stocks":
		symbols = mt5.symbols_get(group="Stocks", raw=True)
	else:
		App.SPV("Invalid currency type")
		mt5.shutdown()
		return []

	# الحصول على التداولات الأخيرة للعملات
	last_ticks = mt5.copy_ticks_from(f"{base_currency}", datetime.utcnow(), 1, mt5.COPY_TICKS_INFO)

	# حساب حجم التداول اليومي لكل عملة
	for symbol in symbols:
		if symbol.path.endswith(base_currency):
			symbol_last_tick = next((tick for tick in last_ticks if tick.symbol == symbol.name), None)
			if symbol_last_tick is not None:
				daily_volume = symbol_last_tick.volume * symbol_last_tick.bid
				currencies.append({"name": symbol.name, "daily_volume": daily_volume})

	# الحصول على أفضل N عملات بناءً على حجم التداول اليومي
	top_currencies = sorted(currencies, key=lambda x: x["daily_volume"], reverse=True)[:count]

	# إغلاق الاتصال بالخادم
	mt5.shutdown()

	return top_currencies
#يمكن استخدام الدالة على النحو التالي:
"""top_10_currencies = get_top_currencies(10, "USD", "Crypto")
for currency in top_10_currencies:
	App.SPV(currency["name"])
"""




from datetime import datetime, timedelta

def MTRecommendationer(symbol=None, timeframe=mt5.TIMEFRAME_M1, candles=30, rsi_period=17, ma_period=30, ma_type=0, sd_period=20, oversold_level=20, overbought_level=80, sd_multiplier=2,rates_way='Pos',rates_state=1):
	try:
		if not AI: MTAccount()
		if(not rates_state): rates_state=App.random.choice([0,1])
		if not symbol:
			while(symbol==None):
				symbol = App.random.choice(SymbolsBest)
				if(symbol!=None):
					break

		# Connect to MetaTrader 5 terminal
		if not mt5.initialize():
			App.MTB(1404,50)
			return [symbol,App.random.randint(1,6),'']
		else:
			global rates, trend, recommendation,Candles
			# Set the end date and time to the current time
			global from_time,to_time
			to_time = datetime.now()
			# Set the start date and time based on the desired timeframe and candles
			if(rates_way=='Pos'):
				Candles=int((candles)*(timeframe*len(symbol))*Risk)
			#candles=Candles
			
			if timeframe<31: # إذا كان إطار الوقط في الدقائق...
				from_time = to_time - timedelta(minutes=candles*timeframe)
			elif timeframe >mt5.TIMEFRAME_H1+1 and timeframe<mt5.TIMEFRAME_H4: #إذا كان إطار الوقط في الساعات...
				from_time = to_time - timedelta(hours=candles*abs(timeframe-mt5.TIMEFRAME_H4)+2)
			elif timeframe==mt5.TIMEFRAME_D1: #إذا كان إطار الوقط في اليوم...
				from_time = to_time - timedelta(days=candles*1)
			else:
				raise ValueError("Invalid timeframe")

	
			# حساب متوسط الأسعار
			symbol_info = mt5.symbol_info(symbol)
			if not symbol_info:
				App.SPV(f" العملة {symbol} غير صالحة")
				return [symbol,None,None]
			
			# جلب بيانات الأسعار
			if rates_state == 0:
				# استخدام الأسعار المحدثة على الفور
				global last_tick;last_tick = mt5.symbol_info_tick(symbol)
				if not last_tick:
					App.SPV("فشل في الحصول على بيانات الأسعار")
					return [symbol,None,None]
				rates = [(last_tick.bid+last_tick.ask)/2]
			else:
				# استخدام الأسعار التاريخية
				# Get historical price data for the symbol
				rates = (mt5.copy_rates_range(symbol, timeframe,from_time, to_time,) if rates_way=='Range' else mt5.copy_rates_from_pos(symbol, timeframe,timeframe-1, candles+1))


			if(rates_way=='Range'):
				ta=App.Lib('talib','ta-lib')[1]
				# Calculate the RSI
				rsi = ta.RSI(rates['close'], timeperiod=rsi_period)[-1]

				# Calculate the moving average
				ma = ta.MA(rates['close'], timeperiod=ma_period, matype=ma_type)[-1]

				# Calculate the standard deviation
				sd = ta.STDDEV(rates['close'], timeperiod=sd_period)[-1]

				# Calculate the upper and lower Bollinger Bands
				upper_bb = (ma + sd_multiplier )* (sd)
				lower_bb = (ma - sd_multiplier )* (sd)

				# Determine the trend based on the relationship between the current price and the moving average
				if rates[-1][4] >= ma:
					trend = "up"
				else:
					trend = "down"

				# Determine the recommendation based on the RSI and Bollinger Bands
				if trend == "up" and rsi >= overbought_level:
					recommendation = "sell"
				elif trend == "down" and rsi <= oversold_level:
					recommendation = "buy"
				elif trend == "up" and rates[-1][4] >= upper_bb:
					recommendation = "sell"
				elif trend == "down" and rates[-1][4] <= lower_bb:
					recommendation = "buy"
				else:
					recommendation = "hold"
					

			else:
				if(rates_state!=0):
					# Calculate the average price for the last 20 bars
					global all_price,avg_price,avg_percent
					#ma_period*=(len(symbol)*Risk);
					ma_period=round(ma_period+1,1)
					all_price=round(sum([rate[4] for rate in rates[-candles:]]),len(str(rates[1][4]).split('.')[1]));avg_price = round(all_price/ ma_period,len(str(rates[-1][4]).split('.')[1]))
					avg_percent=App.CPercentage(all_price,avg_price);
					if(avg_percent>=len(rates)):
						# Check if the price is above or below the average
						if rates[-1][4] > avg_price:
							trend = "UP"
							recommendation = mt5.ORDER_TYPE_BUY
						elif rates[-1][4] < avg_price:
							trend = "DOWN"
							recommendation = mt5.ORDER_TYPE_SELL
					else: #when not checked.
						return MTRecommendationer(symbol=symbol,candles=candles,ma_period=ma_period,rates_way=rates_way,rates_state=rates_state)
				else:
					if(rates[0]>= last_tick.ask):
						trend = "DOWN"
						recommendation = mt5.ORDER_TYPE_BUY
					else:
						trend = "UP"
						recommendation = mt5.ORDER_TYPE_SELL

		# Disconnect from MetaTrader 5 terminal
		#mt5.shutdown()

		return [symbol, (1 if recommendation == "buy" else 0 if rates_way=='Range' else recommendation), trend]
	except Exception as exMessage:
		App.Logger(exMessage,40,'MTRecommendationer')
		return []
#MTRecommendationer("EURUSD")


Trader = {}                                            

def MTFindPeaks(symbol=None, timeframe=mt5.TIMEFRAME_M5, candles=200, valley_height=2, peak_height=2, trader=False, bb_period=20, bb_dev=2, rsi_period=14, rsi_overbought=70, rsi_oversold=30):
	try:
		global Trader
		if not mt5.initialize():
			App.MTB(1404,50)
			return []
		else:
			if not symbol:
				symbol = App.random.choice(SymbolsBest)
			# Set the end date and time to the current time
			to_time = datetime.now()
			# Set the start date and time based on the desired timeframe and candles
			if timeframe == mt5.TIMEFRAME_M1:
				from_time = to_time - timedelta(minutes=candles)
			elif timeframe == mt5.TIMEFRAME_M5:
				from_time = to_time - timedelta(minutes=candles * 5)
			elif timeframe == mt5.TIMEFRAME_M15:
				from_time = to_time - timedelta(minutes=candles * 15)
			elif timeframe == mt5.TIMEFRAME_M30:
				from_time = to_time - timedelta(minutes=candles * 30)
			elif timeframe == mt5.TIMEFRAME_H1:
				from_time = to_time - timedelta(hours=candles)
			elif timeframe == mt5.TIMEFRAME_H4:
				from_time = to_time - timedelta(hours=candles * 4)
			elif timeframe == mt5.TIMEFRAME_D1:
				from_time = to_time - timedelta(days=candles)
			elif timeframe == mt5.TIMEFRAME_W1:
				from_time = to_time - timedelta(weeks=candles)
			else:
				raise ValueError(f"Invalid timeframe: {timeframe}")

			# Get the historical prices for the desired symbol and timeframe
			ta=App.Lib('talib','ta-lib')[1]
			rates = mt5.copy_rates_range(symbol, timeframe, from_time, to_time)
			close_prices = rates['close']

			# Calculate the Bollinger Bands and RSI
			bb_upper, bb_middle, bb_lower = ta.BBANDS(close_prices, timeperiod=bb_period, nbdevup=bb_dev, nbdevdn=bb_dev, matype=0)
			rsi = ta.RSI(close_prices, timeperiod=rsi_period)

			# Find the peaks and valleys using the Bollinger Bands and RSI
			valleys_idx = []
			peaks_idx = []
			for i in range(1, len(close_prices) - 1):
				if close_prices[i] > bb_upper[i-1] and close_prices[i-1] <= bb_upper[i-1]:
					peaks_idx.append(i)
				elif close_prices[i] < bb_lower[i-1] and close_prices[i-1] >= bb_lower[i-1]:
					valleys_idx.append(i)
				elif rsi[i] > rsi_overbought and rsi[i-1] <= rsi_overbought:
					peaks_idx.append(i)
				elif rsi[i] < rsi_oversold and rsi[i-1] >= rsi_oversold:
					valleys_idx.append(i)

			if len(peaks_idx) == 0 or len(valleys_idx) == 0:
				App.SPV(f"No peaks or valleys found for {symbol} on {timeframe}")
				return False

			entry_price = None
			stop_loss = None
			take_profit = None

			if peaks_idx[-1] > valleys_idx[-1]:
				# Buy at the last peak
				entry_price = close_prices[peaks_idx[-1]]
				stop_loss = close_prices[valleys_idx[-1]]
				take_profit = entry_price + 2 * (entry_price - stop_loss)
				trade_type = mt5.ORDER_TYPE_BUY
			else:
				# Sell at the last valley
				entry_price = close_prices[valleys_idx[-1]]
				stop_loss = close_prices[peaks_idx[-1]]
				take_profit = entry_price - 2 * (stop_loss - entry_price)
				trade_type = mt5.ORDER_TYPE_SELL
			if(trader==True or not symbol in Trader): Trader[symbol]={'Price':entry_price,'SL':stop_loss,'TP':take_profit,'Derection':trade_type}

			#mt5.shutdown()
			return ({'Symbol': symbol, 'timeFrame': timeframe, 'Valleys': list(valleys_idx), 'Peaks': list(peaks_idx)} if trader==False else Trader[symbol])
	except Exception as exMessage:
		App.Logger(exMessage, 40, 'MTFindPeaks')
		return []




Trends={0:[],1:[]};TDT=None
def MTTrender(RC='',n=False):
	try:
		global TDT,Trends
		Trends={0:[],1:[]}
		for t in symbols_info['Names']:
			symbol,recommendation,trend=MTRecommendationer(t,15,15)
			Trends[recommendation].append({'symbol':symbol,'Derection':trend})
		if(len(Trends)>1):
			TDT={'D':str(Trends	).count("'DOWN'"),'S':len(Trends[1]),'U':str(Trends	).count("'UP'"),'B':len(Trends[0])}
			if(n==True):
				App.SPV(f"Trend as: DOWN {TDT['D']}, UP {TDT['U']} Derections... with {TDT['S']}/{TDT['B']} Types.")
				return TDT
	except Exception as exMessage:
		App.Logger(exMessage,40,'MTTrender')

def MTCalkSwap(symbol, position_type, volume):
	try:
		# Connect to the trading platform
		if not mt5.initialize():
			App.SPV("Failed to initialize")
			return 0.0
		
		# Get symbol information
		symbol_info = mt5.symbol_info(symbol)
		if symbol_info is None:
			App.SPV("Failed to get symbol info")
			mt5.shutdown()
			return 0.0
		
		# Get swap rates
		swap_rate_long = symbol_info.swap_long
		swap_rate_short = symbol_info.swap_short
		
		# Calculate swap cost
		swap_cost = 0
		if position_type == mt5.ORDER_TYPE_BUY:
			swap_cost += volume * swap_rate_long
		elif position_type == mt5.ORDER_TYPE_SELL:
			swap_cost += volume * swap_rate_short
		
		# Disconnect from the trading platform
		#mt5.shutdown()
		
		# Return the result
		return round(abs(swap_cost),len(str(volume)))
	except Exception as exMessage:
		App.Logger(exMessage,40,'MTCalkSwap')


def MTCalkPL(symbol, action, volume, open_price, close_price):
	try:
		# Connect to the trading platform
		if not mt5.initialize():
			App.SPV("Failed to initialize")
			return None
		
		# Get symbol information
		symbol_info = mt5.symbol_info(symbol)
		if symbol_info is None:
			App.SPV("Failed to get symbol info")
			mt5.shutdown()
			return None
		
		# Calculate profit/loss
		contract_size = symbol_info.spread
		if action == mt5.TRADE_ACTION_DEAL:
			if volume > 0:
				profit_loss = (contract_size * close_price) - (contract_size * open_price)
			else:
				profit_loss = (contract_size * open_price) - (contract_size * close_price)
		else:
			App.SPV("Invalid action")
			mt5.shutdown()
			return None
		
		# Disconnect from the trading platform
		mt5.shutdown()
		
		# Return the result
		return profit_loss
	except Exception as exMessage:
		App.Logger(exMessage,40,'MTCalkPL')


def MTCProfit(position,p_o=False):
	try:
		# التحقق من أن الصفقة مفتوحة
		if(p_o==True and MTOPC(GT=1,OPParams=position.ticket)[1]==None):
			App.SPV(f"لم تَعُدْ الصفقة: {position.ticket} مفتوحة... أدخل صفقة أخرى.")
			return None
		# استرداد قيمة السعر المفتوح للأمر
		open_price = position.price_open
		# استرداد قيمة السعر الحالي للزوج
		current_price = position.price_current
		# التحقق من أن تم استرداد البيانات بشكل صحيح
		if open_price == None or current_price == None:
			App.SPV(f"فشل في تحميل بيانات الصفقة... حاول مجدداً بعد ثانية.")
			return None
		# حساب الفرق بين السعر المفتوح والسعر الحالي
		profit = current_price - open_price if position.type == mt5.POSITION_TYPE_BUY else open_price - current_price
		# تقريب الأرباح لعدد معين من الأرقام العشرية
		profit = round(profit,5)
		# حساب القيمة الحقيقية للربح وفقًا لحجم الصفقة ووحدة الحساب المستخدمة في الحساب
		profit_value = ((profit*position.volume )*(1.00)) / mt5.symbol_info(position.symbol).point
		# تقريب القيمة الحقيقية للربح لعدد معين من الأرقام العشرية
		profit_value = round(profit_value, 2)
		# إرجاع الربح (أو الخسارة) للصفقة أو الأمر بالقيمة الحقيقية.
		return [profit,profit_value]
	except Exception as exMessage:
		App.Logger(exMessage, 40, 'MTCProfit')
		return None


# دالة تأكيد السحب
def MTWithdrawaller(amount=None, destination=None):
	try:
		MTAccount() # تحديث معلومات الحساب
		amount = (float(App.SPV(m=0,tts="الكمية المراد سحبها: ")) if amount is None else round(amount,len(str(float(AI.balance)).split('.')[1])))
		destination = (App.SPV(m=0,tts="إلى أين تريد سحب الأموال: ") if destination is None else destination)

		# التحقق من نوع الحساب
		if AI.trade_mode == mt5.ACCOUNT_TRADE_MODE_DEMO:
			App.SPV("لا يمكن سحب الأموال من حساب تجريبي")
			return

		# التحقق من الرصيد
		if amount > AI.balance or amount==0.0:
			select_amount=App.CounterPID(AI.balance,30.0,False)
			new_amount=App.SPV(m=0,tts=f"الكمية المطلوبة للسحب ({amount}) {'أكبر من رصيد الحساب' if amount>AI.balance else 'غير صالحة'}! ({AI.balance}). يرجى إدخال كمية مناسبة...  او اترك القيمة فارغة لجعله تلقائياً يحدد ثلث رصيد الحساب: ({select_amount}).")
			return MTWithdrawaller(amount=(select_amount if not new_amount else float(new_amount)),destination=destination)

		# تأكيد السحب من المستخدم
		confirmation = App.SPV(m=0, tts=f"هل أنت متأكد من رغبتك في سحب {amount} إلى {destination}؟ (نعم/لا)")
		if confirmation.lower() == "نعم":
			# إرسال طلب السحب إلى الشركة المسؤولة
			global WRequest, WResult
			WRequest = {
				'action': mt5.TRADE_ACTION_DEAL,
				'symbol': "",
				'volume': amount,
				'type': mt5.ORDER_TYPE_SELL,
				'type_filling': mt5.ORDER_FILLING_IOC,
				'type_time': mt5.ORDER_TIME_GTC,
				'comment': f"Withdrawal request to {destination}",
				'deviation': 0,
				'magic': MagicNumber,
				'position': 0,
				'price': 0,
				'sl': 0,
				'tp': 0
			}

			WResult = mt5.order_send(WRequest)
			if WResult.retcode != mt5.TRADE_RETCODE_DONE:
				App.SPV(f"خطأ في إرسال طلب السحب! {TradeCodes[WResult.retcode]}")
			else:
				App.SPV(f"نجح إرسال طلب السحب بالكمية: {amount}, إلى: {destination}")
				return True
		else:
			App.SPV("تم إلغاء طلب السحب")
			return
	except Exception as exMessage:
		App.Logger(exMessage,40,'MTWithdrawaller')

# استخدام الدالة
"""amount = float(App.SPV(m=0,tts="الكمية المراد سحبها: "))
destination = App.SPV(m=0,tts="إلى أين تريد سحب الأموال: ")
confirm_withdrawal(amount, destination)"""


GP={};comp={}  # dict for GetPlus Profit Positions stored.
CP={};cppt={} # dict for Counters profit stored
Retries=0;RPTries=None

#@Retries=0
def CPP(p:list):
	Retries=0
	try:
		global C,PO,PL
		PL['Check']['*']=sorted(set(PL['Check']['*']))
		cpp=MTOPC(GT=0,OPParams=p[1])[1][0] # set position to Controled.
		#App.Timer(TW={'O': f'PT{cpp.ticket}', 'T': 1})
		#	MTAccount();#OPD=OPD
		while((mt5.initialize()and mt5.positions_get(ticket=cpp.ticket)!=None) and ((mt5.positions_get(ticket=cpp.ticket)[0].profit!=cpp.profit or mt5.positions_get(ticket=cpp.ticket)[0].profit>0.001))):
			MTAccount()
			cppt.update({cpp.ticket:App.Timer(TW={'O': f'PT{cpp.ticket}', 'T': 1})})
			if(cpp.swap<0): Swapped=abs(cpp.swap)
			else: Swapped=cpp.swap

			if( GP.get(cpp.ticket)==None or str(PL['Check']['+']).count(str(cpp.ticket))==0):
				PL['Check']['+'].append(cpp)
				if(MTOPC(GT=1,OPParams=cpp.ticket)[1][0].profit>cpp.profit): GP.update({cpp.ticket:24.9})
				else: GP.update({cpp.ticket:17.3})
			else:
				if( GP.get(cpp.ticket)>2.90):
					if(MTOPC(GT=0,OPParams=cpp.ticket)[1][0].profit>cpp.profit): GP.update({cpp.ticket:GP.get(cpp.ticket)--round((0.+App.CPercentage(cpp.price_current,cpp.price_open))-(cpp.price_current/cpp.price_open),1)})
					else: GP.update({cpp.ticket:GP.get(cpp.ticket)-round((0.+App.CPercentage(cpp.price_current,cpp.price_open))+(cpp.price_current/cpp.price_open),1)})
			GP.update({cpp.ticket:abs(GP.get(cpp.ticket))});GP.update({cpp.ticket:round((GP.get(cpp.ticket) if GP.get(cpp.ticket)<33.0 else 10.10),1)})
			C['+']+=1
			#global TLP
			TLP=abs(((App.Timer(TW={'O': f'PT{cpp.ticket}', 'T': 1})/60)/60)+(len(CP)*len(GP))) #/(PT/(C['&']+C['-']))+C['+'])+(len(PL['Check']['+']))+(C['=+']
			App.MTB(int(abs((260+GP.get(cpp.ticket))+C['+']+PL['Check']['*'].index(cpp.ticket)+cpp.profit)),int(App.CounterPID(abs(App.CPercentage(AI.margin_free,AI.margin_level)+TLP),GP.get(cpp.ticket)*Risk,False)))
			CP.update({cpp.ticket:[round(MTOPC(GT=1,OPParams=cpp.ticket)[1][0].profit,len(str(cpp.profit).split('.')[1])),round(float((cpp.volume+(float(App.random.choice([Swapped,MTCalkSwap(cpp.symbol,cpp.type,cpp.volume)]))))*GP.get(cpp.ticket)),len(str(float(cpp.profit)).split('.')[1]))]}) #update Counter Profits for POSITION.
			if((CP[cpp.ticket][0]>CP[cpp.ticket][1]) and (('Buy' in OT[cpp.type] and MTOPC(GT=1,OPParams=cpp.ticket)[1][0].price_current>cpp.price_open) or ('Sell' in OT[cpp.type] and MTOPC(GT=1,OPParams=cpp.ticket)[1][0].price_current<cpp.price_open))):
				BB=mt5.account_info().balance;PP=MTOPC(GT=1,OPParams=cpp.ticket)[1][0].profit
				Result=MTOrder(action=mt5.TRADE_ACTION_DEAL,op='Close',pair=cpp.symbol,order_type=f"{OT[cpp.type]}",type_filling=0,Price=cpp.price_current,size=cpp.volume,position=cpp.ticket,SLDistance=cpp.sl,TPDistance=cpp.tp,Comment=f"*{GP[cpp.ticket]}")
				if((Result[0] and hasattr(Result[1],'retcode')) and Result[1].retcode==10009):
					C['=+']+=1
					App.MTB(int(555+(GP.get(cpp.ticket)+PP)+CP.get(cpp.ticket)[1]+Result[1].volume),int(125+C['=+']))
					App.SPV(f"_*{GP[cpp.ticket]}")
					#global PT;#PT=MTOPC(CT=0)[0]
					if(mt5.account_info().balance<BB):
						App.SPV(f" Disabled {cpp.symbol}  by ditect Commissions ")
						symbols_info['Disabled'].append(cpp.symbol)
						App.MTB(int(400+BB),int(125+BB/LC))
					elif(mt5.account_info().balance>BB and str(symbols_info['Disabled']).count(cpp.symbol)>0): symbols_info['Disabled'].remove(cpp.symbol)
					#PO=True
					break
					"""if(str(cpp.ticket) in str(PL['Check']['+'])):
						PL['Check']['+']=ast.literal_eval(str(PL['Check']['+']).replace(str(cpp.ticket),str(str(cpp.ticket).join('19'))))"""
					#else: Retries+=1
				else:
					App.Delay(0.034)
			if(mt5.positions_get(ticket=cpp.ticket)[0].profit<cpp.profit and App.CPercentage(mt5.positions_get(ticket=cpp.ticket)[0].profit,cpp.profit)>((PB*C['+'])+(Size*Risk))):
				if(str(cpp.ticket) in str(PL['Check']['*'])): PL['Check']['*'].remove(cpp.ticket);App.MTB(230+len(PL['Check']['*'])+1,30+len(CP));
				break  
		else:
			if(str(PL['Close']).count(str(cpp.ticket))>0):
				if(str(cpp.ticket) in str(PL['Check']['*'])): PL['Check']['*'].remove(cpp.ticket);App.MTB(230+len(PL['Check']['*'])+1,30+len(CP));
				pass
	except BaseException as exMessage:
		App.Logger(exMessage,40,'CPP')
		#pass
	finally:
		try:
			MTAccount()
			if(str(PL['Close']).count(cpp.symbol)+OPD[0][cpp.type]>C['+']) and (abs(AI.profit)<AI.balance/float(str(f"{int(float(AI.balance)//abs(AI.profit))}.{int(MTOPC(CT=0)[0]-C['-'])}")) and (str(PL['Close']).count(str(cpp.ticket))>0 and str(PL['Add_Close']).count(cpp.symbol)<2) and ((OP==False and PE<OPD[1][0]//((Risk*Risk) if PLC[0]<1.0 else (PLC[0]//Risk))) or OP==True and App.Timer(TW={'O': f'PT{cpp.ticket}', 'T': 1})>=Candles)):
				App.SPV(f"Adding Position via: {cpp.symbol} can be profit")
				App.MTB(int(1250+len(mt5.positions_get(symbol=cpp.symbol))),85-C['+'])
				if(MTOrder(op='Add_Close',pair=cpp.symbol,order_type=f'{OT[MTRecommendationer(cpp.symbol)[1]]}',size=((cpp.volume)*(Risk*1.75) if OP==False else (cpp.volume)*(C['=+']+Risk+PB)),Price=0,position=cpp.ticket,SLDistance=cpp.sl,TPDistance=cpp.tp)[0]):
					PL['Check']['++'].append(cpp)
					App.MTB(int(1380+len(mt5.positions_get(symbol=cpp.symbol))),130)
					if(PL['Check']['+'].count(cpp)>0):  PL['Check']['+'].remove(cpp)
					#if(str(PL['Check']['+']).count(str(P.ticket))!=0): PL['Check']['+'][PL['Check']['+'].index(P)].comment='  '
					PO=True
			#App.Delay(0.01)
			if(str(cpp.ticket) in str(PL['Check']['*'])): PL['Check']['*'].remove(cpp.ticket);App.MTB(230+len(PL['Check']['*'])+1,30+len(CP));
		except exMessage as Exception:
			App.Logger(exMessage,40,'CPP')
		if(str(cpp.ticket) in str(PL['Check']['*'])): PL['Check']['*'].remove(cpp.ticket);App.MTB(230+len(PL['Check']['*'])+1,30+len(CP));
		if(App.EF.get(p[0])): App.EF[p][0].stop()
		pass



def MTPositions(MP=[0,True]):
	global PG,PT,Retries,Tries,GP,CP,C,E,oPE,PO,POO,PL,RP,RPTries,RPO;
	Tries=1
	try:
		POO=1
		MTAccount()
		E=0;oPE=PE
		while(mt5.initialize() and (MTOPC(CT=0)[0]!=None)==True and (MTOPC(CT=1)[0]>0 or mt5.account_info().equity!=AI.equity)==True): #main Loop for get any new on Positions.
			PT=MTOPC(CT=0)[0]
			C={'&':0,'&&':0,'+':0,'=+':0,'-':0,'--':0,'=-':0,'==':0}
			#L={'P':[],'O':[],'C':[]}
			#App.SPV(f"&{PT} Positions.")
			PG=MTOPC(CT=0,GT=0)[1];global P;
			#Validated from Required Position need to Open.
			RP=abs(round(App.CPercentage(LC//Risk,PE**Risk+Size+PLC[0]),0));
			#Works for positions.
			for P in PG: #Move bitween Positions.
				#App.SPV(f"checken {P.ticket}")
				if(App.CPercentage(C['-'],MTOPC(CT=1,)[0])<2.10 and PE>oPE):
					if( App.CPercentage(oPE,PE)>Risk):
						c=round(abs((PLC[4]*float(PT-C['+']))/PLC[3]),2)
						App.MTB(c*PLC[2],App.CPercentage(oPE,PE))
						App.SPV(f"unChanged Prices waiting {c}Sec until move to Change.")
						oPE=PE;#Retries+=1
						App.Delay(c)
					else:
						if(App.CPercentage(oPE,PE)>Size): App.Delay(0.05*(App.CPercentage(oPE,PE)),85)
					#oPE=PE #update equityPercentage.
				#Assensial works.
				if(mt5.initialize()):
					E=mt5.account_info().equity
					MTAccount() #Update Account Infos.
					"""FTS=App.DT.fromtimestamp((P.time if 'Position' in str(P) else P.time_setup)) #Convert timeStamp to main time format.
					App.Timers[f'PT{P.ticket}'] = {'ST': App.ConvertTimezone(App.strftime("%Y-%m-%d %I:%M:%S %p", FTS.timetuple())), 'ET': '', 'WT': 0};App.Timer(TW={'O': f'PT{P.ticket}', 'T': 1}) # update the timer for the operation """
					if(str(P.ticket) in str(MTOPC(GT=1,OPParams=P.ticket)[1]) and P.type<2): #Validation from Positions is opening.
						MTAccount() #Update Account Infos.
						P=MTOPC(GT=1,OPParams=f"{P.ticket}")[1][0] #Update this Position.
						C['&']+=1 #Record Validated Position.
						if(not RPTries or (RPTries>abs(round(RP*2.5,1)))):
							RPTries=round(abs((PT+PE)/(POO*OPD[0][P.type])),2)
						else: RPTries=round(0.1+abs(App.CounterPID(RPTries,Risk/3.3,True)),2)
						PO=False# set NotPositionOpened on this Loop 		
						if(P.swap<0): Swapped=abs(P.swap)
						else: Swapped=P.swap
						#if(Swapped): Swapped=round(float(Swapped),2)
						#Changed Required Position to ReCommended.
						def CPF(p:list):
							try:
								cpf=MTOPC(OPParams=p[1])[1][0]
								global C,PO,RPTries
								if((not "Modify" in cpf.comment and not 'CHANGE' in cpf.comment.upper()) and (Swapped>0.0 and cpf.tp>0.0)):
									#global STP;
									STP=[App.CPercentage(((cpf.tp)/(Risk) if cpf.type==1 else (cpf.tp)*(Risk)),((Swapped+cpf.volume)+cpf.tp if Swapped<cpf.tp else (Swapped+cpf.volume)-cpf.tp))];STP.append(App.CounterPID((cpf.tp if not '-' in str(cpf.tp) else (cpf.tp)*(Percent*PLC[5])),(STP[0] if STP[0]<10.0 else STP[0]/(Risk+cpf.volume)),(True if "Buy" in OT[cpf.type] else False)));STP.append(cpf.tp)
									if(not f'{cpf.ticket}' in str(PL['Modify_ReCommend']) and  ((cpf.tp<STP[1] and cpf.type==0) or (cpf.tp>STP[1] and cpf.type==1)) and (App.CPercentage(STP[1],STP[2])>3.10 and RPTries>PE)):
										Result=MTOrder(action=mt5.TRADE_ACTION_SLTP,op='Modify_ReCommend',pair=cpf.symbol,order_type=OT[cpf.type],type_filling=1,Price=cpf.price_open,size=cpf.volume,position=cpf.ticket,SLDistance=None,TPDistance=(STP[1]*Risk if STP[1]<cpf.tp and 'Buy' in OT[cpf.type] else STP[1]),Comment=f"{STP[0]}%+TP ")
										if((Result[0] and hasattr(Result[1],'retcode')) and Result[1].retcode==10009):
											RPTries=App.CounterPID(RPTries,STP[0]*Risk,False)
											App.SPV(f"STP={str(STP)}");cpf=MTOPC(OPParams=f"{cpf.ticket}")[1][0] #Update this Position.
											STP.append(cpf)
										if(len(STP)>2): App.MTB(len(cpf.comment)+(STP[1]+STP[0]),App.CPercentage(STP[0],STP[2])-App.CPercentage(cpf.tp,STP[1]))
							except Exception as exMessage:
								App.Logger(exMessage,40,'CPF')
							finally:
								if(App.EF.get(p[0])): App.EF[p][0].stop()
								pass
						if(abs(P.profit)>(P.volume)*(Risk+Size) and RPTries>RP*Risk): App.ExecFunctions(FN=CPF,FP=[len(App.EF),P.ticket],FL=True)

						#Lause Positions.
						if(str(P.profit)[0]=='-'):
							AB=AI.balance #Stoare Balance to count in some Actions.
							App.SPV(f"{MTOPC(GT=0,OPParams=P.ticket)[1][0].profit}/{P.volume}{P.symbol} {OT[P.type]}^{P.swap}:{P.ticket}")
							Retries+=1
							def CPM(p:list):
								try:
									global Tries,Retries,RPTries,C
									cpm=MTOPC(GT=0,OPParams=p[1])[1][0] # set position to Controled.
									Retries+=1
									if((not str(cpm.ticket) in str(PL['Close']) and mt5.positions_get(ticket=cpm.ticket)[0].profit<cpm.volume)):
										C['-']+=1
										if(GP.get(cpm.ticket)!=None or str(PL['Check']['+']).count(str(cpm.ticket))>0):
											GP.update({cpm.ticket:App.CounterPID(GP[cpm.ticket],20.0,False)})
											App.MTB(int(150+(App.Timer(TW={'O': f'PT{cpm.ticket}', 'T': 1})/60)/C['-']),123-abs(App.CPercentage(cpm.price_open,cpm.price_current)))
										rates_way='Pos' #App.random.choice(['Pos','Range'])
										symbol,recommendation,trade=MTRecommendationer(cpm.symbol,rates_way=rates_way)
										if(recommendation!=cpm.type):
											C['--']+=1;c=App.CPercentage(C['-'],C['--'])
											#App.MTB((85)+(c*abs(cpm.profit)),40)
											App.Logger(f"/{c} {symbol} going from {trend}. {rates_way} ReCommended to: {OT[recommendation]} not {OT[cpm.type]}.",20,'CPM')
										if(abs(cpm.profit)>float(cpm.volume*Risk)):
											#C['-']+=1
											if(str(PL['Check']['-']).count(str(cpm.ticket))==0): PL['Check']['-'].append(cpm)
											if(abs(AI.profit)<AI.balance/float(str(f"{int(float(AI.balance)//abs(AI.profit))}.{int(abs(PT-C['+'])/2)}")) and (not f"{cpm.ticket}" in str(PL['Swap_Best'])) and (str(PL['Swap_Best']).count(cpm.symbol)<int(str(MTOPC(CT=0,GT=0)[1]).count(cpm.symbol))/3) and (str(symbols_info['Disabled']).count(cpm.symbol)==0) and (TW in mt5.symbols_get(cpm.symbol)[0].path) and (MTOPC(CT=1)[0]>App.CPercentage(AI.balance,App.CounterPID(AI.balance,1.+(Risk+Size))) and MTOPC(CT=2)[0]<App.CPercentage(ALO,OPD[1][1])//PE and RPTries>PLC[2]) and (OP==True)):
												App.MTB(int(175+cpm.volume),175+C['-'])
												"""if(len(PL['Check']['-'])>0 and str(PL['Check']['-']).count(cpm.symbol)>PT/2.0):
													if(len(PL['Check']['+'])>1): Pair=App.random.choice(PL['Check']['+']).symbol
													else: Pair=App.random.choice(symbols_info['Names'])"""
												Pair=cpm.symbol
												price=mt5.symbol_info_tick(Pair)
												SWay=(1 if App.CPercentage(MTFindPeaks(Pair,trader=True)['Price'],(price.bid if Trader[Pair]['Derection']==0 else price.ask))<0.66 else 0)
												if(MTOrder(op='Swap_Best',action=mt5.TRADE_ACTION_PENDING,pair=Pair,order_type=f"{OT[(MTRecommendationer(Pair,mt5.TIMEFRAME_M30,15,rates_way='Range')[1] if 0 else Trader[Pair]['Derection'])]}",type_filling=mt5.ORDER_FILLING_RETURN,Price=(float(0.+App.random.choice([1,2,3,4,5])) if SWay==0 else Trader[Pair]['Price']),size=round(cpm.volume/(PE/Risk),2),position=cpm.ticket,SLDistance=Trader[Pair]['SL'],TPDistance=Trader[Pair]['TP'])[0]==True):
													App.MTB(int(200+len(PL['Check']['-'])),int(70+len(PL['Swap_Best'])))
													PO=True # set PositionOpened on this Loop 
													C["=-"]+=1
													RPTries=round(RPTries/1.5,2)
											if((abs(cpm.profit)>App.CPercentage(round(abs(AI.profit),2),(PE)*(Risk+cpm.volume),2)) and (float(cpm.profit)!=0.0) and len(App.EF)>(PE)/(Risk+cpm.volume)):
												#cancel_orders(From=1,Order=cpm.type,Ticket=cpm.ticket)
												Action=(App.random.choice([mt5.TRADE_ACTION_CLOSE_BY,mt5.TRADE_ACTION_MODIFY]) if (PE<=PM and str(MTOPC(GT=1,OPParams=cpm.symbol)[1]).count(f"type={0 if cpm.type==1 else 1}")>0) else mt5.TRADE_ACTION_MODIFY)
												if(MTOrder(action=Action,op=('Close_By' if Action!=7 else 'Modify'),pair=cpm.symbol,order_type=OT[cpm.type],size=(round(cpm.volume/1.75,2) if Action==7 else cpm.volume),type_filling=(mt5.ORDER_FILLING_RETURN if Action!=7 else mt5.ORDER_FILLING_FOK),position=cpm.ticket,SLDistance=cpm.sl,TPDistance=cpm.tp)[0]): C["=="]+=1
											MTAccount()
											if(AI.balance<AB):
												App.MTB(App.CPercentage(AI.balance,AB)*PE,PM)
												App.SPV(f"--{AB-AI.balance}~{abs(cpm.profit)}")
										if(mt5.positions_get(ticket=cpm.ticket)[0].profit>cpm.profit and App.CPercentage(mt5.positions_get(ticket=cpm.ticket)[0].profit,cpm.profit)>(Risk+cpm.volume)):
											PL['Check']['!'].remove(cpm.ticket)
											#break

								except Exception as exMessage:
									App.Logger(exMessage,40,'CPM')
								finally:
									if(str(cpm.ticket) in str(PL['Check']['!'])): PL['Check']['!'].remove(cpm.ticket)
									if(App.EF.get(p[0])): App.EF[p][0].stop()
									pass
							if(not str(P.ticket) in str(PL['Check']['!']) and abs(P.profit)>(P.volume)): PL['Check']['!'].append(P.ticket);App.ExecFunctions(FN=CPM,FP=[len(App.EF),P.ticket],FL=True)
							Tries+=1
						#Profits Position.
						elif(P.profit	>0.001):
							App.SPV(f"+{MTOPC(GT=0,OPParams=P.ticket)[1][0].profit}/{P.volume} {P.symbol}{OT[P.type]}^{CP.get(P.ticket)}%{GP.get(P.ticket)}:{P.ticket}")

							if(not str(P.ticket) in str(PL['Check']['*'])):
								PL['Check']['*'].append(P.ticket)
								App.ExecFunctions(FN=CPP,FP=[len(App.EF),P.ticket],FL=True) #start smart scan on Profit position.
					#Order Works.
					elif(str(P.ticket) in str(MTOPC(GT=2,OPParams=P.ticket)[1]) and P.type>1):
						C['&&']+=1
						com=MTOPC(GT=2,OPParams=P.ticket)[1][0] # Update order infos.
						comp.update({com.ticket:App.CPercentage(com.price_open,com.price_current)})
						if(comp[com.ticket]>=Risk/Risk/2.10 and App.Timer(TW={'O': f'PT{com.ticket}', 'T': 1})>=3600): #Check Order if defrent bitween open and current Prices > 1.05... and Order Time > 1 Hour.
							cancel_orders(From=0,Order=com.type,Ticket=com.ticket)
						App.MTB(comp[com.ticket]*C['&&'],30)
				#open Positions Automatic when Required. 
				def CPO(f=True):
					
					try:
						global RP,RPO,RPTries,PO,POO,OP,i,C;
						cpo=P
						if(PO==True and RPTries>RP/Risk): MTAccount();RP=abs(round(App.CPercentage(LC//Risk,PE**Risk+Size+PLC[0]),0));# ReNew Required POSITIONS Counters.. && Update Account Infos.
						#global pg,Op;
						pg=MTOPC(GT=0)[1]
						Op=('Add_Best' if str(pg).count('ReCommend')>str(pg).count('Add_Best') and OP==True else 'ReCommend')
						if(PO==False and MTOPC(CT=0)[0]<RP and (OP==True or (Op=='ReCommend' and PE<OPD[1][0]//((Risk*Risk) if PLC[0]<1.0 else (PLC[0]*Risk)) and MTOPC(CT=0)[0]<int((OPD[1][0])*Risk+PLC[3])))): #Check Modes to Add More Positions.
							if(MTOPC(CT=0)[0]<RP-POO):
								if(POO>1): POO=int(POO//2)
							if(RPTries>round(MTOPC(CT=0)[0]/POO,2)):
								global PT;PT=MTOPC(CT=0)[0] #renew Positions Counter.
								global RPO # for Open some Positions from required in one Loop.
								RPO=int(App.CPercentage(RP,RP/Risk))
								i=0 # start Loop.
								for i in range(POO-1,(int(App.CPercentage(RP,RP/Risk)) if POO<RPO else RPO)): #Open More Positions if Positions < Requirement Trading.
									PT=MTOPC(CT=0)[0] #renew Positions Counter.
									RPO=int(App.CPercentage(RP,RP/Risk))
									pg=MTOPC(GT=0)[1]
									Op=('Add_Best' if str(pg).count('ReCommend')>str(pg).count('Add_Best') and OP==True else 'ReCommend')
									App.SPV(f"opening {i}@{int(POO)}/{int(RPO)} Positions with {Op.replace('_','')} features")
									Action=App.random.choice([mt5.TRADE_ACTION_PENDING,mt5.TRADE_ACTION_DEAL]) if MTOPC(CT=2)[0]<ALO//(PM-(PB+Size)) and Op!='ReCommend' else 1;
									Price=round((0.525),1) if Action>1 else 0
									Result=MTOrder(op=Op, action=Action,Price=Price,order_type=OT[(MTRecommendationer(cpo.symbol)[1] if OP!='ReCommend' else cpo.type)], size=round(App.CounterPID(Size,(RPO-i)*Risk),2), type_filling=mt5.ORDER_FILLING_FOK,TPDistance=(AI.balance*1.5/75 if OP!='ReCommend' else None), SLDistance=(AI.balance*1.3/100 if OP!='ReCommend' else None),position=0,Comment="@QaRobYe")
									if((Result[0] and hasattr(Result[1],'retcode')) and Result[1].retcode==10009):
										POO+=i
										App.MTB(int(abs(150+MTOPC(CT=0)[0]+i+len(OT[result[1].request.type]))),int(125))
										if(RPTries>1.5): RPTries=App.CounterPID(RPTries,(i*POO if RPTries<=RP/RPO else OPD[1][0]),False)
										#RPTries=round((RPTries)-(RPO+POO+i),2)
										#RPTries=App.CounterPID(RPTries,i,False)
									else:
										#pass
										#break
										if( Result[0] and (Result[1].retcode==10018 or Result[1].retcode==10019)): POO+=int((PT+RP)/RPO)
										POO+=i;i+=POO
										if(RPTries>1.5): RPTries=App.CounterPID(RPTries,POO*i,False) 
										#RP/=RPO
								if(POO>RPO+i):                                                  
									POO=RPO+i+1
									#break
					except Exception as exMessage:
						App.Logger(exMessage,40,'CPO')
					finally:
						pass
				App.ExecFunctions(CPO,FL=True)
			MTAccount()
			App.MTB(int(PB+(App.CPercentage(oPE,PE)*PE)+100),35)
			if(AI.balance>ai[ail].balance):
				App.SPV(f"*Good. {AI.balance}>{ai[ail].balance}; growth rate: {PB}%  in: {App.Timer(TW={'O':MTA , 'T': 1})} Seconds.")
				if(AI.balance/2.1>ai[ail].balance):
					App.MTB(2150+PB,185+PE)
					App.SPV("** Very good. You maid profit and growth {PB} percent on {AI.login} Account. via {App.AppInfo['Script']} in: {App.Timer(TW={'O':MTA , 'T': 1})} Seconds.")
			elif(AI.balance<ai[ail].balance): App.SPV(f"!Oh. {AI.balance}<{ai[ail].balance} ")
			elif(AI.balance==AI.balance):
				App.SPV(f"*Profect. {AI.balance}={ai[ail].balance}")
				#App.SPV(MTTrender())
				#App.Delay(abs(round((TDT['U'])-(TDT['D']/Risk) if TDT['B']>TDT['S'] else (TDT['D'])-(TDT['U']/Risk),2)))
			#C['&&']=(PT-C['&']) # set Orders counter from Positions.
			App.SPV(f"&:{C['&']}/{C['&&']} +:{C['+']}/{C['=+']} -:{C['-']}/{C['=-']} ==:{C['==']}")
			if(Tries>PT-C['+'] or App.CPercentage(oPE,PE)>10):
				c=App.CounterPID(round(float(0.02+((E/abs(AI.profit))+C['-'])-(C['+']+len(random.choice(list(OT.values()))))),3),((App.CPercentage(oPE,PE)+Size*C['-'])*PLC[3]),False)
				if(c>0):
					App.SPV(f"waiting {c}Sec  until change Prices to Best")
					#App.Delay(c)
				Tries=0
		else:
			App.SPV("Not Positions")
			if(MP[1]):
				MTAccount()
				App.SPV("Adding One Position")
				Pair=random.choice(SymbolsBest)
				if(MTOrder(op='Add',pair=Pair, Price=0,order_type=OT[MTRecommendationer(Pair,30,20,rates_way='Range')[1]], size=0, TPDistance=None, SLDistance=None,position=0,Comment="QRobotY")[0]): App.MTB(1000+len(Pair),100)
				else: symbols_info['Disabled'].append(Pair)
				return MTPositions(MP)
	except Exception as exMessage:
		App.Logger(exMessage,40,"MTPositionsLogs")
		if(Retries<App.Timer(TW={'O':App.AppInfo['PID'],'T':1})):
			App.SPV(f"retrying: {Retries}/{App.Timer(TW={'O':App.AppInfo['PID'],'T':1})} to get A Positions")
			App.Delay(0.75)
			Retries+=1
			if(MTOPC(CT=0)[0]!=None):
				return MTPositions(MP)
			else:
				App.SPV("Reloading MT5")
				if(MTConnect(account=Account)!=False):
					return MTPositions(MP)
		else:
			App.Delay(2.5)
			App.SE(SW='R')
	except KeyboardInterrupt:
		if(App.EF.get(MP[0])): App.EF.get(MP[0]).stop()
	finally:
		pass


def OLD():
	App.Logger("opening Logs Directory for Day.",10,OL=[True,App.SPV(m=0,tts=f"choice By typing Caps Letter from optionName. \n LogDir, YearLogDir, MonthLogDir, LogFiles")])
	return main(W='')


WF={0:sys.exit,9:OLD,1:MTTrying,2:MTAccount,3:MTOrder,4:MTPositions,5:MTZones}
def main(W='',R=False,la=0):
	try:
		App.AppInfo.update({'Script':"MTFullScript",'PID':App.os.getpid()})
		if(not App.AppInfo['PID'] in App.Timers): App.Timer(TW={'O':App.AppInfo['PID'], 'T': 0}) # Starting App.
		if(I==False):
			if(LD==0): la=int(App.SPV(m=0,tts="Choice Account: "))-1
			else:
				if(LD>len(LA or la>len(LA))): la=len(LA)-1
				else: la=(LD-1 if la ==0 else la-1)
			MTConnect(LA[la])
		if(len(W)!=0 and WF.get(int(W))!=None):
			R=True
			RF=App.ExecFunctions(FN=WF.get(int(W)),FP=[len(App.EF),True],FL=True) #WF.get(int(W))()
		else: R=False
	except Exception as exMessage:
		App.Logger(exMessage,40,f"{__name__}Logs")
	finally:
		if(R==False):
			if(App.NoOption==True):
				return main(W='4',R=R)
			elif(App.NoOption==False):
				return main(W=App.SPV(m=0,tts="Option"),R=R)
		"""else:
			if(RF):
				return App.inspect.stack()
			else:
				return False"""



if(__name__=='__main__'):
	try:
		Main=False
		if(App.IL): Main=main()
		LL=10;LT=f"Running {App.inspect.stack()[0].function if not Main else Main[len(Main)-1] }";SD=False
	except (Exception,KeyError) as exMessage:
		LT=exMessage;LL=40;SD=False
	except KeyboardInterrupt:
		LL=50;SD=True
	else: LL=20;SD=False
	finally:
		if(LL==50): LT=f"stopped:{App.AppInfo['Script']}{App.AppInfo['Version']} after {App.Timer(TW={'O':App.AppInfo['PID'],'T':1})} seconds. very Thanks to: {App.AppInfo['DevBy'][1]}";
		App.Logger(LT,LL,__name__)
		if(I and SD==True):
			App.SPV("Shuting down")
			App.ExitFunctions()
			App.MTB(500,150)
			mt5.shutdown()
			App.SE(DT=False,TO=False)
