"""def add(a, b):
    a = input("enter a number\n")
    b = input("enter another number\n")
    c = int(a)+ int(b)
    print("the answer is", str(c) + ".")
a = 0
b = 0
add(a, b"""
import random
def mult13(a):
    return a%13 == 0
w = random.randint(0, 13)
for x in range(0, 20):
    print(mult13(w))

