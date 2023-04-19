import difflib

class FileBackUp:

    BACKUP_TYPE=""

    def Compare_Files(self,Old_File,New_File):

        nResult=""

        with open(Old_File) as file_1:
            file_1_text = file_1.readlines()

        with open(New_File) as file_2:
            file_2_text = file_2.readlines()

        for line in difflib.unified_diff(
            file_1_text, file_2_text, fromfile='file1.txt',
            tofile='file2.txt', lineterm=''):
            nResult+=(line)

    def Incrimental_Backup(self):
        pass

    def Partial_Backup(self):
        pass

    def Full_Backup(self):
        pass

    def __init__(self,backup_type) -> None:
        BACKUP_TYPE=backup_type