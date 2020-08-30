"""
time: 1hr + fist round, then 5 min
https://www.i-programmer.info/programming/theory/2744-how-not-to-shuffle-the-kunth-fisher-yates-algorithm.html

"""

class Solution:

    def __init__(self, nums: List[int]):
        self.orig = nums
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.orig
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        shuffle = self.orig[:]
        for i, l in enumerate(shuffle):
            r = random.randrange(0+i, len(shuffle))
            shuffle[i], shuffle[r] = shuffle[r], shuffle[i]
        return shuffle
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()