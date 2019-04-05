585. 山脉序列中的最大值
给 n 个整数的山脉数组，即先增后减的序列，找到山顶（最大值）
#二分的边界问题要疯狂扣？
样例
例1:

输入: nums = [1, 2, 4, 8, 6, 3] 
输出: 8
例2:

输入: nums = [10, 9, 8, 7], 
输出: 10
class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        if nums == []:
            return -1
        if len(nums) == 1:
            return nums[0]
        if nums[0] > nums[1]:
            return nums[0]
        if nums[-1] > nums[-2]:
            return nums[-1]
        low = 0
        high = len(nums) - 1
        mid = 0
        while low < high:
            mid = low + (high - low) // 2
            if  nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:
                low = mid 
            elif nums[mid] <nums[mid - 1] and nums[mid] > nums[mid + 1]:
                high = mid
            else:
                return nums[mid]