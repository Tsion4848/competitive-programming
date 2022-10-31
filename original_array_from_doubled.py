class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        original = []
        x = deque()
        changed.sort()
        for i in changed:
            if x and i == x[0]:
                x.popleft()
            else:
                x.append(i * 2)
                original.append(i)
                
        return [] if x else original
