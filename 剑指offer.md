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
**数值的整数次幂**
- 描述：  
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
  
- 思路：  
利用递归计算,若n为偶数则f(b,n) = f(b,n/2)×f(b,n/2);若n为奇数则f(b,n) = b×f(b,n-1) 
还有一种巧妙的做法，将n写成二进制形式，每次迭代求对应位置的幂值，2^5 = 2^(101) = 2^(100)*2^(001)
  
- 答案：
> python 思路一答案
```python
class Solution:
    def Power(self, base, exponent):
        n = abs(exponent)
        if n==0:
            return 1
        if n == 1:
            return base
        result = self.Power(base,n>>1)
        result *= result#先计算出f(b,n/2)
        if n&1==1:
            result *= base
        if exponent <0:
            result = 1/result
        return result
```
> java 思路二答案
```java
public class Solution {
    public double Power(double base, int exponent) {
        if(base==0){
            if(exponent < 0){
                throw new RuntimeException("分母不能为0");
            }
            else if (exponent == 0){
                return 1;
            }
            else{
                return 0;
            }
        }
        int n;
        double res = 1,curr = base;
        if(exponent<0){
             n = -exponent;
         }
        else{
            n = exponent;
        }
         while(n!=0){
             if((n&1)==1){
                 res *= curr;#二进制对应为1则乘到结果中
             }
             curr *= curr;//记录对应位置幂值即base^1,base^2,base^4.....
             n >>= 1;
         }
         return exponent>0?res:1/res;
  }
}
```
**链表中倒数第k个节点**
- 描述：  
输入一个链表，输出该链表中倒数第k个结点。
  
- 思路：  
1、建立一个栈，依次将链表中值入栈，然后出栈，第k个出栈的元素即为倒数第k个节点，注意对异常值的处理。
2、利用两个指针，先将一个指针后移k步，然后两个指针同时后移，当后一个指针指向null时，前一个指针即指向倒数第k个节点
  
- 答案：
> python 思路一答案
```python
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindKthToTail(self, head, k):
        if k==0 or head ==None:
            return None
        Node_list = []
        count = 0
        while(head):
            Node_list.append(head)
            head = head.next
            count += 1
        if count <k:
            return None
        else:
            return Node_list[-k]
```
> java 思路一答案
```java
import java.util.*
public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
public class Solution {
    public ListNode FindKthToTail(ListNode head,int k){
        if(head == null || k<=0){
            return null;
        }
        Stack<ListNode> st = new Stack<ListNode>();
        int count = 0;
        ListNode current = head;
        while(current!=null){
            st.push(current);
            current = current.next;
            count ++;
        }
        if(k>count){
            return null;
        }
        else{
            while(k>0){
            current = st.pop();
            }
            return current;
        }
    }
}
```
>java 思路二答案
```java
public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
public class Solution {
    public ListNode FindKthToTail(ListNode head,int k){
        if(head == null || k<=0){
            return null;
        }
        ListNode pre,last;
        pre = last = head;
        int i = 0;
        while(last!=null){
            if(i<k){
                last = last.next;
                i++;
            }
            else{
                pre = pre.next;
                last = last.next;
            }
        }
        if(i<k){
            return null;
        }
        else{
            return pre;
        }
    }
}
```
**链表反转**
- 描述：  
输入一个链表，输出该链表的反转。
  
- 思路：  
1、建立一个栈，依次将链表中值入栈，然后依次出栈。  
2、利用两个指针p和q，其中q存head->next,p用于当前节点的反转并往后移当前节点，即head->next = p;p = head;head = q;
  
- 答案：
> python 思路一答案
```python
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead == None:
            return None
        list_node = []
        while(pHead!=None):
            list_node.append(pHead)
            pHead = pHead.next
        list_node = list_node[::-1]
        for i in range(len(list_node)-1):
            list_node[i].next = list_node[i+1]
        list_node[-1].next = None
        return list_node[0]
```
>java 思路二答案
```java
public class Solution {
    public ListNode ReverseList(ListNode head) {
        if (head == null){
            return null;
        }
        ListNode p,q;
        p=q=null;
        while(head!=null){
            q = head.next;
            head.next = p;
            p = head;
            head = q;
        }
        return p;
    }
}
```
**合并两个有序链表**
- 描述：  
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。。
  
