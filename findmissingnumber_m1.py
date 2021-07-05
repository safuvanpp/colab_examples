# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 10:52:13 2021

@author: safuv
"""

"""
You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in the list. 
One of the integers is missing in the list. Write an efficient code to find the missing integer.
"""

#method 1

"""
missing number =  n*(n+1)/2 - (sum of the list)
"""

def findmissingnumber(arr,n):
    total_sum = int((n+1)*(n+2)/2)
    print(total_sum)
    for i in array:
        total_sum -= i
    return total_sum

array = [1,2,5,6,3,8,7]
print(type(array))

print("The missing number is ", findmissingnumber(array,len(array)))