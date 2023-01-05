class Solution(object):
    def findMinArrowShots(self, points):
        ans,i = (0,1)
        points.sort(key= lambda x:x[1])
        set_edge = points[0][1]
        while i < len(points):
            if points[i][0] <= set_edge:
                i = i + 1
            else:
                ans = ans + 1
                set_edge = points[i][1]

        return ans+1