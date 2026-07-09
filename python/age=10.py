# age=10
# if age>18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")

# if age==10:
#     print("You are 10 years old.")
# elif age==12:
#     print("You are 12 years old.")

# name="Alice"
# if age>10:
#     if name!="":
#         print(f"Your name is {name}.")
#     elif name=="":
#         print("You have no name.")
# else:
#     print("You are not old enough to have a name.")



#and , or , not
age=15
print(age>10 and age<20)
print(age<10 or age>20)
if age>10 and age<20:
    print("You are a teenager.")
if age<10 or age>20:
    print("You are not a teenager.")

if not age>18:
    print("You are not an adult.")