'''
140. 快速幂

计算an % b，其中a，b和n都是32位的非负整数。

您在真实的面试中是否遇到过这个题？  
样例
例如 231 % 3 = 2

例如 1001000 % 1000 = 0

挑战
O(logn)

思路：利用二分法减少计算量，达到测试标准
'''

class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if n == 0:
             return 1 % b
        if n == 1:
             return a % b
        temp = self.fastPower(a, b, n // 2)
        if(n % 2 == 1):
            return temp * temp * a % b 
        else:
            return temp * temp % b 