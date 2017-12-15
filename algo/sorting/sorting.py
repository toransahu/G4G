#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 09:03:20 2017

@author: toran
"""


def partition(arr, left, right):
    """
    Partition.
    
    Picks pivot is any preferable fashion:
        1. First element
        2. last element
        3. Mean
        4. randon
    Finds index of pivot and re-arranges elements smaller than pivot to left
    and greater to right.
    Returns: Partitioning Index (Re-calculated index of pivot)
    Time Complexity: O(n)
    Auxilary Space: O(1)
    """
    pivot_idx = right
    pivot_val = arr[pivot_idx]
    partition_idx = left
    
    # iterate from left to one step less of right
    # check number of elements lower than pivot_val, it will give partition_idx
    
    for i in range(left,right):
        if arr[i]<=pivot_val:
            arr[i], arr[partition_idx] = arr[partition_idx], arr[i]
            partition_idx+=1
    
    # put pivot in its partitioning index
    arr[right], arr[partition_idx] = arr[partition_idx], arr[right]
    return partition_idx

def quick_sort_iterative(arr,left,right):
    pass

def quick_sort_recursive(arr,left,right):
    """
    Quick Sort.
    
    
    Paradigm: Divide & Conquer
    Implementation: 
    In-place: 
    Time Complexity: 
        Best Case: O(nlogn)
        Avg Case: O(nlogn)
        Worst Case: O(n2)        
    Auxilary Space: 
    """
    if left<right:
        partition_idx = partition(arr,left,right)
        quick_sort_recursive(arr,left,partition_idx-1)
        quick_sort_recursive(arr,partition_idx+1,right)
    return arr


def merge(arr,left, pivot, right):
    """
    Merge.
    
    Desc:
        1. Merges two sorted sub-arrays by using an extra space of O(n).
        2. begin from 0th index of both sub-array, do comparision
        3. Make changes in original array
    Time Complexity: O(n)
    Auxilary Space: O(n)
    """
    import copy
    i = left
    j = pivot+1
    k = left
    temp_arr = copy.copy(arr)
    while(i<=pivot and j<=right):
        if temp_arr[i] <= temp_arr[j]:
            arr[k] = temp_arr[i]
            i+=1
        else:
            arr[k] = temp_arr[j]
            j+=1        
        k+=1
    while(i<=pivot):
        arr[k] = temp_arr[i]
        i+=1
        k+=1
    while(j<=right):
        arr[k] = temp_arr[j]
        j+=1
        k+=1
    return arr
        

def merge_sort(arr, left, right):
    """
    Merge Sort.
    
    Description: 
        1. Binary split of array till minimum/single entity
        2. Start merging single entity --> 2 sorted sub-array --> merge both
        3. Continue merging till end
    Paradigm: Divide  & Conquer
    Implementation: Recursive only
    In-place: Yes
    Time Complexity: 
        Best Case: O(nlogn)
        Avg Case: O(nlogn)
        Worst Case: O(nlogn)
    Auxilary Space: O(n)
    """
    if(left<right):
        pivot = (left+right)//2
        merge_sort(arr,0,pivot)
        merge_sort(arr,pivot+1,right)
        merge(arr,left,pivot,right)
    return arr
    
       
        
def insertion_sort(arr):
    """
    Select second & onwards elements one by one. ie. i
    Compare rest elements arr[j] i.e. 0...i-1 with above elements & if arr[j]
    is greater than arr[i] then shift jth elements right by one index.
    Repeat this for all j from i-1 to 0.
    
    Time Complexity: O(n2)
    Auxilary Space: 
    """
  
    n = len(arr)
    for i in range(1,n):
        k = i-1
        v = arr[i]
        for j in range(i-1,-1,-1):            
            if arr[j]>v:
                arr[j+1] = arr[j]
                k = j
        arr[k] = v        
    return arr
    

def selection_sort(arr):
    """
    Pulls a minimum element from sub-array and appends infront of that array.
    Time Complexity: 
        all case: O(n2)
    Auxilary Space: O(1)
    """
    n = len(arr)
    for i in range(0,n-1):
        min_idx = i
        for j in range(i,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort_optimized(arr):
    """
    Optimized to detect an already sorted array.
    Time Complexity:
        Worst/Avg Case: O(n2)
        Best Case: O(n)
    """
    n = len(arr)
    swapped = False
    # travers the array n-1 times
    for i in range(0,n-1):
        # Last i elements are already in place
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            return arr
    return arr


def bubble_sort(arr):
    """
    Time Complexity:
        Worst/Avg Case: O(n2)
        Best Case: O(n2)
    """
    n = len(arr)
    # travers the array n-1 times
    for i in range(0,n-1):
        # Last i elements are already in place
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [3,6,9,1,4,9,0,3,5,2]
arr = [9,8,7,6,5,4,3,2,1]
arr_s = [1,2,3,4,5,5,6,7]
# print(bubble_sort(arr))
# print(bubble_sort_optimized(arr_s))
# print(selection_sort(arr))
# print(insertion_sort(arr))
# print(insertionSort(arr))
# print(merge_sort(arr,0,8))
print(quick_sort_recursive([2,3,9,4,5,10],0,5))