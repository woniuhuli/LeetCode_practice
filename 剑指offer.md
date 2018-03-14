 **有序二维数据中的查找**

 - 描述：  
 在一个有序的二维数据中，每一行都按照从左到右递增的顺序排序，
 每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
 判断数组中是否含有该整数。
 - 思路：  
 从左下角开始查找，大了就往上找，小了就往右找。避免从左上角查找时出现分叉
  
  
 - 答案：
 > python答案
 ```python
def Find(target,array):
    raws = len(array)
    columns = len(array)
    raw = raws - 1
    column = 0
    while(raw>=0 and column < columns):
        if(target == array[raw][column]):
            return True
        elif(target > array[raw][column]):
            raw -= 1
        else:
            column += 1
    return False
```
> java答案
```java
public class solution{
    public boolean Find(int target, int [][] array){
        int raws = array.length;
        int columns = array[0].length;
        int raw = raws -1;
        int column = 0;
        while(raw>=0 && column < columns){
            if(target == array[raw][column]){
                return true;
            }
            else if(target > array[raw][column]){
                raw --;
            }
            else
                column ++;
        }
        return false
    }
}
```  
**替换空格**
- 描述：  
请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.
则经过替换之后的字符串为We%20Are%20Happy。
  
- 思路：  
题目应该指的在原字符串的基础上修改。对于python直接替换；  
对于java，首先计算出修改后的字符串长度，然后从最后一个字符开始查找替换，这样字符移动次数最少
  
- 答案：
> python答案
```python
def ReplaceSpace(s):
    return s.replace(' ', '%20')
```
> java答案
```java
public class Solution {
    public String replaceSpace(StringBuffer str) {
        int spacenum = 0;
        for(int i=0;i<str.length();i++){
            if(str.charAt(i) == ' ')
                spacenum++;
        }
        int index_old = str.length()-1;
        int length_new = str.length() + spacenum*2;
        int index_new = length_new-1;
        str.setLength(length_new);
        for(;index_old>=0;index_old--){
            if(str.charAt(index_old) == ' '){
                str.setCharAt(index_new--,'0');
                str.setCharAt(index_new--,'2');
                str.setCharAt(index_new--,'%');
            }
            else{
                str.setCharAt(index_new--,str.charAt(index_old));
            }
        }
    	return str.toString();
    }
}
```

**从尾到头打印链表**
- 描述：  
输入一个链表，从尾到头打印链表每个节点的值。
  
- 思路：  
对于python将链表依次读入list，然后将list倒序返回即可；  
对于java借用栈来实现，链表元素依次入栈然后出栈进list即可
  
- 答案：
> python 答案
```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        items = []
        current_node = listNode
        while(current_node):
            items.append(current_node.val)
            current_node = current_node.next
        return items[::-1]
```
> java 答案
```java
/**
*    public class ListNode {
*        int val;
*        ListNode next = null;
*
*        ListNode(int val) {
*            this.val = val;
*        }
*    }
*
*/
import java.util.Stack;
import java.util.ArrayList;
public class Solution {
    public ArrayList<Integer> printListFromTailToHead(ListNode listNode) {
        Stack<Integer> stack = new Stack<>();
        while(listNode != null){
            stack.push(listNode.val);
            listNode = listNode.next;
        }
        ArrayList<Integer> list = new ArrayList<>();
        while(!stack.isEmpty()){
            list.add(stack.pop());
        }
        return list;
    }
}
```
**旋转数组查找最小值**
- 描述：  
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。  
 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。   
 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。  
  NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
  
- 思路：  
简单查找：找到后一个元素小于前面一个即找到了，如果一直没找到则是未旋转数组，直接输出第一个元素即可。  
二分法思路：令mid = low+(high-low)/2.将mid与high比较有三种情况。  
1) high < mid:则分界在后半段, 令low = mid+1；  
2) high=mid:则分界不确定，继续查找，令high=high-1  
3) high>mid: 则分界在前半段，令high = mid (不是mid-1，分析只有两个元素时情况即可)
  
