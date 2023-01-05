
# Initial Approach ------------------
class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        flag,ans = 0,0
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                if strs[j][i] > strs[j+1][i]:
                    flag = 1
            if flag == 1: 
                ans += 1
                flag = 0
        return ans

# second Approach -------------------------------

class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        return sum( any( strs[i][j]<strs[i-1][j] for i in range(1,len(strs)) ) for j in range(len(strs[0])))

# Most Efficient approach ----------------
class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        ret = 0
        for c in zip(*strs): 
            if list(c) != sorted(c): 
                ret += 1
                
        return ret 