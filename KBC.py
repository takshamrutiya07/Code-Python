list=["What is the answer of 2+2.",
      "What is the answer of 2*2.",
      "What is the answer of 2-2.",
      "What is the answer of 2/2."]
anslist=[4,4,0,1]
for i in range(0,4):
    print(list[i])
    ans=input("Enter the answer:")
    if(int(ans)==anslist[i]):
        print("Correct answer!")
    else:
        print("Incorrect answer!")
    