#  _*_ coding:utf-8 _*_
'''
冒泡排序算法的运作如下：

比较相邻的元素。如果第一个比第二个大（升序），就交换他们两个。
对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
针对所有的元素重复以上的步骤，除了最后一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
'''


def bubble_sort(alist):
    for j in range(len(alist) - 1, 0, -1):

        # j表示每次遍历需要比较的次数，是逐渐减小的

        for i in range(j):

            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


li = [54, 26, 93, 17, 77, 31, 44, 55, 20]

bubble_sort(li)

print(li)
