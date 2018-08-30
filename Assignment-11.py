#Q.1- Write a python code to find a valid email address from a text.
import re
string=input("Enter valid email id with a domain of gmail or yahoo")
m=re.search('[a-zA-Z][a-zA-Z0-9_.]*[@](gmail.com|yahoo.com)',string)
if(m==None):
    print("Invalid email id")
else:
    print("Valid email id")
    print("Starting from:",m.start(),"Ending at:",m.end(),"Email found is:",m.group())

#Q.2- Write a python program to find a valid Indian phone number from a text.
#(Valid Indian numbers will start with "+91-" and after that [6-9] followed by 9 digits.)
import re
string=input("Enter valid Phone Number")
m=re.search('\+91-[6-9][0-9]{9}',string)
if(m==None):
    print("Invalid Phone Number")
else:
    print("Valid Phone Number")
    print("Starting from:",m.start(),"Ending at:",m.end(),"Number found is:",m.group())

