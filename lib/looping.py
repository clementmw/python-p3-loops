#!/usr/bin/env python3


def happy_new_year ():
    for i in range(10, 0, -1  ):
        print(i)
    print("Happy New Year!")

happy_new_year()


def fizzbuzz_printer():
    for num in range(1, 101):
       print(fizzbuzz(num))

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return num
    
fizzbuzz_printer()



def reverse_string(str):
    reversed_str = ""
    for char in str:
        reversed_str = char + reversed_str
    return reversed_str

print(reverse_string("hello"))



def square_integers(int_list):
    squared_list = []
    for int in int_list:
        squared_list.append(int**2)
    return squared_list

print(square_integers([1, 2, 3, 4, 5]))


    
 
    



