'''
75. 寻找峰值
 
你给出一个整数数组(size为n)，其具有以下特点：

相邻位置的数字是不同的
A[0] < A[1] 并且 A[n - 2] > A[n - 1]
假定P是峰值的位置则满足A[P] > A[P-1]且A[P] > A[P+1]，返回数组中任意一个峰值的位置。

数组保证至少存在一个峰
如果数组存在多个峰，返回其中任意一个就行
数组至少包含 3 个数
您在真实的面试中是否遇到过这个题？  
样例
样例 1:
	输入:  [1, 2, 1, 3, 4, 5, 7, 6]
	输出:  1 or 6
	
	解释:
	返回峰顶元素的下标


样例 2:
	输入: [1,2,3,4,1]
	输出:  3

挑战
Time complexity O(logN)
思路：两边一起寻找的话会更快
'''


class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        if len(A) == 3:
            return 1
        for i in range (1, len(A)-1):
            if A[i] > A[i-1] and A[i] > A[i+1]:
                return i
            if A[len(A)-1-i] > A[len(A)-i] and A[len(A)-1-i] > A[len(A)-1-i-1]:
                return len(A)-1-i
        return None