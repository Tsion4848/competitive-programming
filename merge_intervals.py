class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        lists = []
        
        lists.append(intervals[0])
        for i in intervals[1:]:
            if lists[-1][0] <= i[0] <= lists[-1][-1]:
                lists[-1][-1] = max(lists[-1][-1], i[-1])
            else:
                lists.append(i)
                
        return(lists)
            
