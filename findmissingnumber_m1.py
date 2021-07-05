# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 10:52:13 2021

@author: safuv
"""

#method 1

"""
missing number =  n*(n+1)/2 - (sum of the list)
"""

def findmissingnumber(arr,n):
    total_sum = (n+1)*(n+2)/2
    print(total_sum)
    for i in array:
        total_sum -= i
    return total_sum

array = [1,2,5,6,3,8,7]
print(type(array))

print("The missing number is ", findmissingnumber(array,len(array)))