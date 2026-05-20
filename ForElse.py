#The else statement will not execute when we break the loop.
for i in range(6):
    print(i)
    if i==4:
        break
else:
    print("Hlw")