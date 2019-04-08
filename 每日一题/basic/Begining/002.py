13.字符串查找

对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。如果不存在，则返回 -1。

样例
样例  1:
	输入: source = "source" ， target = "target"
	输出:-1
	
	样例解释: 
	如果source里没有包含target的内容，返回-1

样例 2:
	输入: source = "abcdabcdefg" ，target = "bcd"
	输出: 1
	
	样例解释: 
	如果source里包含target的内容，返回target在source里第一次出现的位置

class Solution {
public:
    /**
     * @param source: 
     * @param target: 
     * @return: return the index
     */
    int strStr(string &source, string &target) {
        // Write your code here
        if(target.size()==0)
        return 0;
        int count = 0;
        int len = source.size();
        for(int i = 0; i < len; i++)
        {
            for(int j = i; j < len; j++)
            {
                if(source[j] == target[count])
                {
                    count++;
                    if(count == target.size()){
                        return j-count+1;
                    }
                }else if(source[j]!=target[count]){
                    count = 0;
                    continue;
                }
            }
        }
        return -1;
    }
};