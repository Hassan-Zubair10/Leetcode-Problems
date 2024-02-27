class Solution:
    def merge_if_overlapping(self, A, B):
        if not (A[1] < B[0]):
            return (min(A[0], B[0]), max(A[1], B[1]))
        return None
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return None
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            merged_interval = self.merge_if_overlapping(result[-1], intervals[i])
            print(merged_interval)
            if merged_interval is not None:
                result.pop()
                result.append(merged_interval)
            else:
                result.append(intervals[i])
        return result