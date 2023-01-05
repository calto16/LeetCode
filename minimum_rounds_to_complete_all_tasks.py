class Solution(object):
    from collections import Counter
    def minimumRounds(self, tasks):
        count = Counter(tasks)
        ans = 0
        for j in count.values():
            if j < 2: 
                return -1
            ans+= j//3 + bool(j%3)
        return ans