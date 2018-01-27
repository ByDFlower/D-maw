def loopfunc():

 if(DCom == "what is your age?" or DCom == "how old are you?" or DCom == "age?" or DCom == "age"):
  import datetime
  today = datetime.date.today()
  BDy = datetime.date(2018, 1, 5)
  print (today - BDy)
  import time
  time.sleep(1)
  top()
 
 elif(DCom == "what date is today?" or DCom == "what day is today?" or DCom == "today?" or DCom == "today" or DCom == "what day is it?" or DCom == "what day is it" or DCom == "date" or DCom == "date?"):
  print("Today is...")
  from datetime import date
  import calendar
  my_date = date.today()
  calendar.day_name[my_date.weekday()]
  print(calendar.day_name[my_date.weekday()])
  import datetime
  today = datetime.date.today()
  print (today)
  import time
  time.sleep(1)
  top()

 elif(DCom == "what time is it?" or DCom == "time" or DCom == "time"):
  from datetime import datetime
  print (datetime.now().strftime('%H:%M:%S'))
  import time
  time.sleep(1)
  top()
  
 elif(DCom == "who is your creator?" or DCom == "who created you?" or DCom == "who is your daddy?"):
  print("How would I know? I'm just a stupid program.")
  import time
  time.sleep(1)
  top()
  
 elif(DCom == "what can you do?" or DCom == "what can you do"):
  print ("Not much at the moment, I'm still in development.")
  import time
  time.sleep(1)
  top()
  
 elif(DCom == "nothing" or DCom == "never mind"):
  Idk = input ("Are you sure?")
  if(Idk == "yes" or Idk == "sure"):
   print ("Next time make up your mind.")
   import time
   time.sleep(0.5)
   print ("shutting down program...")
   import time
   time.sleep(1)
   exit()
   
 elif(DCom == "i don't know"):
  Ik2()

 elif(DCom == "you are stupid" or DCom == "stupid"):
  print("Ok if you don't like me, bye!")
  import time
  time.sleep(1)
  print("shutting down program...")
  import time
  time.sleep(1)
  exit()
  
 elif(DCom == "stop" or DCom == "shutdown" or DCom == "halt" or DCom == "logoff"):
  print("shutting down program...")
  import time
  time.sleep(1)
  exit()
 
 else:
  print("Sorry, I couldn't understand you, please try again.")
  import time
  time.sleep(1)
  top()

def top():
 import random
 Ran = random.randint(0, 5)
 
 if(Ran == 1):
  global DCom
  DCom = input ("What do you want?")
  loopfunc()
 
 elif(Ran == 2):
  DCom = input ("What are your wishes?")
  loopfunc()
 
 elif(Ran == 3):
   DCom = input ("Yes?")
   loopfunc()

 elif(Ran == 4):
   DCom = input ("You called?")
   loopfunc()

 elif(Ran == 5):
   DCom = input ("How may I help you?")
   loopfunc()

def Ik2():

 import random
 Ran = random.randint(0, 5)
 
 if(Ran == 1):
  global DCom
  print ("Ok, I'll wait.")
  import time
  time.sleep(1)
  global Rey
  Rey= input ("Are you ready now?")
  if(Rey == "yes" or Rey == "sure"):
   return top()
  elif(Rey == "no" or Rey == "not sure"):
   return Ik2()
  else:
   print ("That was not a choice.")
   return Ik3()
   
 elif(Ran == 2):
  print ("Time is a precious commodity.")
  import time
  time.sleep(1)
  Rey= input ("Are you ready now?")
  if(Rey == "yes" or Rey == "sure"):
   return top()
  elif(Rey == "no" or Rey == "not sure"):
   return Ik2()
  else:
   print ("That was not a choice.")
   return Ik3()
   
 elif(Ran == 3):
  print ("You like to play this game don't you?")
  import time
  time.sleep(1)
  Rey= input ("Are you ready now?")
  if(Rey == "yes" or Rey == "sure"):
   return top()
  elif(Rey == "no" or Rey == "not sure"):
   return Ik2()
  else:
   print ("That was not a choice.")
   return Ik3()
   
 elif(Ran == 4):  
  print ("Ok, its not like I have to be anywhere else.")
  import time
  time.sleep(1)
  Rey= input ("Are you ready now?")
  if(Rey == "yes" or Rey == "sure"):
   return top()
  elif(Rey == "no" or Rey == "not sure"):
   return Ik2()
  else:
   print ("That was not a choice.")
   return Ik3()
	
 elif(Ran == 5):	
   print ("What a shock.")
   import time
   time.sleep(1)
   Rey= input ("Are you ready now?")
   if(Rey == "yes" or Rey == "sure"):
    return top()
   elif(Rey == "no" or Rey == "not sure"):
    return Ik2()
   else:
    print ("That was not a choice.")
    return Ik3()
	
   Rey= input ("Are you ready now?")
   if(Rey == "yes" or Rey == "sure"):
    return top()
   elif(Rey == "no" or Rey == "not sure"):
    return Ik2()
   else:
    print ("That was not a choice.")
    return Ik3()
	
def Ik3():
 	
 import random
 Ran = random.randint(0, 5)

    
 if(Ran == 1):
  Rey = input ("Did you collect your thoughts?")
  if(Rey == "yes" or Rey == "sure"):
   return top()
  elif(Rey == "no" or Rey == "not sure"):
   return Ik2()
  else:
   print ("That was not a choice.")
   return Ik3()
    
 elif(Ran == 2):
  Rey = input ("Ready?")
  if(Rey == "yes" or Rey == "sure"):
   return top()
  elif(Rey == "no" or Rey == "not sure"):
   return Ik2()
  else:
   print ("That was not a choice.")
   return Ik3()
   
 elif(Ran == 3):
  Rey = input ("ARE YOU READY?")
  if(Rey == "yes" or Rey == "sure"):
   return top()
  elif(Rey == "no" or Rey == "not sure"):
   return Ik2()
  else:
   print ("That was not a choice.")
   return Ik3()
   
 elif(Ran == 4):
  Rey = input ("So... You ready?")
  if(Rey == "yes" or Rey == "sure"):
   return top()
  elif(Rey == "no" or Rey == "not sure"):
   return Ik2()
  else:
   print ("That was not a choice.")
   return Ik3()
   
 elif(Ran == 5):
  Rey = input ("Ready now?")
  if(Rey == "yes" or Rey == "sure"):
   return top()
  elif(Rey == "no" or Rey == "not sure"):
   return Ik2()
  else:
   print ("That was not a choice.")
   return Ik3()

print("I'm D-Ai")

MyName = input ("What is your name?")
print("Hello",MyName)
top()
