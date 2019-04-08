'''
159. 寻找旋转排序数组中的最小值

假设一个排好序的数组在其某一未知点发生了旋转（比如0 1 2 4 5 6 7 可能变成4 5 6 7 0 1 2）。

你需要找到其中最小的元素。

你可以假设数组中不存在重复元素。

您在真实的面试中是否遇到过这个题？  
样例
Example 1:

Input：[4, 5, 6, 7, 0, 1, 2]
Output：0
Explanation：
数组中的最小值为0
Example 2:

Input：[2,1]
Output：1
Explanation：
数组中的最小值为1

思路：从旋转的例子上来看，数值大小的分布呈由小到大再由大到小，并且旋转后的数组左边的最小值大于
右边的最大值。
讨论边界：
假如旋转的位置是0，也就是没有旋转，那么返回第一个数
假如旋转的位置是最后一位，则直接返回最后一个数
使用二分法：
我们先以4567012为例，当 mid 落在 数值 7 上面时，此时它比low、high两点都大，说明它属于
原先由右侧旋转过去的数，此时最小值必然在它的左部分。
此时low点变为7，high仍为2，此时mid为0，此时他比low小，比high小，说明它属于原先左部分数组，
此时最小值可能是它或者为它的左部分值
注：在改变low或者high的值时候，注意及时判断此点是否是最小值
'''

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        if nums == None:
            return None
        low = 0
        high = len(nums) - 1
        if nums[low] < nums[high]:
            return nums[0]
        if nums[high] < nums [high - 1]:
            return nums[high]
        while(low <= high):
            mid = low +(high - low) // 2
            if nums[low] > nums[mid] < nums[high]:
                high = mid 
                if nums[high] <= nums[high - 1] and nums[high] <= nums[high + 1]:
                           return nums[high]
            else:
                low = mid + 1
                if nums[low] <= nums[low - 1] and nums[low] <= nums[low + 1]:
                           return nums[low]
        return None