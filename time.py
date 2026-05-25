# t=int(input("Enter the time in form of 1-24 hours:"))
# if(t>=18 and t<23):
#     print("Good Evening :")
# elif(t>=23 and t<=24 or t<6):
#     print("Good night:")
# elif(t>6 and t<12):
#     print("Good mornig ")
# else:
#     print("Good Afternoon ")
import time 
timestemp=(time.strftime('%H:%M:%S'))
print(timestemp)
times=int(time.strftime('%H'))
if(times>=6 and times<=12):
    print("Good Morning!")
elif(times>12 and times<=18):
    print("Good Afternoon!")    
elif(times>18 and times<=23):
    print("Good Evening!")
elif(times>23 and times<=24 or times>=0 and times<6):
    print("Good Night!")
import time

