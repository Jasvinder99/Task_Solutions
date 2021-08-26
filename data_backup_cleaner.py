import os
from datetime import date, datetime
from typing import Optional
from calendar import monthrange, day_name


class BackupCleaner():

    def __init__(self, current_date: Optional, file_date: Optional) :
        self.current_date: Optional[date] = current_date
        self.file_date: Optional[date] = file_date

#------------------------------------------------------------------------------------------------------------------
    def check_five_days(self, file_name: Optional) -> bool:
        day_diff  = self.current_date - self.file_date
        if day_diff.days >= 5:
            return True
        else:
            return False

#-------------------------------------------------------------------------------------------------------------------
    def check_last_day(self, file_name) -> bool:
        if self.file_date.day == monthrange(self.file_date.year, self.file_date.month)[1]:
            return True
        else:
            return False

#--------------------------------------------------------------------------------------------------------------------
    def check_sat(self, file_name) -> bool:
        if day_name[self.file_date.weekday()] == 'Saturday':
                return True
        else:
            return False
#-----------------------------------------------------------------------------------------------------------------
#Main Program
if __name__ == "__main__":
    #Taking current date as 2020 - 9 -18 as of now
    #current_date = datetime.now()

    path: [str] = input("Provide the path to folder")
    current_date: Optional[date] = datetime.strptime('2020-9-18', '%Y-%m-%d')
    #count of last 4 saturdays
    saturday_count: int = 0

#----------------------------------------------------------------------------------------------------------------------------------------------------------


    for folder_name in os.walk(path):

        if 'bucket' in folder_name[0]:
            path = folder_name[0]

            for file in os.listdir(path):
                starting: Optional = file.rfind('_') + 1
                ending: Optional = file.find('.')
                file_date: Optional = file[starting:ending]

                
                file_date: Optional = datetime.strptime(file_date, '%Y-%m-%d')
                clean = BackupCleaner(current_date, file_date)
                if clean.check_five_days(file):
                    if clean.check_sat(file) == False:
                        if clean.check_last_day(file) == False:
                            os.remove(path + '\\' + file)
                            print("Files are Removed")
                    else:
                        if saturday_count > 4:
                            if clean.check_last_day(file) == False:
                                os.remove(path + '\\' + file)
                                print("Files are removed")
                        else:
                            saturday_count += 1
