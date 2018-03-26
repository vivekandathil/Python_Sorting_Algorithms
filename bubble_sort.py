#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:57:09 2018

@author: vivekkandathil
"""

import time

test_List = [5, 4, 6, 7, 2, 3]

#Function that implements the bubble sort algorithm to sort a list in ascending order
def bubbleSort(data = []):
    
    """
    Iterate through each element in the list, if the value of the element is 
    greater than that of the next element, the two numbers swap indexes
    """
    start_time = time.time() #Variable to track execution time
    swaps = 0 #Variable to track number of swaps

    data_length = len(data)
    
    for x in range(data_length):
        switched = False
        for y in range(0, data_length - x - 1):
            if data[y] > data[y + 1]:
                data[y], data[y + 1] = data[y + 1], data[y]
                swaps += 1 
                switched = True
                
        #Causes program to only iterate if any initial values are swapped
        #Optimizes execution time
        if switched == False:
            break
    
    #Subtract start time from current time to get total execution time
    execution_time = time.time() - start_time
    
    print("Bubble Sorted:")
    print(data)
    print("%s seconds to execute " % format(execution_time, '.8f') + str(swaps) + " swaps")            
    
bubbleSort(test_List)
