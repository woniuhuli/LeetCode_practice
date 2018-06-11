本文参考这个[链接](https://blog.csdn.net/zyq522376829/article/details/47686867)
### 引题  
1. 从n(非常大)个数中造出最大的K(较小)个数
- 思路：  
先拿出K个数建立一个小根推，那么堆顶元素就是K个数中最小的。然后每次从剩余数中选择一个数与堆顶元素进行比较，如果大于堆顶数就用该数
替换堆顶数，然后维护小根堆，直到处理完所有数据。那么这个小根堆中的K个数就是最大的K个数。建堆的复杂度为O(K)，维护堆的复杂度为O(logK)，
n-K个数替换并维护堆的复杂度为O(n-K)+(n-K)O(logK)，因此总的复杂度为O(nlogK)  
- 小小优化  
将n个数分组存放，比如切分层m个文件，利用上述方法找到每个文件的前K个，然后将每个文件的前K个合并找到最大的K个，类似MapReduce的思想。
- 关键代码  
由上述分析，这个问题关键在于建小根堆和维护堆.关于小根堆的概念及其建堆维护见排序算法中的堆排序。
```python
def swim(heap,index):
    if(index==0):
        return 
    parent = (index-1)//2
    if heap[parent]<=heap[index]:
        return 
    else:
        heap[parent],heap[index] = heap[index],heap[parent]
        swim(heap,parent)
def sink(heap,index):
    heapSize = len(heap)
    leftChild = 2*(index+1) - 1
    rightChild = leftChild + 1
    if leftChild >= heapSize:
        return 
    minIndex = index
    if heap[leftChild]<heap[minIndex]:
        minIndex = leftChild
    if (rightChild < heapSize and heap[rightChild] < heap[minIndex]):
        minIndex = rightChild
    if minIndex == index:
        return 
    else:
        heap[index],heap[minIndex] = heap[minIndex],heap[index]
        sink(heap,minIndex)
def buildHeap(array):
    heapSize = len(array)
    index = heapSize//2 - 1
    for i in range(index,-1,-1):
        sink(array,i)
def topK(array,k):
    heap = array[0:k]
    buildHeap(heap)
    for i in range(k,len(array)):
        if array[i] > heap[0]:
            heap[0] = array[i]
            sink(heap,0)
    return heap
```
### TopK问题  
- 描述  
在大规模数据处理中，经常会遇到的一类问题：在海量数据中找出出现频率最高的前k个数，或者从海量数据中找出最大的前k个数，这类问题通常被称为top K问题。
例如，在搜索引擎中，统计搜索最热门的10个查询词；在歌曲库中统计下载最高的前10首歌等。  
 针对top K类问题，通常比较好的方案是分治+Trie树/hash+小根堆，即先将数据集按照Hash方法分解成多个小数据集，
 然后使用Trie树或者Hash统计每个小数据集中的query词频，之后用小顶堆求出每个数据集中出现频率最高的前K个数，
 最后在所有top K中求出最终的top K。  
- 例题  
有1亿个浮点数，如果找出期中最大的10000个？
- 解法  
1. 最容易想到的方法是将数据全部排序。  
然后在排序后的集合中进行查找，最快的排序算法的时间复杂度一般为O（nlogn），如快速排序。但是在32位的机器上，
每个float类型占4个字节，1亿个浮点数就要占用400MB的存储空间，对于一些可用内存小于400M的计算机而言，
很显然是不能一次将全部数据读入内存进行排序的。其实即使内存能够满足要求，
该方法也并不高效，因为题目的目的是寻找出最大的10000个数即可，而排序却是将所有的元素都排序了，做了很多的无用功。  
2. 局部淘汰法  
该方法与排序方法类似，用一个容器保存前10000个数，然后将剩余的所有数字——与容器内的最小数字相比，
如果所有后续的元素都比容器内的10000个数还小，那么容器内这个10000个数就是最大10000个数。
如果某一后续元素比容器内最小数字大，则删掉容器内最小元素，并将该元素插入容器，最后遍历完这1亿个数，
得到的结果容器中保存的数即为最终结果了。此时的时间复杂度为O（n+m^2），其中m为容器的大小，即10000  
3. 分治法  
将1亿个数据分成100份，每份100万个数据，找到每份数据中最大的10000个，最后在剩下的100*10000个数据里面找出最大的10000个。
如果100万数据选择足够理想，那么可以过滤掉1亿数据里面99%的数据。100万个数据里面查找最大的10000个数据的方法如下：
用快速排序的方法，将数据分为2堆，如果大的那堆个数N大于10000个，继续对大堆快速排序一次分成2堆，
如果大堆个数N小于10000个，就在小的那堆里面快速排序一次，找第10000-n大的数字,就可以找到前10000个数。
此种方法需要每次的内存空间为10^6*4=4MB，一共需要101次这样的比较。  
4. Hash法  
如果这1亿个书里面有很多重复的数，先通过Hash法，把这1亿个数字去重复，
这样如果重复率很高的话，会减少很大的内存用量，从而缩小运算空间，然后通过分治法或最小堆法查找最大的10000个数  
5. 采用小根堆  
首先读入前10000个数来创建大小为10000的最小堆，建堆的时间复杂度为O（mlogm）（m为数组的大小即为10000），
然后遍历后续的数字，并于堆顶（最小）数字进行比较。如果比最小的数小，则继续读取后续数字；如果比堆顶数字大，
则替换堆顶元素并重新调整堆为最小堆。整个过程直至1亿个数全部遍历完为止。
然后按照中序遍历的方式输出当前堆中的所有10000个数字。该算法的时间复杂度为O（nlogm），空间复杂度是10000（常数）。  

