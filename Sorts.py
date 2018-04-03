# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 11:12:08 2018

@author: Administrator
@各种排序算法python实现
"""


def selectSort(array):
    for i in range(len(array)-1):
        minindex = i
        for j in range(i+1,len(array)):
            if array[j] < array[minindex]:
                minindex = j
        array[i],array[minindex] = array[minindex],array[i]
    return array

def bubbleSort(array):
    for index in range(len(array)):
        tag = False
        for j in range(len(array)-1-index):
            if array[j+1] < array[j]:
                tag = True
                array[j+1],array[j] = array[j],array[j+1]
        if tag == False:
            return array
    return array
def insertSort(array):
    for i in range(1,len(array)):
        while(array[i]<array[i-1] and i>=1):
            array[i],array[i-1] = array[i-1],array[i]
            i -= 1
    return array

def shellSort(array):
    gap = int(len(array)/2)
    while(gap>0):
        for i in range(gap,len(array)):
            temp = array[i]
            j = i-gap
            while(j>=0 and array[j]>temp):
                array[j+gap] = array[j]
                j -= gap
            array[j+gap] = temp
        gap = int(gap/2)
    return array

def mergeSort(array):
    def merge(left,right):  #用来将两个有序序列合并成一个有序序列
        array = []
        length = len(left) + len(right)
        left_index = 0;right_index = 0
        for i in range(length):
            if left_index >= len(left):
                array.append(right[right_index])
                right_index += 1
            elif right_index >= len(right):
                array.append(left[left_index])
                left_index += 1
            elif left[left_index] <= right[right_index]:
                array.append(left[left_index])
                left_index += 1
            else:
                array.append(right[right_index])
                right_index += 1
        return array
    if len(array)<2:     #分到只有一个元素，即是有序的
        return array
    mid = int(len(array)/2) 
    left = array[:mid]
    right = array[mid:]
    return merge(mergeSort(left),mergeSort(right))#将两个有序序列(故需要递归调用排序)合并  
def quickSort(array):
    def partition(array,left,right):#分区操作
        if(left>right):
            return None
        base = array[left]
        i = left;j=right
        while(i != j):
            while(array[j]>=base and i<j):
                j -= 1
            while(array[i]<=base and i<j):
                i += 1
            if(i<j):
                array[i],array[j] = array[j],array[i]
        array[left],array[i] = array[i],array[left]
        partition(array,left,i-1)#继续对左边进行分区
        partition(array,i+1,right)#继续对右边进行分区
    left = 0;right = len(array)-1
    partition(array,left,right)
    return array

def heapSort(array):
    heapSize = len(array)
    if(heapSize<2):
        return array
    def sink(array,heapSize,index):#将index位置元素下沉
       leftChild = 2*(index+1)-1
       if(leftChild>=heapSize):#若为叶子节点直接返回
           return 
       maxIndex = index #存最大元素下标
       if(array[leftChild]>array[index]):
           maxIndex = leftChild
       rightChild = leftChild+1
       if(rightChild<heapSize and array[rightChild]>array[maxIndex]):
           maxIndex = rightChild
       if(maxIndex != index):#若当前节点不是最大元素，则进行交换，并继续下沉
           array[index],array[maxIndex] = array[maxIndex],array[index]
           sink(array,heapSize,maxIndex)
    def buildHeap(array):
        current = len(array)//2-1 #第一个非叶子节点
        while(current>=0):
            sink(array,len(array),current)
            current -= 1
    buildHeap(array)
    for i in range(len(array)-1,-1,-1):
        array[0],array[i] = array[i],array[0]#将堆顶最大元素与最后一个元素交换，即将最大元素放置最后
        sink(array,i,0)#维护堆
    return array

def countSort(array):
    max_value = max(array)
    min_value = min(array)
    temp = [0 for i in range(min_value,max_value+1)]
    for item in array:
        temp[item-min_value] += 1
    i = 0
    for index,item in enumerate(temp):
        while(item != 0):
            array[i] = min_value + index
            i += 1
            item -= 1
    return array

def bucketSort(array,bucketsize):
    max_value = max(array)
    min_value = min(array)
    bucketcount = (max_value - min_value)//bucketsize + 1#桶的个数
    bucketList = [[] for i in range(bucketcount)]#桶的初始化
    for item in array:
        bucketList[(item-min_value)//bucketsize].append(item)
    for buncket in bucketList:#每个桶采用快速排序来排
        buncket = quickSort(buncket)
    i = 0
    for buncket in bucketList:
        for item in buncket:
            array[i] = item
            i += 1
    return array
        
    
                     
        
        
        
        
if __name__ == '__main__':
    a = [0, 1, 3, 4, 1, 8, 2, 6, 9, 5, 2, 7, 10]
    b = [1,2,3,4,5,6,7]
    a = bucketSort(a,3)
    print(a)
