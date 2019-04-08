 
����һ���ַ��������賤���Ϊ1000�����������������Ӵ�������Լٶ�ֻ��һ����������������Ĵ���

����
���� 1:

����:"abcdzdcab"
���:"cdzdc"
���� 2:

����:"aba"
���:"aba"
��ս
O(n2) ʱ�临�Ӷȵ��㷨�ǿ��Խ��ܵģ���������� O(n) ���㷨����Ȼ����

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