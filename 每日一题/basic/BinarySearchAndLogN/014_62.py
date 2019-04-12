'''
62. 搜索旋转排序数组

假设有一个排序的按未知的旋转轴旋转的数组(比如，0 1 2 4 5 6 7 可能成为4 5 6 7 0 1 2)。给定一个目标值进行搜索，如果在数组中找到目标值返回数组中的索引位置，否则返回-1。

你可以假设数组中不存在重复的元素。

您在真实的面试中是否遇到过这个题？  
样例
例1:

输入: [4, 5, 1, 2, 3] and target=1, 
输出: 2.
例2:

输入: [4, 5, 1, 2, 3] and target=0, 
输出: -1.
'''
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if A == []:
            return -1
        low = 0
        high = len(A) - 1
        while low <= high:
            mid = (low + high)//2
            if A[mid]==target :
                return mid
            if A[mid] >= A[low]:
                if A[low] <=target and A[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if A[high] >= target and A[mid] <= target:
                    low = mid + 1
                else:
                    if mid == 0:
                        high = mid
                    else:
                        high = mid - 1