- 思路：  
1、按照逻辑来即可  
2、利用递归，每次找到较小节点然后递归实现
  
- 答案：
>java 思路一答案
```java
public class Solution {
    public ListNode Merge(ListNode list1,ListNode list2) {
        if(list1 == null){
            return list2;
        }
        if(list2 == null){
            return list1;
        }
        ListNode head, current;
        if(list1.val<list2.val){
            head = list1;
            list1 = list1.next;
        }
        else{
            head = list2;
            list2 = list2.next;
        }
        current = head;
        while(list1!=null || list2!=null){
            if(list1 == null){
                current.next = list2;
                return head;
            }
            if(list2 == null){
                current.next = list1;
                return head;
            }
            if(list1.val<list2.val){
                current.next = list1;
                current = list1;
                list1 = list1.next;
            }
            else{
                current.next = list2;
                current = list2;
                list2 = list2.next;
            }
        }
        return head;
    }
}
```
>python 思路二答案
```python
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if(pHead1 == None):
            return pHead2
        if(pHead2 == None):
            return pHead1
        if(pHead1.val<pHead2.val):
            pHead1.next = self.Merge(pHead1.next,pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1,pHead2.next)
            return pHead2
```

**树的子结构**
- 描述：  
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
  
- 思路：  
树的题目大多需要利用递归实现，按照根节点->左节点->右节点 这样的顺序进行递归判断。  
在本题中首先从根节点开始查找，如果值相等就开始判断是否存在子结构，若不存在再查找左节点，左节点不存在再查找右节点。
  
- 答案：
> java 答案
```java
public class TreeNode {
    int val = 0;
    TreeNode left = null;
    TreeNode right = null;

    public TreeNode(int val) {
        this.val = val;

    }
}
public class Solution {
    public boolean HasSubtree(TreeNode root1,TreeNode root2) {
        if(root1 == null || root2 == null){
            return false;//任意一个为空返回false
        }
        boolean result = false;
        if(root1.val == root2.val){
            result = Find(root1,root2);//当前节点值相等开始以该节点为起点来找
        }
        if(!result){
            result = HasSubtree(root1.left,root2);//没找到则递归判断左节点
        }
        if(!result){
            result = HasSubtree(root1.right,root2);//左节点没找到，继续找右节点
        }
        return result;
    }
    public boolean Find(TreeNode root1,TreeNode root2){
        if(root2 == null){//目标子树遍历完毕则找到
            return true;
        }
        if(root1 == null){//没找到，但是待匹配树已遍历完毕，则不匹配
            return false;
        }
        if(root1.val != root2.val){//都未遍历完但是当前节点不相等，则不匹配
            return false;
        }
        return Find(root1.left,root2.left) && Find(root1.right,root2.right);
    }
}
```
**树的镜像**
- 描述：  
操作给定的二叉树，将其变换为源二叉树的镜像。
  
- 思路：  
树的递归，类似于先序遍历，先对根节点操作，再对左子树操作，然后对右子树操作。
  
- 答案：
```java
public class Solution {
    public void Mirror(TreeNode root) {
        if(root==null){
            return;
        }
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
        if(root.left!=null){
            Mirror(root.left);
        }
        if(root.right!=null){
            Mirror(root.right);
        }
    }
}
```
**顺时针打印矩阵**
- 描述：  
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，  
例如，如果输入如下矩阵： [[1 2 3 4] [5 6 7 8] [9 10 11 12] [13 14 15 16]]   
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
  
- 思路：  
每一圈打印定位好关键的左上右下位置即可，注意设置终止循环的条件
  
