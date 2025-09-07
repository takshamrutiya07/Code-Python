import sqlite3
# Connect to database (or create it)
conn = sqlite3.connect('student_record.db')
cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS student_record (
#                     Enrollment INTEGER PRIMARY KEY AUTOINCREMENT,
#                     name TEXT NOT NULL,
#                     Subject TEXT NOT NULL,
#                     Mark INTEGER NOT NULL
#                 )''')
student_record = [
    (92301733016,'ASHUTOSH KUMAR SINGH','PWP',95),
    (92301733017,'HARSH VISHALBHAI TRIVEDI','PWP',85),
    (92301733027,'VIRAJ PRAKASHBHAI VAGHASIYA','PWP',90),
    (92301733046,'SHIVAM ATULKUMAR BHATT', 'PWP',93),
    (92301733058,'DEVENDRASINH DOLATSINH JADEJA','PWP',75)
]
cursor.executemany('INSERT INTO student_record (name, Subject, Mark) VALUES (?, ?, ?)',
                   [(s[1], s[2], s[3]) for s in student_record])
conn.commit()
# cursor.execute('SELECT name, Subject, Mark FROM student_record WHERE Mark > 90')
# high_marks = cursor.fetchall()
# print("\nStudents with Marks greater than 90:")
# for student in high_marks:
#     print(student)
# conn.close()

# cursor.execute('SELECT * FROM student_record')
# rows = cursor.fetchall()
# # Display the results
# print("All Student Records:")
# for row in rows:
#     print(row)

# Update MArk for Ashutosh kumar (PWP)
# cursor.execute('''UPDATE student_record SET Mark = 98 
#                   WHERE name = 'ASHUTOSH KUMAR SINGH' AND subject = 'PWP' ''')

# # Commit the changes
# conn.commit()
# # Verify the update
# cursor.execute('SELECT name, MArk FROM student_record WHERE name = "ASHUTOSH KUMAR SINGH"')
# updated_mark = cursor.fetchone()
# print(f"\nUpdated Mark for {updated_mark[0]}: {updated_mark[1]}")


# Delete a student record (e.g.,DEVENDRASINH DOLATSINH JADEJA )
# cursor.execute('''DELETE FROM student_record WHERE name = 'DEVENDRASINH DOLATSINH JADEJA' ''')

# # Commit the changes
# conn.commit()

# # Verify the deletion
# cursor.execute('SELECT * FROM student_record WHERE name = "DEVENDRASINH DOLATSINH JADEJA"')
# deleted_name = cursor.fetchone()

# if deleted_name is None:
#     print("\nDEVENDRASINH DOLATSINH JADEJA has been successfully deleted.")

# # Calculate the average Mark
# cursor.execute('''SELECT AVG(Mark) FROM student_record''')
# avg_mark = cursor.fetchone()[0]

# print(f"\nThe average mark of students is: {avg_mark:.2f}")
# conn.close()
conn = sqlite3.connect('student_record.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    Enrollment INTEGER PRIMARY KEY,
                    Name TEXT NOT NULL
                )''')
cursor.execute('''CREATE TABLE IF NOT EXISTS enrollments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Enrollment INTEGER,
                    Subject TEXT NOT NULL,
                    Mark INTEGER NOT NULL,
                    FOREIGN KEY (Enrollment) REFERENCES students (Enrollment)
                )''')
students = [
    (92301733016, 'TAKSH '),
    (92301733017, 'PRINCE'),
    (92301733027, 'KRISH'),
    (92301733046, 'DARSHIT'),
    (92301733058, 'AKSHAT')
]
enrollments = [
    (92301733016, 'PWP', 95),
    (92301733016, 'DBMS', 90),
    (92301733017, 'PWP', 85),
    (92301733017, 'DSA', 80),
    (92301733027, 'PWP', 90),
    (92301733027, 'MATHS', 88),
    (92301733046, 'PWP', 93),
    (92301733058, 'PWP', 75),
    (92301733058, 'OS', 70)
]
cursor.executemany('INSERT OR IGNORE INTO students (Enrollment, Name) VALUES (?, ?)', students)
cursor.executemany('INSERT INTO enrollments (Enrollment, Subject, Mark) VALUES (?, ?, ?)', enrollments)
conn.commit()
cursor.execute('''SELECT s.Name, e.Subject, e.Mark 
                  FROM students s 
                  JOIN enrollments e ON s.Enrollment = e.Enrollment''')
rows = cursor.fetchall()
print("\nAll Student Enrollments:")
for row in rows:
    print(row)
cursor.execute('''SELECT AVG(Mark) FROM enrollments''')
avg_mark = cursor.fetchone()[0]
print(f"\nThe average mark of all subjects is: {avg_mark:.2f}")
conn.close()
