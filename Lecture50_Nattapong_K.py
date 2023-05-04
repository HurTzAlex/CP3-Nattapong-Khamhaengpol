# Create and Use Function + - * /
def plus(x, y):
    print(x, "+", y, "=", (x+y))

def minus(x, y):
    print(x, "-", y, "=", (x-y))

def multiply(x, y):
    print(x, "*", y, "=", (x*y))

def divine(x, y):
    print(x, "/", y, "=", (x/y))

Q1 = int(input("1 : "))
Q2 = int(input("2 : "))

print("Choose the operator")
print("1 is Plus,", "2 is Minus,", "3 is Multiply,", "4 is divined")

select = int(input("Select the option : "))
if select == 1:
    plus(Q1, Q2)
elif select == 2:
    minus(Q1, Q2)
elif select == 3:
    multiply(Q1, Q2)
elif select == 4:
    divine(Q1, Q2)
else:
    print("Error!!!")