import pandas as pd
df = pd.read_csv('D:/Semester-3/PythonClass/PACAssignment/students.csv')
percentages=[]
n = 3 
for index,row in df.iterrows():#iterrows return a series object at a time it will return index and object series
    marks = row[1:]
    total = sum(marks)
    percentage = total/3
    percentages.append(percentage)

df['Percentage'] = percentages
print(df)
