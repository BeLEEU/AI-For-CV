'''
428. x的n次幂
实现 pow(x, n). (n是一个整数)

样例
样例 1:

输入: x = 9.88023, n = 3
输出: 964.498
样例 2:

输入: x = 2.1, n = 3
输出: 9.261
样例 3:

输入: x = 1, n = 0
输出: 1
挑战
时间复杂度O(logn)

思路：这题的思路很简单，一个循环，但是这种解题思路简单的题的考察点是优化时间的复杂度，
单纯做循环是会溢出的。已知一个循环的复杂度是O(n),所以我们需要用二分的方法来求解，
此题我们无法得到类似数组中的最大值，我们把目标值设为f(n)，根据乘法的特性可知f(n/2) *f(n/2)
== f(n/2) (这里我们假设n是偶数，如果是奇数 需要再乘以一个x。可知，该提需要用递归来解决，因为
该问题可以化简为数据规模更小的问题，且求解思路完全一致，并且有递归终结式子：当为0时，返回1.

'''
class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def power(self, x, n):
        if n == 0:
            return 1
        half = self.power(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return x * half * half
    def myPow(self, x, n):
        # write your code here
        if n < 0:
            return 1 / self.power(x, -n)
        return self.power(x, n)