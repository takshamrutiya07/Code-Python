#finding factorial using recursion
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter a number:"))
print(fact(n))

# How it's working
# 5*fact(4)
# 5*4*fact(3)
# 5*4*3*fact(2)
# 5*4*3*2*fact(1)
# 5*4*3*2*1

#fibonacci sequence using recursion
def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
# list of Fibonacci numbers
fib_sequence = [fibonacci(i) for i in range(5)]

print(*fib_sequence, sep=",")