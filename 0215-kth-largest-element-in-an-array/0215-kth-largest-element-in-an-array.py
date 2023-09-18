class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        freq = dict()

        for element in nums:
            if element not in freq.keys():
                freq[element] = 1
            else:
                freq[element] +=1
        sorted_freq = sorted(freq.items(),key=lambda x:x[0],reverse=True)

        for pair in sorted_freq:
            k-=pair[1]
            if k <= 0:
                return pair[0]
