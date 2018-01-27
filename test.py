print("I'm D-Ai")
import time

MyName = input ("What is your name?")
print("Hello",MyName)



DCom = input ("What do you want?")

if(DCom == "what is your age?" or DCom == "how old are you?" or DCom == "age?" or DCom == "age"):
 import datetime
 today = datetime.date.today()
 BDy = datetime.date(2018, 1, 5)
 print (today - BDy)
 input()
 
 
elif(DCom == "what date is today?" or DCom == "what day is today?" or DCom == "today?" or DCom == "today" or DCom == "what day is it?" or DCom == "what day is it"):
 from datetime import date
 import calendar
 my_date = date.today()
 calendar.day_name[my_date.weekday()]
 print(calendar.day_name[my_date.weekday()])
 input()

elif(DCom == "who is your creator?" or DCom == "who created you?" or DCom == "who is your daddy?"):
 print("How would I know? I'm just a stupid program.")
 input()
 
elif(DCom == "you are stupid" or DCom == "stupid"):
 print("Ok if you don't like me, bye!")
 import time
 time.sleep(1)
 print("shutting down program...")
 import time
 time.sleep(1)
 exit()
 
else():
 print("Sorry I couldnt understand you, please try again.")
 import time
 time.sleep(1)