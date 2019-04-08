 
给出一个字符串（假设长度最长为1000），求出它的最长回文子串，你可以假定只有一个满足条件的最长回文串。

样例
样例 1:

输入:"abcdzdcab"
输出:"cdzdc"
样例 2:

输入:"aba"
输出:"aba"
挑战
O(n2) 时间复杂度的算法是可以接受的，如果你能用 O(n) 的算法那自然更好

class Solution {
public:
    /**
     * @param s: input string
     * @return: the longest palindromic substring
     */
    string longestPalindrome(string &s) {
        // write your code here
        if(s.size() == 0) return "";
        if(s.size() == 1) return s;
        int start = 0, end = 0;
        int maxl = 0;
        for(int i = 0; i < s.size(); ++i) {
            int len1 = expand(s, i, i);
            int len2 = expand(s, i, i+1);
            int len = max(len1, len2);
            if(len > end - start) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
                maxl = len ;
            }
        }
        return s.substr(start, maxl);
    }
    
    int expand(string s, int left, int right) {
        int L = left, R = right;
        while(L >= 0 && R < s.size() && s.at(L) == s.at(R)) {
            --L;
            ++R;
        }
        return R - L - 1;
    }
};