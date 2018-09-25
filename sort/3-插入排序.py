"""
    插入排序：
    插入排序（英语：Insertion Sort）是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
    插入排序在实现上，在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。
    
    思路：
    写里面的循环，拿未排序的第一个元素和已经排好序的序列进行比较，如果遇到小于的数，进行替换
    从第二个位置，即下标为1的元素开始向前插入
    
    最优时间复杂度：O(n) （升序排列，序列已经处于升序状态）
    最坏时间复杂度：O(n2)
    稳定性：稳定
    # 是否稳定：比较相同的元素是否位置发生互换
    """

list_raw = [56, 13, 24, 87, 34, 12, 44]

def insert_sort(listName):
    n = len(listName)
    
    for j in range(1,n):
        for i in range(0, j):
            if listName[j] < listName[i]:
                listName[i] , listName[j] = listName[j], listName[i]
    return listName

print(insert_sort(list_raw))

#第二种实现方式
def insert_sort2(listName):
    n = len(listName)
    for i in range(1,n):
        while i > 0:
            if listName[i] < listName[i-1]:
                listName[i], listName[i-1] = listName[i-1], listName[i]
            i -= 1
    return listName

print(insert_sort2(list_raw))
