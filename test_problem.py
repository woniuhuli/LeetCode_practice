'''
题目：
题目描述
五张牌，每张牌由牌大小和花色组成，牌大小2~10、J、Q、K、A，牌花色为红桃、黑桃、梅花、方块四种花色之一。 判断牌型:
牌型1，同花顺：同一花色的顺子，如红桃2红桃3红桃4红桃5红桃6。
牌型2，四条：四张相同数字 + 单张，如红桃A黑桃A梅花A方块A + 黑桃K。
牌型3，葫芦：三张相同数字 + 一对，如红桃5黑桃5梅花5 + 方块9梅花9。
牌型4，同花：同一花色，如方块3方块7方块10方块J方块Q。
牌型5，顺子：花色不一样的顺子，如红桃2黑桃3红桃4红桃5方块6。
牌型6，三条：三张相同 + 两张单。
牌型7，其他。
说明：
1）五张牌里不会出现牌大小和花色完全相同的牌。
2）前面的牌型比后面的牌型大，如同花顺比四条大，依次类推。
输入描述:
输入由5行组成
每行为一张牌大小和花色，牌大小为2~10、J、Q、K、A，花色分别用字符H、S、C、D表示红桃、黑桃、梅花、方块。输出描述:
输出牌型序号，5张牌符合多种牌型时，取最大的牌型序号输出
示例1
输入
2 H
3 C
6 S
5 S
4 S
输出
5

'''
def function(a):
    '''
    :param a: 输入，数组[数字，花色]
    :return:
    '''
    s = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    a = mySort(a)
    flag = []
    if (s.index(a[0][0]) - s.index(a[1][0]) == -1 and s.index(a[1][0]) - s.index(a[2][0]) == -1 \
            and s.index(a[2][0]) - s.index(a[3][0]) == -1 and s.index(a[3][0]) - s.index(a[4][0]) == -1):
        flag.append(5)
    if (a[0][1] == a[1][1] and a[1][1] == a[2][1] and a[2][1] == a[3][1] and a[3][1] == a[4][1]):
        flag.append(4)
    number_list = [a[0][0],a[1][0],a[2][0],a[3][0],a[4][0]]
    number_set = set(number_list)
    number_same = 6-len(number_set)
    if number_same == 4:
        flag.append(2)
    if number_same == 3:
        flag.append(6)
        for i in number_set:
            number_list.pop(i)
        if number_list[0] == number_list[1]:
            flag.append(3)
    if 5 in flag and 4 in flag:
        flag.append(1)
    flag.append(7)
    return min(flag)

def mySort(a):
    s = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for index in range(len(a)):
        tag = False
        for j in range(len(a)-1-index):
            if s.index(a[j+1][0]) < s.index(a[j][0]):
                tag = True
                a[j+1],a[j] = a[j],a[j+1]
        if tag == False:
            return a
    return a
a = ['2H','3C','6S','5S','4S']
print(function(a))
