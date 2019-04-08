458. 目标最后位置

给一个升序数组，找到 target 最后一次出现的位置，如果没出现过返回 -1

输入：nums = [1,2,2,4,5,5], target = 2
输出：2
样例 2：

输入：nums = [1,2,2,4,5,5], target = 6
输出：-1

#这题的边界问题很玄乎，没扣明白是人肉bug出来的
class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if nums == []:
            return -1
        low = 0
        high = len(nums) - 1
        mid = 0
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                    break
        if nums[mid] != target:
                    return -1
        low = mid 
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                low = mid + 1
            elif nums[mid] != target and nums[mid -1] == target:
                return mid - 1
            else:
                high = mid 
        return low        