- 答案：
```java
import java.util.ArrayList;
public class Solution {
    public ArrayList<Integer> printMatrix(int [][] matrix) {
        ArrayList<Integer> result = new ArrayList<Integer> ();
        if(matrix.length == 0){
            return result;
        }
        if(matrix[0].length == 0){
            return result;
        }
        int rows = matrix.length;
        int columns = matrix[0].length;
        int left = 0,top = 0,right = columns -1,bottom = rows -1;//四个顶点
        while(left<=right && top <= bottom){
            for(int i = left;i<=right;i++){//从左到右
                result.add(matrix[top][i]);
            }
            for(int i = top+1;i<=bottom;i++){//从上到下
                result.add(matrix[i][right]);
            }
            if(top!=bottom){
                for(int i = right-1;i>=left;i--){//从右到左
                    result.add(matrix[bottom][i]);
                }
                if(left!=right){
                    for(int i = bottom-1;i>top;i--){//从下到上
                        result.add(matrix[i][left]);
                    }
                }
            }
            left++;top++;right--;bottom--;
        }
        return result;
    }
}
```
**包含main函数的栈**
- 描述：  
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
  
- 思路：  
新建一个辅助栈，用来存最小值，入栈时辅助栈栈顶总是最小元素的值  
5 3 4 2 5  
5 3 3 2 2
  
- java答案：
```java
import java.util.Stack;

public class Solution {
    Stack<Integer> dataStack = new Stack<Integer>();
    Stack<Integer> minStack = new Stack<Integer>();//辅助栈，栈顶始终为当前栈的最下值
    public void push(int node) {
        dataStack.push(node);
        if(minStack.isEmpty()|| node<minStack.peek()){
            minStack.push(node);
        }
        else{
            minStack.push(minStack.peek());
        }
    }
    
    public void pop() {
        dataStack.pop();
        minStack.pop();
    }
    
    public int top() {
        return dataStack.peek();
    }
    
    public int min() {
        return minStack.peek();
    }
}
```
**栈的压入弹出顺序**
- 描述：  
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。  
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，  
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
  
- 思路：  
新建一个辅助栈来模拟出栈和入栈的操作，每次入栈后判断辅助栈顶元素是否与当前出栈元素相等，相等则出栈，不相等则入栈
模拟完成后判断辅助栈是否为空，为空则符合栈的操作规则
  
- java答案：
```java
import java.util.ArrayList;
import java.util.Stack;
public class Solution {
    public boolean IsPopOrder(int [] pushA,int [] popA) {
        if(pushA.length == 0 || popA.length == 0){
            return false;
        }
        Stack<Integer> temp = new Stack<Integer>();
        int i = 0;//入栈位置下标
        int j = 0;//出栈位置小标
        while(i<pushA.length){
            temp.push(pushA[i]);//模拟入栈操作
            while(!temp.empty() && temp.peek()==popA[j]){//临时栈顶元素与当前出栈元素相等，则临时栈出栈，模拟出栈操作，出栈元素下标+1
                temp.pop();
                j++;
            }
            i++;//直到临时栈顶元素与当前出栈元素不相等，则入栈下标+1
        }
        return(temp.empty());
    }
}
```
- python答案
```python
class Solution:
    def IsPopOrder(self, pushV, popV):
        if len(pushV) == 0 or len(popV)==0:
            return False
        temp = []
        popIndex = 0
        for item in pushV:
            temp.append(item)
            while len(temp)!= 0 and temp[-1] == popV[popIndex]:
                temp.pop()
                popIndex += 1
        return len(temp)==0
```
**字符串全排列**
- 描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
- 思路
每次将一个字符作为第一个字符，然后剩下字符全排列即可。故利用递归来实现，每一个位置字符与第一个字符交换，剩下的字符递归调用全排列，然后再交换一次使得字符串复原。递归出口为待排列字符串只有一个字符。
- python答案
```python
class Solution:
    def Permutation(self, ss):
        if len(ss)<=1:
            return list(ss)
        ss_set = set() #利用集合进行去重
        def helper(str_list,begin,end):
            if begin == end:
                s = ''
                for ch in str_list:
                    s += ch
                ss_set.add(s)
                return
            for i in range(begin,end+1):
                str_list[i],str_list[begin] = str_list[begin],str_list[i]
                helper(str_list,begin+1,end)
                str_list[i],str_list[begin] = str_list[begin],str_list[i]
        helper(list(ss),0,len(ss)-1)
        return sorted(ss_set) #利用sorted函数进行按照字典排序
```






