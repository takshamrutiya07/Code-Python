# file1 = open("ict.txt")
# for each in file1:
#     print(each)

# file1 = open("ict.txt")
# print(file1.read())


# with open("ict.txt",'r') as f1:  
#     data = f1.read() 
# print(data)

# file1 = open("ict.txt")
# print(file1.read(5))


# with open("ict.txt",'r') as file:
#     data = file.readlines()
#     for line in data:
#         word = line.split()
#         print (word)

# file = open("ict.txt",'w')
# file.write("ICT ICT ICT \n")
# file.write("ICT ICT ICT ICT ICT")
# file.close()

# file = open("ict1.txt",'a')
# file.write("\n Department Department")
# file.close()

# with open('a.tif', 'rb') as file:
#     binary_data = file.read()

# import csv
# with open('data-1.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# import csv
# with open('output.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Name', 'Subject', 'Mark'])
#     writer.writerow(['Ram', 'PWP', 9])
#     writer.writerow(['Shyam', 'PWP', 10])
#     file.close()

# Program to count lines, words, and characters in a text file


# with open("ict.txt", "r") as file:
#     lines = file.readlines()
# line_count = len(lines)
# word_count = sum(len(line.split()) for line in lines)
# char_count = sum(len(line) for line in lines)
# print("Number of lines:", line_count)
# print("Number of words:", word_count)
# print("Number of characters:", char_count)

# lines = []
# with open("ict.txt", "r") as f:
#     for line in f:
#         lines.append(line.strip())
# print(lines)


# import csv

# with open("data-1.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


with open("ict1.txt", "r") as f1, open("ict.txt", "r") as f2:
    data1 = f1.read()
    data2 = f2.read()

with open("merged.txt", "w") as f:
    f.write(data1)
    f.write(data2)
