
import datetime
import subprocess
import sys

x = datetime.datetime.now()
year=x.year
month=x.month
day=x.day
hour=x.hour
minute=x.minute

from datetime import datetime, date
t4 = datetime(year=2021, month=5, day=22, hour=11, minute=10) #Hour in 24-hour format (00-23).
t5 = x
t6 = t4 - t5


if year==2021 and month==5 and day==22 and hour==11 and minute==10: #Hour in 24-hour format (00-23).
    
    print(" opening the notepad")
    subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
else:
           
    print(f" SORRY!! You have to wait {t6} to open the notepad by executing this python code ")
    print("\n")
    print(" If you want to open calculator instead of notepad then Enter C from keyboard")
    y=input()
    
    if y=="C" or y=="c":
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')
    else:
        sys.exit()
        
        

        
    



