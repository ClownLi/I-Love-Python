"""
    希尔排序：
    希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。
    希尔排序是非稳定排序算法。该方法因DL．Shell于1959年提出而得名。 希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
    随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。
    
    思路：
    希尔排序是插入排序的改进，所以还是安装插入排序写
    但是进行比较时，引入了gab值
    
    最优时间复杂度：根据步长序列的不同而不同
    最坏时间复杂度：O(n2)
    稳定想：不稳定 （因为存在分组）
    
    希尔排序通过将比较的全部元素分为几个区域来提升插入排序的性能。这样可以让一个元素可以一次性地朝最终位置前进一大步。
    然后算法再取越来越小的步长进行排序，算法的最后一步就是普通的插入排序，但是到了这步，需排序的数据几乎是已排好的了（此时插入排序较快）。
    """

list_raw = [56, 13, 24, 87, 34, 12, 44]


def shell_sort2(listName):
    n = len(listName)
    gab = n // 2
    
    while gab > 0:
        for i in range(gab, n):
            while i >= gab:
                if listName[i] < listName[i-gab]:
                    listName[i], listName[i-gab] = listName[i-gab], listName[i]
                i -= gab

    gab //= 2

return listName

print(shell_sort2(list_raw))
