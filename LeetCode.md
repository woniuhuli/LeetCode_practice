#### 1.  Two Sum 
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
```
Given nums = [2, 7, 11, 15], target = 9  
Because nums[0] + nums[1] = 2 + 7 = 9
return [0, 1]
```
```python
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        算法一：暴力搜索
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        '''
        '''
        算法二：遍历列表两次,用空间换时间
        nums_dict = dict()
        for i in range(len(nums)):
            nums_dict[nums[i]] = i
        for i in range(len(nums)):
            t = target - nums[i]
            if (t in nums_dict) and (nums_dict[t] != i):
                return [i,nums_dict[target-nums[i]]]
        '''
        '''
        算法三：遍历一次,边建立字典边检查，找到答案即输出
        '''
        nums_dict = dict()
        for i in range(len(nums)):
            t = target - nums[i]
            if (t in nums_dict) and (nums_dict[t] != i):
                return [i,nums_dict[target-nums[i]]]
            nums_dict[nums[i]] = i       
```

#### 2. Add Two Numbers  
You are given two non-empty linked lists representing two non-negative integers.
 The digits are stored in reverse order and each of their nodes contain a 
 single digit. Add the two numbers and return it as a linked list.
```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```
```python
#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        '''
        直线思维
        a = [];b=[];c=[]
        while(l1.next!=None):
            a.append(l1.val)
            l1 = l1.next
        a.append(l1.val)
        while(l2.next!=None):
            b.append(l2.val)
            l2 = l2.next
        b.append(l2.val)
        x1 = 0;x2=0
        for i in range(len(a)):
            x1 += pow(10,i)*a[i]
        for i in range(len(b)):
            x2 += pow(10,i)*b[i]
        ans = x1 + x2
        if ans == 0:
            c = [0]
        else:
            while(ans!=0):
                c.append(ans%10)
                ans = ans//10
        result = ListNode(c[0])
        current = result
        for i in range(1,len(c)):
            current.next = ListNode(c[i])
            current = current.next
        return result
        '''
        #仿照手算加法过程
        p = l1;q = l2;
        carry = 0           #进位标志
        x = p.val;y = q.val
        temp = x+y
        ans = ListNode(temp%10)
        carry = temp//10
        current = ans
        while(p.next != None or q.next != None):
            if(p.next != None):
                p = p.next
                x = p.val
            else:
                x = 0
            if(q.next != None):
                q = q.next
                y = q.val
            else:
                y = 0
            temp = x+y+carry
            current.next = ListNode(temp%10)
            current = current.next
            carry = temp//10
        if carry == 1:
            current.next = ListNode(1)
        return ans
```

#### 3.  Longest Substring Without Repeating Characters  
Given a string, find the length of the longest substring without repeating characters.
```
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, 
"pwke" is a subsequence and not a substring.
```
```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 滑窗
        temp = []
        maxlen = 0
        for i in range(len(s)):
            if s[i] not in temp:
                temp.append(s[i])
                if maxlen < len(temp):
                    maxlen = len(temp)
            else:
                index = temp.index(s[i])
                if index == len(temp)-1:
                    temp = list(s[i])
                else:
                    temp = temp[index+1:]
                    temp.append(s[i])
        return maxlen       
```
#### 18. 4Sum  
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

