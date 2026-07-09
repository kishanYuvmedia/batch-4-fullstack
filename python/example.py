name=input("Enter your name: ")
age=int(input("Enter your age: "))
subject=input("Enter your favorite subject: ")
Total_marks=int(input("Enter your total marks: 500"))

def calculate_percentage(name,age,subject,Total_marks):
    percentage=(Total_marks/500)*100
    grade=""
    if percentage>=90:
        grade="A"
    elif percentage>=80:
        grade="B"
    elif percentage>=70:
        grade="C"
    elif percentage>=60:
        grade="D"
    else:
        grade="F"
    print(f"{name}, your age is {age}, your favorite subject is {subject}, and your grade is {grade}.")


calculate_percentage(name,age,subject,Total_marks)