- 答案：
> python 答案
```python
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray)== 0:
            return 0
        low = 0;high = len(rotateArray)-1;
        mid = low + (high-low)/2
        while high>low:
            if rotateArray[high] <rotateArray[mid]:#分界值在后半段
                low = mid +1
            elif rotateArray[high]== rotateArray[mid]:#分界值不确定，继续查找
                high -= 1
            else:#分界值在前半段
                high = mid
            mid = low + (high-low)/2
        return rotateArray[high]
```
> java 答案
```java
import java.util.ArrayList;
public class Solution {
    public int minNumberInRotateArray(int [] array) {
        if (array.length == 0){
            return 0;
        }
        int low = 0;int high = array.length-1;
        int mid = low + (high-low)/2;
        while(high>low){
            if(array[high]<array[mid]){
                low = mid+1;
            }
            else if(array[high]==array[mid]){
                high -= 1;}
            else{
                 high = mid;
                }
            mid = low + (high-low)/2;
            }
            
        return array[high];
    
    }
}
```
**斐波那契数列**
- 描述：  
斐波那契数列 0,1,1,2,3,5,8.现在要求输入一个整数n，请你输出斐波那契数列的第n项。
  
- 思路：  
利用递归很容易实现，但是由于重复计算太多次，很容易导致递归栈的溢出。  
于是我们可以考虑利用动态规划，将最后计算出来的两个数字存起来，避免进行重复计算  
关于动态规划可以参考[这个博客](http://blog.csdn.net/baidu_28312631/article/details/47418773)
  
- 答案：
> python 答案
```python
class Solution:
    def Fibonacci(self, n):
        if n==0:
            return 0
        if n==1:
            return 1
        fn_1 = 1;fn_2 = 0
        while n>1:
            fn_1 += fn_2
            fn_2 = fn_1 - fn_2
            n -= 1
        return fn_1
```
> java 答案
```java
public class Solution {
    public int Fibonacci(int n) {
        if(n==0){
            return 0;
        }
        else if(n==1){
            return 1;
        }
        else{
            int fn_1 = 1,fn_2 = 0;
            while(n-- >1){
                fn_1 = fn_1+fn_2;
                fn_2 = fn_1 - fn_2;
            }
            return fn_1;
        }

    }
}
```
**跳台阶问题**
- 描述：  
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
  
- 思路：  
假设第一步跳一阶，则有f(n-1)种跳法，若第一步跳两阶，则有f(n-2)种跳法。因此f(n) = f(n-1)+f(n-2)  
即转化成了斐波那契数列问题。具体分析见上一题。

**变态跳台阶问题**
- 描述：  
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
  
- 思路：  
假设第一步跳一阶，则有f(n-1)种跳法，若第一步跳两阶，则有f(n-2)种跳法...因此f(n) = f(n-1)+f(n-2)+..f(1) +1   
又有f(n-1) = f(n-2)+f(n-3)+...f(1)+1 所以有f(n) = 2*f(n-1)
f(1) = 1,故f(n) = 2^(n-1).  

**矩形覆盖问题**
- 描述：  
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。  
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
  
- 思路：  
如果最后一行单独放一个，则有f(n-1)种方法，如果最后两行错开放则有f(n-2)种方法，故f(n)=f(n-1)+f(n-2)

**二进制中1的个数**
- 描述：  
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示(32位).
  
- 思路：  
每次与1做与运算即可得到最低位是否是1，利用右移操作依次判断。  
注意在java中负数右移操作会自动在最高位加1，故首先对负数最高位进行处理(与0xFFFFFFF做与运算将最改为变为0)  
还有一种巧妙的做法，任何二进制数减1后即是最右边的1变为0，该位置左边的所有0变为1。  
故每次计算n&(n-1)后都会减少一个1，统计在变为0前能进行几次这样的计算即可。
  
- 答案：
> java 答案1
```java
public class Solution {
    public int NumberOf1(int n) {
        int count = 0;
        if (n<0){
            n = n & 0x7fffffff;
            count ++;
        }
        while(n!=0){
            count += n&1;
            n = n>>1;
        }
        return count;
    }
}
```
> java 答案2
```java
public class Solution {
    public int NumberOf1(int n) {
        int count = 0;
        while(n!=0){
            n = n&(n-1);
            count++;
        }
        return count;
    }
}
```







