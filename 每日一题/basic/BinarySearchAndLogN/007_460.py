'''
460. 在排序数组中找最接近的K个数
给一个目标数 target, 一个非负整数 k, 一个按照升序排列的数组 A。在A中找与target最接近的k个整数。返回这k个数并按照与target的接近程度从小到大排序，如果接近程度相当，那么小的数排在前面。

k是一个非负整数，并且总是小于已排序数组的长度。
给定数组的长度是正整数, 不会超过 10^410
​4
​​ 
数组中元素的绝对值不会超过 10^410
​4
​​ 
您在真实的面试中是否遇到过这个题？  
样例
样例 1:

输入: A = [1, 2, 3], target = 2, k = 3
输出: [2, 1, 3]
样例 2:

输入: A = [1, 4, 6, 8], target = 3, k = 3
输出: [4, 1, 6]

思路：在一个有序的数组中做查找时，往往是使用二叉树来进行的（因为二叉树的复杂度室友logn，效率
极高），我们需要去找到或者逼近这个数（因为不一定存在），同时需要验证左边是否存在某一个数与target
的值和当前值与target的值是否相等，如果有，需要左移）。
最后是判断 数组中的接近值
'''
class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        low = 0
        high = len(A) - 1
        mid = 0 
        tar = 0
        while(low < high):
            mid = low + (high -low) // 2
            if A[mid] > target:
                high = mid - 1
                tar = high
            elif A[mid] < target:
                low = mid + 1
                tar = low
            else:
                tar = mid
                break
        lis = []
        l = tar
        while abs(A[l] - target) >= abs(A[l - 1] - target):
            l = l - 1
        h = l + 1
        while k > 0:
            if l < 0:
                lis.append(A[h])
                h = h + 1
                k = k - 1
            elif h > len(A) - 1:
                lis.append(A[l])
                l = l - 1
                k = k - 1
            elif abs(A[l] - target) <= abs(A[h] - target):
                lis.append(A[l])
                l = l - 1
                k = k - 1
            elif abs(A[l] - target) > abs(A[h] - target):
                lis.append(A[h])
                h = h + 1
                k = k - 1
        return lis