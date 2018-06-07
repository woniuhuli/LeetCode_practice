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


if __name__ == "__main__":
    s1 = 'abcfbc'
    s2 = 'abfcabc'
    print(LCS2(s1,s2))
    # a =[1, 7, 3, 5, 9, 4,5, 8]
    # print(MAL(a))