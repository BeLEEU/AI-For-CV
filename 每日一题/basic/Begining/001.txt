627. 最长回文串

给出一个包含大小写字母的字符串。求出由这些字母构成的最长的回文串的长度是多少。
数据是大小写敏感的，也就是说，"Aa" 并不会被认为是一个回文串。

样例
样例 1:

输入 : s = "abccccdd"
输出 : 7
说明 : 
一种可以构建出来的最长回文串方案是 "dccaccd"。

class Solution {
public:
    /**
     * @param s: a string which consists of lowercase or uppercase letters
     * @return: the length of the longest palindromes that can be built
     */
    int longestPalindrome(string &s) {
        // write your code here
        std::vector<int> hash(52,0);
        for(char c:s){
            hash[c - (isupper(c)?'A':'a'-26)]++;
        }
        int sum = 0;
        for(int i:hash){
            sum += i/2 * 2;
        }
        return sum==s.size()?sum:sum+1;
    }
};