```python
class Solution:
    def fourSum(self, nums, target):
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
                        while(k<h and nums[k+1] == nums[k]):
                            k+=1
                        while(k<h and nums[h-1] == nums[h]):
                            h -= 1
                        k,h = k+1,h-1
        return ans        
```
```cpp
#include <algorithm>    // std::sort
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        int N = nums.size();
        vector<vector<int>> result;
        if(N<4)
            return result;
        std::sort(nums.begin(),nums.end());
        for(int i = 0; i< N-3; i++){
            if( i>0 && nums[i] == nums[i-1]) 
                continue;
            if(nums[i]*4>target) 
                break;
            for(int j = i+1; j< N-2; j++){
                if(j > i+1 && nums[j] == nums[j-1]) 
                    continue;
                if(nums[j]*3+nums[i] > target) 
                    break;
                int k = j+1, h = N-1;
                while(k<h){
                    int temp = nums[i] + nums[j] + nums[k] + nums[h];
                    if (temp < target) k++;
                    else if (temp > target) h--;
                    else{
                        vector<int> ans = {nums[i],nums[j],nums[k],nums[h]};
                        result.push_back(ans);
                        while(k<h && nums[k] == nums[k+1]) k++;
                        while(k<h && nums[h] == nums[h-1]) h--;
                        k++;h--;
                    }
                }
            }
        }
        return result;
    }
};
```
```java
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        int N = nums.length;
        List<List<Integer>> result = new ArrayList<>();
        if(N<4) return result;
        Arrays.sort(nums);
        for(int i = 0; i < N-3; i++){
            if(i>0 && nums[i] == nums[i-1]) continue;
            if(nums[i]*4 > target) break;
            for(int j = i+1; j< N-2; j++){
                if(j>i+1 && nums[j] == nums[j-1]) continue;
                if(nums[j]*3 + nums[i] > target) break;
                int k = j+1, h = N-1;
                while(k<h){
                    int temp = nums[i]+nums[j]+nums[k]+nums[h];
                    if(temp<target) k++;
                    else if(temp>target) h--;
                    else{
                        List<Integer> ans = Arrays.asList(nums[i],nums[j],nums[k],nums[h]);
                        result.add(ans);
                        while(k<h && nums[k] == nums[k+1]) k++;
                        while(k<h && nums[h] == nums[h-1]) h--;
                        k++;h--;
                    }
                }
            }
        }
        return result;
    }
}
```

#### 35. Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, 
return the index where it would be if it were inserted in order.
```python
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums)-1
        while(low<=high):
            mid = (low + high)//2
            if(nums[mid] == target):
                return mid
            elif(nums[mid] < target):
                low = mid + 1
            else:
                high = mid -1
        if(nums[mid] > target):
            return mid
        else:
            return mid + 1
        
```

#### 41. First Missing Positive  
Given an unsorted integer array, find the smallest missing positive integer.  
```python
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def partion(A):
        # 将所有正数放在左边，返回值即为正数个数
            q = -1
            for i in range(len(A)):
                if(A[i] > 0):
                    q += 1
                    A[i],A[q] = A[q],A[i]
            return q + 1
        
        k = partion(nums)  
        firstMissIndex = k      
        for i in range(k):
            #若正数中有<=k的值则将第A[k-1]位置数置为负数
            #因此若有存在<=k的正数，则该位置值一定为负数
            temp = abs(nums[i])
            if(temp <=k):
                if(nums[temp-1] > 0):
                    nums[temp-1] = -nums[temp-1]
                    
        for i in range(k):
            if(nums[i] > 0):
                firstMissIndex = i
                break
        return firstMissIndex+1
```
```java
class Solution {
    static public void swap(int[] A, int i, int j){
        if(i!=j){
            A[i] ^= A[j];
            A[j] ^= A[i];
            A[i] ^= A[j];
        }
    }
    static public int partion(int[] A){
        int q = -1;
        for(int i = 0; i < A.length; i++){
            if(A[i] > 0){
                q++;
                swap(A,i,q);
            }
        }
        return q+1;
    }
    public int firstMissingPositive(int[] nums) {
        int N = nums.length;
        if(N==0) return 1;
        int k = partion(nums);
        int firstMissIndex = k;
        for(int i = 0; i<k; i++){
            int temp = Math.abs(nums[i]);
            if(temp <= k){
                if(nums[temp-1] > 0) nums[temp-1] = -nums[temp-1];
            }
        }
        for(int i = 0; i<k; i++){
            if(nums[i]>0){
                firstMissIndex = i;
                break;
            }
        }
        return firstMissIndex + 1;
    }
}
```

#### 55. Jump Game  
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.  

