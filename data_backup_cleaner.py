#Task : Backup Cleaner
#.................................................................................................................
import os, sys, time
from calendar import calendar, monthrange
from datetime import datetime, timedelta
#----------------------------------------------------------------------------

class Backup_Cleaner:

    def __init__(self, number_days, weeks_days, path):
        self.number_days = number_days
        self.weeks_days = weeks_days     #store monday,tueday ...
        self.path = path

    # ----------------------------------------------------------------------

    def cleaner(self):

        temp_data = []                                        # temporary list of weekdays

        for folder_name in os.walk(self.path):

            if 'bucket' in folder_name[0]:
                self.path = folder_name[0]
                # Consider todays date  as '2020-09-18'
                current_date = '2020-09-18'
                current_date = datetime.strptime(current_date, '%Y-%m-%d').date()   #set date as per format
                temp_date = current_date - timedelta(days = number_days)   #get date from last x days, where x value taken from user or set = 5


                for i in range(self.number_days):
                    single_day = current_date - timedelta(days = self.weeks_days + 1, weeks=i)  #get past saturday
                    temp_data.append(single_day)

                for backup_files in os.walk(self.path, topdown=False):

                    for file in (backup_files[2]):    #
                        only_date = (file[file.index('2020'): file.index('.txt')])
                        only_date = datetime.strptime(only_date, '%Y-%m-%d').date() #only store date ....stripinto format

                        if temp_date > only_date != only_date.replace(day = monthrange(only_date.year, only_date.month)[1]) and only_date not in temp_data:
                            clean_path = (self.path + '\\' + file)
                            self.clear_path(clean_path)


                print("Files are  removed from ", self.path)

    #-----------------------------------------------------------------------------------------

    def clear_path(self, path):
        if os.path.isdir(path):
            pass
        else:
            try:
                if os.path.exists(path):
                    os.remove(path)
            except OSError:
                print("Unable to delete the files : ", path)



# ----------------------------------------------------------------------
#main program
if __name__ == "__main__":
    print("*-"*30)
    number_days = int(input("\nEnter number of days : "))
    weeks_days = int(input("choose weekday:\n 0.Mon, 1.Tues, 2.Wed, 3.Thus, 4.Fri, 5.Sat, 6.Sun :"))

    path = input("Provide path for cleaning of data to folder  :")    # user input, for removing data from buckets
    print("*:"*10)

    files = Backup_Cleaner(number_days, weeks_days, path)
    files.cleaner()