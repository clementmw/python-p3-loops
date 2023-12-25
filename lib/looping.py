#!/usr/bin/env python3


def happy_new_year ():
    i = 10
    while i > 0:
       # print(i)
        i -= 1
    print("Happy New Year!")
     
happy_new_year()

#square integers

square = [1,2,3,4,5]
square_numbers = [i ** 2 for i in square]
print (square_numbers)

def fizzbuzz():
    for i in range (100):
        if i%3 == 0 and i%5 == 0 :
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print ("Buzz")
        else:
            print(i)  
    
fizzbuzz()