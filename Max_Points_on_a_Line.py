from itertools import combinations


pp = [[1,1],[2,2],[3,3]]

def soln(points):
    ll = len(points) 
    if ll == 1: return 1
    elif ll == 2: return 2
    else:
        ans = 0
        for i in list(combinations(points,2)):
            cnt = 0
            for j in points:
                if (j[1] - i[0][1]) * (i[1][0] - i[0][0]) == (j[0] - i[0][0]) * (i[1][1] - i[0][1]):
                    cnt += 1
            ans = max(ans, cnt)
        return ans

print(soln(pp))
