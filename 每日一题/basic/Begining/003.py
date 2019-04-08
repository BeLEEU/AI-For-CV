415. 有效回文串

给定一个字符串，判断其是否为一个回文串。只考虑字母和数字，忽略大小写。
样例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
解释: "amanaplanacanalpanama"
样例 2:

输入: "race a car"
输出: false
解释: "raceacar"
import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        s=re.sub(r'[^a-z0-9]', "",s)
        for i in range(int(len(s)/2)):
            if s[i]!=s[len(s)-1-i]:
                return False
        return True