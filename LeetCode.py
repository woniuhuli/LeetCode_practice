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

def  solve(S, T):
    def compair(s1,s2):
        dict1 = {}
        dict2 = {}
        for i in range(len(s1)):
            if s1[i] in dict1:
                if dict1[s1[i]] != s2[i]:
                    return False
            else:
                dict1[s1[i]] = s2[i]
            if s2[i] in dict2:
                if dict2[s2[i]] != s1[i]:
                    return False
            else:
                dict2[s2[i]] = s1[i]
        return True
    ans = 0
    l1 = len(T)
    for i in range(len(S)-l1+1):
        if compair(S[i:i+l1],T):
            ans += 1
    return ans

def  topk(nums):
    numDict = {}
    for i in nums:
        if i not in numDict:
            numDict[i] = 1
        else:
            numDict[i] += 1
    dictList = [[key,numDict[key]] for key in numDict]

    maxNums = dictList[0:2]
    if dictList[0][1] > dictList[1][1]:
        minindex = 1
        minvalue = dictList[1][1]
        maxindex = 0
        maxvalue = dictList[0][1]
    else:
        minindex = 0
        maxindex = 1
        minvalue = dictList[0][1]
        maxvalue = dictList[1][1]
    for i in range(2,len(dictList)):
        if dictList[i][1] > minvalue:
            maxNums[minindex] = dictList[i]
            if dictList[i][1] > maxvalue:
                minvalue = maxvalue
                maxvalue = dictList[i][1]
                maxindex,minindex = minindex,maxindex
            else:
                minvalue = dictList[i][1]
    return maxNums[0][0] + maxNums[1][0]

def LCS3():
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    length1 = len(s1)
    length2 = len(s2)
    Maxlen = [[0 for _ in range(length2 + 1)] for __ in range(length1 + 1)]
    for i in range(1, length1 + 1):
        for j in range(1, length2 + 1):
            if (s1[i - 1] == s2[j - 1]):
                Maxlen[i][j] = Maxlen[i - 1][j - 1] + 1
            else:
                Maxlen[i][j] = max(Maxlen[i][j - 1], Maxlen[i - 1][j])
    print(Maxlen[length1][length2])

def  miHomeGiftBag(p, M):
    res = []
    def helper(res,array,target,a,index):
        if target == 0:
            res.append(a)
        for i in range(index,len(array)):
            if array[i] <= target:
                a.append(array[i])
                helper(array,target-array[i],a,i+1)
                a.pop(len(a)-1)
    def find(res,array,target):
        array.sort()
        a = []
        helper(res,array,target,a,0)
        return res
    res = find(res,p,M)
    if len(res) >= 1:
        return True
    else:
        return False

def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    ans = []
    N = len(nums)
    if (N<4):
        return ans
    nums.sort()
    for i in range(N-3):
        if(i > 0 and nums[i] == nums[i-1]):
            continue
        if(nums[i]*4 > target):
            break
        for j in range(i+1,N-2):
            if(j > i+1 and nums[j] == nums[j-1]):
                continue
            if(nums[j]*3 + nums[i] > target):
                break
            k,h = j+1,N-1
            while(k<h):
                temp = nums[i] + nums[j] + nums[k] + nums[h]
                if temp < target:
                    k += 1
                elif temp > target:
                    h -= 1
                else:
                    ans.append([nums[i],nums[j],nums[k],nums[h]])
                    k,h = k+1,h-1
    return ans

def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    def partion(A):
        q = -1
        for i in range(len(A)):
            if (A[i] > 0):
                q += 1
                A[i], A[q] = A[q], A[i]
        return q

    k = partion(nums) + 1
    ans = k
    for i in range(k):
        temp = abs(nums[i])
        if (temp <= k):
            if (nums[temp - 1] > 0):
                nums[temp - 1] = -nums[temp - 1]

    for i in range(k):
        if (nums[i] > 0):
            ans = i
            break
    return ans + 1

def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # N = len(nums)
    # def canJumpFromPosition(position,nums):
    #     # N = len(nums)
    #     if(position == N-1):
    #         return True
    #     maxIndex = min(N-1, position + nums[position])
    #     for i in range(maxIndex,position,-1):
    #         if(canJumpFromPosition(i,nums)):
    #             return True
    #     return False
    # return canJumpFromPosition(0,nums)

    # N = len(nums)
    # memo = [2 for i in range(N)]  # 0 不可达，1 可达，2 未知
    # def canJumpFromPosition(position, nums):
    #     if (memo[position] != 2):
    #         if (memo[position] == 0):
    #             return False
    #         else:
    #             return True
    #     maxIndex = min(N - 1, position + nums[position])
    #     for i in range(maxIndex, position, -1):
    #         if (canJumpFromPosition(i, nums)):
    #             memo[position] = 1
    #             return True
    #     memo[position] = 0
    #     return False
    #
    # memo[N - 1] = 1
    # return canJumpFromPosition(0, nums)

    # N = len(nums)
    # memo = [2 for i in range(N)]
    # memo[N - 1] = 1
    # for i in range(N - 2, -1, -1):
    #     maxIndex = min(N - 1, i + nums[i])
    #     for j in range(maxIndex, i, -1):
    #         if (memo[j] == 1):
    #             memo[i] = 1
    #             break
    #         memo[i] = 0
    # return memo[0] == 1

    # N = len(nums)
    # lastPos = N - 1
    # for i in range(N - 1, -1, -1):
    #     if (nums[i] + i >= lastPos):
    #         lastPos = i
    # return lastPos == 0

    maxIndex = 0
    for i in range(len(nums)):
        if (i <= maxIndex):
            maxIndex = max(maxIndex, i + nums[i])
    return maxIndex >= len(nums) - 1

def jump(nums):
    N = len(nums)
    minIndex = [float('inf') for _ in range(N)]
    minIndex[0] = 0
    for i in range(N):
        maxIndex = min(N - 1, i + nums[i])
        for j in range(i + 1, maxIndex+1):
            minIndex[j] = min(minIndex[j], 1 + minIndex[i])
    return minIndex[N - 1]

def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    direction = 0  # 0：→ ；1：↓ ；2：← ； 3：↑
    rowMin, rowMax, colMin, colMax = 0, n - 1, 0, n - 1  # 判断是否越界
    row, col = 0, 0  # 当前位置
    A = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1,n ** 2 + 1):
        A[row][col] = i
        if (direction == 0):
            if (col < colMax):
                col += 1
            else:
                direction = 1
                rowMin += 1
                row += 1
                continue
        if (direction == 1):
            if (row < rowMax):
                row += 1
            else:
                direction = 2
                col -= 1
                colMax -= 1
                continue
        if (direction == 2):
            if (col > colMin):
                col -= 1
            else:
                direction = 3
                row -= 1
                rowMax -= 1
                continue
        if (direction == 3):
            if (row > rowMin):
                row -= 1
            else:
                direction = 0
                col += 1
                colMin += 1
                continue
    return A


if __name__ == "__main__":
    import sys
    import math
    def test():
        case = 5
        ans = generateMatrix(case)
        return ans
    print(test())