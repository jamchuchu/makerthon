import math

def calcLuckyNumber(month, day):
    num = (month + day) / 8
    return math.floor(num)

print("미션 1-1")
print(calcLuckyNumber(5,2))
print("\n")


def printGuGu(number):
    for i in range(1,10):
        print(f"{number}x{i}={number * i}")

print("미션 1-2")
printGuGu(2)
print("\n")


class Mod:
    def add(a, b):
        return a + b
    
    def sub(a, b):
        return a - b
    
    def mul(a, b):
        return a * b
    
    def div(a, b):
        return a / b
    

print("미션 1-3")
print(Mod.add(4, 2))
print(Mod.sub(4, 2))
print(Mod.mul(4, 2))
print(Mod.div(4, 2))
print("\n")
