#!/usr/bin/env 

def binarySearch(searchArray, number):
    first = 0
    last = len(searchArray) - 1
    found = False
    while first <= last:
        mid = (first + last) // 2
        if searchArray[mid] == number:
            # print(searchArray[mid])
            # print(number)
            print("the number is " + str(searchArray[mid]))
            found = True
            break
        elif searchArray[mid] < number:
            first = mid + 1
        elif searchArray[mid] > number:
            last = mid - 1
    # return found

print(binarySearch([1,2,3,5,8], 5))
