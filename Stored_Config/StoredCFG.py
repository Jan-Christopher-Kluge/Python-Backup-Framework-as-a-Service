import os
import json
import datetime

class Store_Configure():
    BACKUP_PATH=""
    OS=""
    STORED_STARTPOINT = ""
    TODAYBACKUPPATH = ""
    DATETIME=""

    def Create_Config(self,hours,OS,host,ipaddress,ipv6address,services,path,status):
        nData= {
            "HOST":{
                "Name":host,
                "OS":OS,
                "AddressV4":ipaddress,
                "AddressV6":ipv6address,
                "Services":[
                    {
                    "ssh":str(services[0]),
                    "database":str(services[1]),
                    "DB_Type":
                        [
                            {
                                "mssql":str(services[2]),
                                "mariadb":str(services[3]),
                                "MySQL":str(services[4])
                            }
                        ]
                    }
                    ],
                    "Path":path,
                    "repeating_Backups":str(status),
                    "Interval":hours,
                    "First_backup":str(self.DATETIME),
                    "Last_backup":"%Y%m%d-%H%M%S"
                }
            }
        json_obj=json.dumps(nData,indent=17)
        file_path=os.getcwd()
        cname=file_path+host+".json"
        with open(cname, "w") as outfile:
            outfile.write(json_obj)
    
    def __init__(self,path,datetime) -> None:
        self.OS=os.getenv("")
        self.DATETIME=datetime
        self.BACKUP_PATH=path
        self.TODAYBACKUPPATH=path + str(datetime)

def testing():
    test = Store_Configure("/var/backup",datetime.datetime.now())
    test.Create_Config(0,"linux","test","192.168.0.1","fe:45:31:21:a3:21:11",[False,False,False,False,False],"/var/backup",False)
testing()