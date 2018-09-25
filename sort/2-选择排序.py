"""
    选择排序：
    选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。
    首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，
    再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
    
    思路:
    先写里面的循环，设定一个游标min_index,依次去比较，找到最小值，放在序列头部
    外面的循环 是指需要选择几次
    
    最优时间复杂度：O(n2)
    最坏时间复杂度：O(n2)
    稳定性：不稳定（考虑升序每次选择最大的情况
    """

list_raw = [13, 56, 24, 87, 34, 12, 44]

def select_sort(listName):
    n = len(listName)
    
    for j in range(0, n-1):
        min_index = j
        for i in range(j+1, n):
            if listName[min_index] > listName[i]:
                min_index = i
        listName[j], listName[min_index] = listName[min_index], listName[j]
    
    return listName

print(select_sort(list_raw))
