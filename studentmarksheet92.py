name = input("Enter student's name: ")
roll_no = input("Enter roll number: ")

print("\nEnter marks for 5 subjects:")

subject1 = float(input("Subject 1: "))
subject2 = float(input("Subject 2: "))
subject3 = float(input("Subject 3: "))
subject4 = float(input("Subject 4: "))
subject5 = float(input("Subject 5: "))

total = subject1 + subject2 + subject3 + subject4 + subject5
percentage = (total / 500) * 100

# Grade
if percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

# Result
if (subject1 < 40 or subject2 < 40 or subject3 < 40 or
    subject4 < 40 or subject5 < 40):
    result = "Fail"
else:
    result = "Pass"

# Display marksheet
print("\n========== STUDENT MARKSHEET ==========")
print("Name:", name)
print("Roll No:", roll_no)
print("---------------------------------------")
print("Subject 1:", subject1)
print("Subject 2:", subject2)
print("Subject 3:", subject3)
print("Subject 4:", subject4)
print("Subject 5:", subject5)
print("---------------------------------------")
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Result:", result)
print("=======================================")