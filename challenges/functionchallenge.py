#!/usr/bin/env python3

from time import sleep
import sys

print("Simple Calculator")
print()
def main():
   
    op = input("Enter operator \n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide: ")
    a = float(input("Enter first # "))
    b = float(input("Enter second # "))
    
    print("Calculating..."); sleep(0.4)
    work(a, b, op)
   

def work(a, b, op):
    if op == '1':
        print(a + b)
        print()
        again= input("would you like to do another calculation 1= yes, 2= no: ")
        redo(again)
    elif op == '2':
        print(a - b)
        print()
        again= input("would you like to do another calculation 1= yes, 2= no: ")
        redo(again)
    elif op == '3':
        print(a * b)
        print()
        again= input("would you like to do another calculation 1= yes, 2= no: ")
        redo(again)
    elif op == '4':
        print(a / b)
        print()
        again= input("would you like to do another calculation 1= yes, 2= no: ")
        redo(again)
    else:
        print("invalid entries, try again")
        main()


def redo(a):
    if a == '1':
        main()
    else:
        sys.exit()



main()  
        

