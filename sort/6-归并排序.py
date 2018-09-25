"""
    归并排序:
    是采用分治法的一个非常典型的应用。归并排序的思想就是先递归分解数组，再合并数组。
    将数组分解最小之后，然后合并两个有序数组，基本思路是比较两个数组的最前面的数，谁小就先取谁，取了后相应的指针就往后移一位。
    然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来即可。
    """

list_raw = [56, 13, 24, 87, 34, 12, 44, 32, 11, 99]

def resolve_sort(listName):
    if len(listName) <= 1:
        return listName
    num = len(listName) // 2
    left = resolve_sort(listName[:num])
    rigth = resolve_sort(listName[num:])
    #！！！注意此处存在递归 ， 拆分后， 合并过程也是逐级合并
    return merge(left, rigth)

def merge(left, right):
    l, r = 0, 0
    result = []
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result

print(resolve_sort(list_raw))
