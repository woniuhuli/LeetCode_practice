# 排序算法

这里是各种排序算法的分析总结以及代码实现，包括java和python  

## 冒泡排序

### 1、算法思想
- 冒泡排序思想是多次比较，每一轮最大值都会被放到最后，经过n-1轮后序列即是有序的。  

- 算法过程：
    1. 比较相邻两个元素，前者比后者小就交换顺序，直到序列最后一个元素
    2. 重复以上步骤直到排序完成
    3. 改进：设置标志位，遍历一次后没有产生交换，则序列已经有序，提前返回
- 排序过程如图
![冒泡算法](https://github.com/woniuhuli/LeetCode_practice/blob/master/src/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F.gif?raw=true)  

### 2、代码实现

- python代码实现
```python
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
```
- java代码实现
```java
public static int[] bubbleSort(int[] array){
    for(int i = 0; i<array.length;i++){
        for(int j = 0;j<array.length-i-1;j++){
            if(array[j]>array[j+1]){
                int temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }
    }
    return array;
}
```  
### 3、算法分析
最佳情况：即序列开始就是有序的，通过设置标志位，遍历一次发现没有发生交换即返回，复杂度为O(n)  
最差情况：需要进行比较及交换的次数为$(n-1)+(n-2)+(n-3)+...1 = \frac{n(n-1)}{2}$ 复杂度为O(n^2)  
平均情况：复杂度为O(n^2)  
稳定性：由于每次比较相等时并没有进行交换(判断条件为<),故该算法是稳定的。
空间复杂度：O(1)

## 选择排序

### 1、算法思想
选择排序思想很简单直观，每次选择序列中最小元素放在已排序序列后面，经过n轮选择后序列即为有序序列。  
这种算法最为稳定，不管序列是怎样的，复杂度都是O(n^2)，不会额外占用内存  
示意图如下![选择排序](https://github.com/woniuhuli/LeetCode_practice/blob/master/src/%E9%80%89%E6%8B%A9%E6%8E%92%E5%BA%8F.gif?raw=true)

### 2、代码实现
- python实现
```python
def selectSort(array):
    for i in range(len(array)-1):
        minindex = i
        for j in range(i+1,len(array)):
            if array[j] < array[minindex]:
                minindex = j
        array[i],array[minindex] = array[minindex],array[i]
    return array
```
- java实现
```java
public static int[] selectSort(int[] array){
    for(int i=0;i<array.length-1;i++){
        int minindex = i;
        for(int j = i+1;j<array.length;j++){
            if(array[j] < array[minindex]){
                minindex = j;
            }
        }
        int temp = array[i];
        array[i] = array[minindex];
        array[minindex] = temp;
    }
    return array;
}
```
### 算法分析
- 时间复杂度：不论初始序列是怎样的 都需要进行n-1轮的比较以及n-1次交换，其时间复杂度为  
$(n-1)+(n-2)+(n-3)+...+1 = \frac{n(n-1)}{2}$ 即O(n^2)  
- 稳定性：由于在每一轮比较后都是将未排序序列最小元素与未排序首位元素进行交换位置，故该算法不稳定。
- 空间复杂度：O(1)

## 插入排序

### 算法思想  

- 和选择排序一样，分为有序序列和无序序列，每一次将无序序列插入到有序序列中，将无序序列全插入有序序列即可完成排序  
- 算法过程：
    1. 将第一个元素看做有序序列，其后看做无序序列
    2. 取无序序列第一个元素当做新元素，在有序序列中从后往前扫描
    3. 如果该元素大于新元素，则该元素后移一个位置
    4. 重复步骤3，直到该位置元素小于或者等于新元素位置，将新元素插入该位置。
    5. 重复步骤2-4，直到无序序列为空
 
其排序过程如下图：![插入排序](https://github.com/woniuhuli/LeetCode_practice/blob/master/src/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F.gif?raw=true)  

### 代码实现
- python实现
```python
def insertSort(array):
    for i in range(1,len(array)):
        while(array[i]<array[i-1] and i>=1):
            array[i],array[i-1] = array[i-1],array[i]
            i -= 1
    return array          
```
- java实现
```java
public static int[] insertSort(int[] array){
    if(array.length<=1){
        return array;
    }
    for(int j = 1;j<array.length;j++){
        int i = j;
        while(i>=1 && array[i]<array[i-1]){
            int temp = array[i];
            array[i] = array[i-1];
            array[i-1] = temp;
            i--;
        }
    }
    return array;
}
```
### 算法分析
- 时间复杂度
 最佳情况：已经是有序序列，则每轮只需比较一次，故时间复杂度为O(n)  
 最差情况：O(n^2)  平均情况：O(n^2)
- 空间复杂度：  O(1) 
- 稳定性：每次只是相邻元素根据大小交换顺序，是一种稳定的排序算法

## 希尔排序  

###算法思想  
希尔排序基于这样一个事实:序列有序性越强，插入排序的效率越高。  
>Indeed, when the number of inversions is low, insertion sort(as well as shellsort) is likely to be faster than any sorting method.

实际上希尔排序就是增量不断缩小的插入排序，一般用到的增量序列为[n/2,n/4,...1] 当n=1时实际上就是对整个序列进行了插入排序。  
其具体过程如下图所示![希尔排序](https://github.com/woniuhuli/LeetCode_practice/blob/master/src/%E5%B8%8C%E5%B0%94%E6%8E%92%E5%BA%8F.jpg?raw=true)
  
### 代码实现
- python实现
 ```python
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
```

- java实现
```java
public static int[] shellSort(int[] array) {
	int temp,gap = array.length/2;
	while(gap>0) {
		for(int i= gap;i<array.length;i++) {
			temp = array[i];
			int j = i-gap;
			while(j>=0 && array[j]>temp) {
				array[j+gap] = array[j];
				j -= gap;
			}
			array[j+gap] = temp;
		}
		gap /= 2;
	}
	return array;
}
```
### 算法分析
- 时间复杂度：$O(nlog_2 n)$
- 空间复杂度：O(1)
- 稳定性：由于希尔排序每次是隔着gap个元素交换，故该算法不稳定

## 归并排序  

### 算法思想  
归并排序采取分而治之的思想。将无序序列分为两个两个序列，先分别对两个小序列排序，再将两个小序列进行合并。  
在具体实施时，小序列排序同样可以采样分而治之的方法来进行。这样可以一直分，直到每个小序列中只有一个元素，该序列自然是有序的。  
于是归并排序主要在与合并，将两个有序序列合并到一起可以借助另一个数组快速完成：每次进入辅助数组中的数是两个有序数组的最小值。  
由于两个数组本身是有序的，故只需比较两个有序数据的第一个元素即可。  
其排序过程如下图![归并排序](https://github.com/woniuhuli/LeetCode_practice/blob/master/src/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F.gif?raw=true)

### 算法实现  
算法分为两个过程，首先将是“分”，一直分到每个部分自有一个元素，然后开始“合”，将所有小序列合并成一个有序序列。  
- python实现
```python
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
```
- java实现
```java
public static int[] merge(int[] left, int[] right) {
	int length = left.length+right.length;
	int[] array = new int[length];
	for(int index = 0,left_index = 0,right_index = 0;index<length;index++) {
		if(left_index>=left.length) {
			array[index] = right[right_index++];
		}
		else if (right_index>=right.length) {
			array[index] = left[left_index++];
		}
		else if (left[left_index]<=right[right_index]) {
			array[index] = left[left_index++];
		}
		else {
			array[index] = right[right_index++];
		}
	}
	return array;
}
public static int[] mergrSort(int[] array) {
	if(array.length < 2) {
		return array;
	}
	int mid = array.length/2;
	int[] left = Arrays.copyOfRange(array, 0, mid);
	int[] right = Arrays.copyOfRange(array, mid, array.length);
	return merge(mergrSort(left),mergrSort(right));
}
```

### 算法分析
- 时间复杂度：同选择排序一样，其时间复杂度与输入序列状态无关，都是O(nlogn). 同关于时间复杂度分析可以查看[这个连接](http://mp.weixin.qq.com/s/YNF-6vY5m2Q_kEXJbep5NQ)
- 空间复杂度：O(n)
- 稳定性：由于在合并时，当左边元素等于右边元素时，是左边元素先进入新序列，故顺序还是不变，故该算法是稳定的。

## 快速排序

### 算法思想 
快速排序实际上是一种二分的思想。每一次选择一个元素作为基准，小于基准的数放在基准左边，大于基准的数放在基准的右边。然后分别对两边的序列进行相同的操作，直到每一边都只有一个元素，那么序列即为有序的。  
每一次的操作称为分区（partition），其过程如下：  
1. 选择第一个数作为基准，选择指针i指向第二个数，指针j指向而后一个数
2. 指针j与基准比较，大于基准就左移，直到小于基准停下
3. 指针i与基准计较，小于基准就右移，直到大于基准停下
4. 交换指针i与指针j位置的元素
5. 重复2-4步，直到i与j相遇，将第一个元素（基准元素）与位置i交换。
  
整个快速排序算法就是不断的递归调用分区操作，直到每个区都只有一个元素，则整个序列有序。

其排序过程示意图如下所示![快速排序](https://github.com/woniuhuli/LeetCode_practice/blob/master/src/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F.gif?raw=true)

### 代码实现
- python实现
```python
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
```
- java实现
```java
public static void partition(int[] array,int left,int right) {
	if(left>right) {
		return;
	}
	int base = array[left];
	int i = left,j = right;
	while(i!=j) {
		while(i<j && array[j]>=base) {
			j--;
		}
		while(i<j && array[i]<=base) {
			i++;
		}
		if(i<j) {
			int temp = array[i];
			array[i] = array[j];
			array[j] = temp;
		}
	}
	array[left] = array[i];
	array[i] = base;
	partition(array, left, i-1);
	partition(array, i+1, right);
}
public static int[] quickSort(int[] array) {
	int left = 0;
	int right = array.length-1;
	partition(array, left, right);
	return array;
}
```

### 算法分析
- 时间复杂度：和冒泡排序很像，快速排序也是经过交换将较大数放在右边较小数放在左边。但是由于快速排序每次交换时跳跃式的，而冒泡排序每次都是和相邻元素进行交换位置，故快速排序相较冒泡排序效率要高。最坏情况时，快速排序交换次数和冒泡排序一样，其时间复杂度为O(n^2)，最好和最坏情况都是O(nlog(n))  
- 空间复杂度：O(log(n))
- 稳定性：由于快速排序有跳跃式交换的过程，故快速排序是一种不稳定的算法

## 堆排序

### 算法思想
堆排序借助堆这种数据结构进行排序。堆是一种特殊的完全二叉树，对于小(大)根堆，父节点总是小于(大于)其左右孩子。因此如果我们首先对无序数据建大根堆，然后每次都将根节点移除到临时数组中，移除后维护堆，使其仍然是大根堆。那么重复此操作直到堆为空为止。  
那么程序的关键在与建堆以及堆的维护了。  
#### 二叉堆
- 概念：二叉堆是一种特殊的完全二叉树。完全二叉树：除了最后一层外，每一层的节点数达到最大，而且最后一层节点都集中在最左边。而二叉堆则是父节点都小于(大于)左右孩子的完全二叉树，其左右孩子的大小关系不确定。  
- 储存：完全二叉树有个好处，将其用数组(0位置空出来)存放时，a[n]的左孩子一定是a[2*n],右孩子一定是a[2*n+1],其父亲一定是a[int(n/2)]
- 好处：若要每次都找到最小值，这种数据的好处在于其插入和删除元素的时间复杂度都很低  

1. 元素插入  
    新元素插入时可能会破坏堆的次序，这时候需要将新元素上浮到对应位置，使得该数组仍然是小根堆。
    将新元素与其父节点比较，如果小于父节点则该元素上浮至其父节点位置，重复该上浮操作，直到该元素成为根节点或者大于其父节点。
    ```python
    def swim(array,index):#将index位置元素上浮
       if index == 1:#父节点直接返回
           return 
       parent = int(index/2)
       if(array[index]<array[parent]):#当前节点小于父节点交换
           array[index],array[parent] = array[parent], array[index]
           swim(array,parent)#继续对父节点进行上浮操作
    ```  
2. 元素删除  
    对于大根堆，删除堆顶的最大元素时，我们可以将最后一个元素与第一个元素交换，新数组长度减一，逻辑上删除最大元素。这时根节点并不满足大根堆的要求，需要将其下沉到对应位置。下沉时我们可以将该节点与两个孩子的较大孩子比较，若小于较大孩子则与较大孩子交换位置。然后对该元素继续进行下沉操作，直到其大于两个孩子，或者是叶子节点。
    ```python
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
    ```
3. 建堆  
    对一个无序列表进行建堆时，可以考虑从头到尾依次插入堆，但是这样做需要做的上浮操作为N，时间复杂度较高。  
    我们可以将数列看做一个完全二叉树，所有叶子节点看做数目为1的堆，那么从第一个非叶子节点开始依次往上做下沉操作，直到根节点，则二叉树变成了二叉堆。
    ```python
    def buildHeap(array):
       current = len(array)//2-1 #第一个非叶子节点
       while(current>=0):
           sink(array,len(array),current)
           current -= 1
    ```
4. 堆排序  
    1. 对于一个无序数组，首先对其建堆，使其满足大根堆的次序，那么根节点（也即数组第一个元素）即为数据最大值。
    2. 将a[0]与a[n]交换位置，则认为a[n]为有序的，a[0:n-1]不再满足大根推次序。
    3. 对a[0:n-1]执行下沉操作，使其仍然为大根堆。
    4. 重复操作2、3步，直到所有元素都有次序（也即交换到了a[0])
5. 堆排序的过程如下所示![堆排序](https://github.com/woniuhuli/LeetCode_practice/blob/master/src/%E5%A0%86%E6%8E%92%E5%BA%8F.gif?raw=true)

### 算法实现
- python实现
```python
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
```
- java实现
```java
public static void sink(int[] array,int heapSize, int index) {
	int leftChild = index*2+1;
	if(leftChild >= heapSize) {
		return;
	}
	int maxIndex = index;
	int rightChild = leftChild+1;
	if(array[leftChild]>array[maxIndex]) {
		maxIndex = leftChild;
	}
	if(rightChild < heapSize && array[rightChild]>array[maxIndex]) {
		maxIndex = rightChild;
	}
	if(maxIndex != index) {
		int temp = array[index];
		array[index] = array[maxIndex];
		array[maxIndex] = temp;
		sink(array, heapSize, maxIndex);
	}
}
public static void bulidHeap(int[] array) {
	if(array.length < 2) {
		return;
	}
	for(int i=array.length/2 -1;i>=0;i--) {
		sink(array, array.length, i);
	}
}
public static int[] heapSort(int[] array) {
	bulidHeap(array);
	int heapSize = array.length;
	for(int i= heapSize-1;i>=0;i--) {
		int temp = array[i];
		array[i] = array[0];
		array[0] = temp;
		sink(array, i, 0);
	}
	return array;
}
```
### 算法分析
- 时间复杂度：O(nlogn) 分析见这个[链接](http://mp.weixin.qq.com/s/4AvOsuwQlcut9DSZjiSTfw)
- 空间复杂度：O(1)
- 稳定性：不稳定（在下沉时会跳跃性的交换位置） 

## 计数排序

### 算法思想
计数排序思想核心在与对原数组中每个数值大小的数进行计数，存到另外一个数组中，第i个数据为原始数组中第i大元素的个数。因此计数排序只能对固定范围的整数数组进行排序  
在排序时，每次取一个新数组中的元素，对应值减1，新数组中值全为0则原数组排好序了。其排序过程如下图所示![计数排序](https://github.com/woniuhuli/LeetCode_practice/blob/master/src/%E8%AE%A1%E6%95%B0%E6%8E%92%E5%BA%8F.gif?raw=true)

### 代码实现
- python实现
```python
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
```

### 算法分析
- 时间复杂度：O(n),找最大最小值需要n步比较，初始化辅助数组需遍历一次原数组，为原数组赋新值依然需要遍历辅助数组，需n步赋值操作。
- 空间复杂度：O(k),k为原始数组中数据范围
- 稳定性：由于对原始数组进行重新赋值，故其实不存在稳不稳定（也可认为是稳定的）

## 桶排序

### 算法思想

桶排序和计数排序一样，也是一种非比较排序（只不过在每个桶的内部采用的排序算法可能需要比较)。桶排序首先将原始数组按照映射函数映射到i个桶中（如0-99之间的数按照十位上的数可以映射到10个桶中），然后对每个桶内元素进行排序（可以用不同的排序方式），最后按照桶的顺序依次将不同桶中的数据拼接起来即是有序序列。  
其排序示意图如下所示：![桶排序](https://github.com/woniuhuli/LeetCode_practice/blob/master/src/%E6%A1%B6%E6%8E%92%E5%BA%8F.jpg?raw=true)

###代码实现
- python
```python
def bucketSort(array,bucketsize):
    max_value = max(array)
    min_value = min(array)
    bucketcount = (max_value - min_value)//bucketsize + 1#桶的个数，尽量使每个桶中的元素一直
    bucketList = [[] for i in range(bucketcount)]#桶的初始化
    for item in array:
        bucketList[(item-min_value)//bucketsize].append(item)
    for buncket in bucketList:#每个桶采用快速排序来排
        buncket = quickSort(buncket)
    i = 0
    for buncket in bucketList:#依次取每个桶中的元素
        for item in buncket:
            array[i] = item
            i += 1
    return array
```




