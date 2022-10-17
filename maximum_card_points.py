class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        summ = sum(cardPoints)
        ws = sum(cardPoints[:n - k])
        res = summ - ws
        
        for i in range(k):
            ws -= cardPoints[i]
            ws += cardPoints[i + n - k]
            res = max(res, summ - ws)
            
        return res
