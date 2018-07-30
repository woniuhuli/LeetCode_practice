def LCS(s1, s2):
    '''
    动态规划求解最长公共子序列
    '''
    length1 = len(s1)
    length2 = len(s2)
    Maxlen = [[0 for _ in range(length2 + 1)] for __ in range(length1 + 1)]
    for i in range(1, length1 + 1):
        for j in range(1, length2 + 1):
            if (s1[i - 1] == s2[j - 1]):
                Maxlen[i][j] = Maxlen[i - 1][j - 1] + 1
            else:
                Maxlen[i][j] = max(Maxlen[i][j - 1], Maxlen[i - 1][j])
    return Maxlen[length1][length2]


def LCS2(s1, s2):
    #最长公共子串
    length1 = len(s1)
    length2 = len(s2)
    MaxLen = [[0 for _ in range(length2 + 1)] for __ in range(length1 + 1)]
    for i in range(1, length1 + 1):
        for j in range(1, length2 + 1):
            if s1[i - 1].lower() == s2[j - 1].lower():
                MaxLen[i][j] = MaxLen[i - 1][j - 1] + 1
            else:
                MaxLen[i][j] = 0
    return max([max(a) for a in MaxLen])
def MAL(a):
    #求最长上升子序列
    length = len(a)
    MaxLen = [1 for _ in range(length)]
    for i in range(1, length):
        for j in range(i):
            if a[j] < a[i]:
                MaxLen[i] = max(MaxLen[i], MaxLen[j] + 1)
    return max(MaxLen)


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

def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    ans = [1 for _ in range(rowIndex+1)]
    for row in range(2,rowIndex+1):
        t2 = 1
        for column in range(1,row):
            t1 = ans[column]
            ans[column] = ans[column] + t2
            t2 = t1
    return ans

def findMin(nums):
    if nums[-1] >=nums[0]:
        return nums[0]
    mid = len(nums)//2
    if nums[mid] > nums[0]:
        return findMin(nums[mid:])
    else:
        return findMin(nums[1:mid+1])
if __name__ == "__main__":
    # s1 = 'abcfbc'
    # s2 = 'abfcabC'
    # print(LCS2(s1,s2))
    a =[4, 7, 3, 5, 9, 4,5, 8,6]
    #print(MAL(a))
    #print(topK(a,4))
    nums = [3,4,5,1,2]
    print(findMin(nums))
