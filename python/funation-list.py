# 1. without prameter with out return value
def sum():
    print(10+20)


# sum()

# 2. with parameter with out return value
def sum(a,b,c):
    print(a+b+c)  

sum(10,20,30)
sum(50,20,30)
# 3. with parameter with return value

def sum(a,b,c):
    return a+b+c




result=sum(10,20,30)
print(result)
# 4. without parameter with return value 

def sum():
    return 10+20

result=sum()