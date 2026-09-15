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