1. 如果index i 能够达到最后一个位置则记为好位置，否则为坏位置。那么题目就变成 0 是否是好位置。  
针对位置i，穷举其可能的步骤，如果能够达到某一个好位置则i为好位置，如果所有步骤都不能达到好位置则i为坏位置
```python
class Solution:
    def canJump(self, nums):
        def canJumpFromPosition(position,nums):
            N = len(nums)
            if(position == N-1):
                return True
            maxIndex = min(N-1,position + nums[position])
            for i in range(maxIndex,position,-1):
                if(canJumpFromPosition(i,nums)):
                    return True
            return False
        return canJumpFromPosition(0,nums)
```
2. 利用动态规划来解。利用一个N长的数组memo来存放各个位置的状态（也就是是否是好位置），每次需要时直接查询数组即可。  
初始状态是所有位置都是位置状态，N-1为好位置。思路与方法一一致。
```python
class Solution:
    def canJump(self,nums):
        N = len(nums)
        memo = [2 for i in range(N)]  #0 不可达，1 可达，2 未知
        memo[N-1] = 1
        def canJumpFromPosition(position,nums):
            if(memo[position] != 2):
                if(memo[position] == 1):
                    return True
                else:
                    return False
            maxIndex = min(N-1,position + nums[position])
            for i in range(maxIndex,position,-1):
                if(canJumpFromPosition(i,nums)):
                    memo[position] = 1
                    return True
            memo[position] = 0
            return False
        return canJumpFromPosition(0,nums)
```
3. 依然利用动态规划。还是利用N长的memo数组来存各位置状态信息，但是我们从右往左开始计算，这样我们总能在memo数组中
找到需要位置的状态信息，而不需要利用递归调用。
```python
class Solution:
    def canJump(self,nums):
        N = len(nums)
        memo = [2 for _ in range(N)]
        memo[N-1] = 1
        for i in range(N-2,-1,-1):
            maxIndex = min(N-1,i + nums[i])
            for j in range(maxIndex,i,-1):
                if(memo[j] == 1):
                    memo[i] = 1
                    break
            memo[i] = 0
        return memo[0] == 1
```
4. 贪心算法。我们从最后位置开始，每次都记录能够到达最后位置的最小下标，记为最小可行下标。而每次判定时只需要看
该位置是否能够到最小可行下标即可。
```python
class Solution:
    def canJunp(self,nums):
        minIndex = len(nums)
        for i in range(len(nums),-1,-1):
            if(i + nums[i] >= minIndex):
                minIndex = i
        return minIndex == 0
```
5. 仍然是贪心算法。我们从头开始遍历，记录所能到达的最大下标。遍历完成后，只要最大下标大于等于N-1即可。
```python
class Solution:
    def canJump(self,nums):
        maxIndex = 0
        for i in range(len(nums)):
            if(i <= maxIndex):
                maxIndex = max(maxIndex,i + nums[i])
        return maxIndex >= len(nums) - 1
```

#### 45. Jump Game II  
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.  

1. 根据问题从头到尾遍历一遍所有位置，维护一个N长数组用来存放到该位置的最少步数  
```python
class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        minStep = [float('inf') for _ in range(N)] #初始化为无穷大
        minStep[0] = 0
        for i in range(N):
            maxIndex = min(N-1, i + nums[i]) #该下标能够到达的最远位置
            for j in range(i + 1, maxIndex+1):
                minStep[j] = min(minStep[j], 1 + minStep[i]) #更新每个位置的最少步数
        return minStep[N-1]
```

2. BFS，广度优先算法。即层次遍历，每一步遍历一层，同步更新下一步能够到达的最远距离  
```python
class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if(N<2):
            return 0
        level, index, currentMax, nextMax = 0, 0, 0, 0
        while(nextMax < N-1):
            level += 1
            for i in range(index,currentMax + 1):
                nextMax = max(nextMax,i+nums[i])
                index += 1
            currentMax = nextMax
        return level
```