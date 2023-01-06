class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ans,price = 0,0
        for i in costs.sort():
            price = price + i
            if price <= coins: ans = ans + 1
            else: break
        return ans