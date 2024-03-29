class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr).most_common()
        count.sort(key=lambda c: -c[1])
        
        sum = 0
        for i, c in enumerate(count):
            sum = sum + c[1]
            if sum >= len(arr) // 2:
                return i + 1
