def sum():
    a=10
    b=20
    print(a+b)

def sum2(a,b):
    print(a+b)

def sum3(a,b):
    return a+b
# a=sum3(10,20)
# print("sum:-",a)
# b=sum3(100,200)
# print("sum:-",b)

def citylist():
    cities=["pune","mumbai","nashik"]
    return cities
a=citylist()
print(a)
for city in citylist():
    print(city)
