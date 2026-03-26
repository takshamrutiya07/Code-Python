def average(a=1,b=1):#its called default argument
    print("The average is :",(a+b)/2)

#average(7,7) it will ignore the by default value 1 and 1 
average()

def average(a=1,b=1):#its called keyword argument
    print("The average is :",(a+b)/2)

average(b=9,a=21)

def average(a,b=1):#its called Required argument
    print("The average is :",(a+b)/2)

def average(a):#its called Required argument
    print("The average is :",a)
average(a=21)

def average(*numbers):#its called Variable length argument
    print(type(numbers))
    sum=0
    for i in numbers:
        sum = sum +i
    print("Average is:",sum/len(numbers))
average(5,5,5)