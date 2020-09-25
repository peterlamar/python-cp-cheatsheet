"""
time: n
space: 1
"""
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        bestSeq = 0
        bestTwoSeq = [0,k]
        bestThreeSeq = [0, k, k*2]
        
        seqSum = sum(nums[0:k])
        seqTwoSum = sum(nums[k:k*2])
        seqThreeSum = sum(nums[k*2:k*3])

        bestSum = seqSum
        bestTwoSum = seqTwoSum + seqSum
        bestThreeSum = seqThreeSum + seqTwoSum + seqSum
        
        seqIdx = 1
        twoSeqIndex = k + 1
        threeSeqIndex = k*2 + 1
        
        while threeSeqIndex <= len(nums) - k:
            seqSum = seqSum - nums[seqIdx - 1] + nums[seqIdx + k - 1]
            seqTwoSum = seqTwoSum - nums[twoSeqIndex - 1] + nums[twoSeqIndex + k - 1]
            seqThreeSum = seqThreeSum - nums[threeSeqIndex - 1] + nums[threeSeqIndex + k - 1]

            if seqSum > bestSum:
                bestSeq = seqIdx
                bestSum = seqSum
            
            if seqTwoSum + bestSum > bestTwoSum:
                bestTwoSeq = [bestSeq, twoSeqIndex]
                bestTwoSum = seqTwoSum + bestSum
            
            if seqThreeSum + bestTwoSum > bestThreeSum:
                bestThreeSeq = bestTwoSeq + [threeSeqIndex]
                bestThreeSum = bestTwoSum + seqThreeSum
            
            seqIdx += 1
            twoSeqIndex += 1
            threeSeqIndex += 1
        
        return bestThreeSeq