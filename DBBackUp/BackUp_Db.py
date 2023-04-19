import colorama
import datetime
import difflib

BACKUP_TYPE = {
        1: 'Full',
        2: 'Incremental',
        3: 'Partial'
    }

class DatabaseBackUP:
    DB_HOST = "localhost"
    DB_USER = "root"
    DB_USER_PASSWORD = "testing"
    DB_NAME = "TEST"
    BACKUP_PATH = "/backup/dbbackup"
    
    def Run_Backup(self):
        pass

    def Return_Parameter(self):
        print(colorama.Fore.BLUE + self.DB_HOST)
        print(colorama.Fore.BLUE + self.DB_USER)
        print(colorama.Fore.RED + self.DB_USER_PASSWORD)
        print(colorama.Fore.BLUE + self.DB_NAME)
        print(colorama.Fore.BLUE + self.BACKUP_PATH)
        
    def __init__(self,frameworkparameter,host,user,user_pass,databasename,backuppath,start_point):
        self.FRMSTART=frameworkparameter
        self.DB_HOST = host
        self.DB_USER = user
        self.DB_USER_PASSWORD = user_pass
        self.DB_NAME = databasename
        self.BACKUP_PATH = backuppath
        self.Script_Start_DATETIME=start_point