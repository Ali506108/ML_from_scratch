from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = defaultdict(int)
        res = float('inf')
        ballon = set("ballon")

        for char in text:
            if char in ballon:
                counts[char]+=1


        for ch in ballon:
            if ch == 'l' or ch == 'o':
                res = min(res , counts[ch]//2)
            else:
                res = min(res , counts[ch])

        return res



    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 0
        right = max(piles)
        res = right

        while left <= right:
            hour = 0
            mid = (left+right)//2

            for p in piles:
                hour += (p+mid-1)//2

            if hour < h :
                res=mid
                right = mid -1
            else:
                left = mid + 1

        return res