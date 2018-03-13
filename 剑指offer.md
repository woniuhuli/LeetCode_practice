1. **有序二维数据中的查找**

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


