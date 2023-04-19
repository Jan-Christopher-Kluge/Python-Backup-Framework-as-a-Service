import os
import time
import colorama
import pathlib
import sys
import datetime
import pipes
import DBBackUp.BackUp_Db
import Host_Config.Stored_Host

M_DATETIME=time.strftime("%Y%m%d-%H%M%S")
M_STATUS = False
M_PARAMETER=sys.argv

class MyFramework:
    M_Start_Parameter=""
    M_Start_DATETIME=""
    M_SSH_KEY_LIST=pathlib.Path()

    

    def __init__(self):
        self.M_Start_Parameter=M_PARAMETER
        self.M_Start_DATETIME=M_DATETIME

menu_options = {
    1: 'start One Time',
    2: 'Configure',
    3: 'Database Backup',
    4: 'Show Config',
    5: 'Store Config',
    6: 'Frequnced start as service/daemon',
    7: 'Run Test or dry Run to check the permisions and create a log file',
    8: 'Show mail support',
    9: 'Quit!',
}

configure_options = {
    1:'Path and Files',
    2:'Include Database',
    3:'Set OS',
    4:'Set Time interval full backup',
    5:'Set Warrning',
    6:'Set Parcel',
    7:'Set Incremential',
    9:'Go to start!'
}

def Check_StorePoint(self):
        try:
            os.stat(self.TODAYBACKUPPATH)
        except:
            os.mkdir(self.TODAYBACKUPPATH)

def Quit_App():
    print(colorama.Fore.LIGHTRED_EX, "See you and bye.")
    print(colorama.Fore.WHITE,"Quit Application.")
    quit()

def Start():
    pass

def Database_Backup(framework):
    DBBACK=DBBackUp.BackUp_Db.DatabaseBackUP(framework)

def Configure():
    print("Configure the backups and pathes to the daemons and files.")
    option=0
    while(True):
        print_menu(configure_options)
        option = int(input('Option Wählen:' + colorama.Fore.BLUE))
        if(option == 9):
            print("Go to main menue")
            Main(1)
        elif(option==1):
            Start()
        elif(option == 2):
            Configure()
        elif(option==3):
            Database_Backup()
        elif(option==4):
            Show_Config()
        elif(option==5):
            Store_Config()
        elif(option==6):
            Set_Frequenced_Backup()
        elif(option==7):
            Run_Test()
        else:
            option=0

def Show_Config():
    nPath = ""
    nReturn = os.system("")    
    print(nReturn)

def Store_Config():
    pass
def Set_Frequenced_Backup():
    pass

def Run_Test():
    pass

def Show_Support():
    print("jck1979@outlook.com")

def print_menu(Menu:dict):
	for key in Menu.keys():
		print(colorama.Fore.GREEN + str(key), '--', end="")
		print(colorama.Fore.BLUE, Menu[key])

def Main(Runing):
    NewFrm=MyFramework()
    
    if Runing == 0:
        print(colorama.Fore.GREEN + "Start Backup")
        nLstPath=input("Path:")
        print(colorama.Fore.BLUE + "Deafault service to connect is ssh." + '/n' + "Make sure that the service is runing and the accounts are able to logging.")

    nTime=str(time.localtime)
    print("script start:"+ nTime)
    option=0
    while(True):
        print_menu(menu_options)
        option = int(input('Option Wählen:' + colorama.Fore.BLUE))
        if(option == 9):
            Quit_App()
        elif(option==1):
            Start()
        elif(option == 2):
            Configure()
        elif(option==3):
            Database_Backup(NewFrm)
        elif(option==4):
            Show_Config()
        elif(option==5):
            Store_Config()
        elif(option==6):
            Set_Frequenced_Backup()
        elif(option==7):
            Run_Test()
        elif(option==8):
            Show_Support()
        else:
            option=0
Main(0)