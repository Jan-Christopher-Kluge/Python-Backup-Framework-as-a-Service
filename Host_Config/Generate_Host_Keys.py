import os

Warnings_SSH_KEY = {
    1: 'Key_Expire',
    2: 'size to small',
    3: 'wrong type',
    4: 'deprecated warrning'
}

class SSH_Key:
    
    M_Framework=""
    M_Key_File_Name=""
    M_Key_Size=""

    def Web_Curl():
        pass

    def Post_Warning():
        pass

    def Warning_MSG():
        Stord_Warning=""

    def Generate_Key():
        pass

    def __init__(self,framework,filename,key_size):
        self.M_Framework=framework
        self.M_Key_File_Name=filename
        self.M_Key_Size=key_size
        