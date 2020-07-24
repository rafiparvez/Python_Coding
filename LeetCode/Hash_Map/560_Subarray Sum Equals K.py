"""
Solution 2: Cumulate sum approach
𝑖𝑛𝑝𝑢𝑡=[10,2,−2,−20,10],𝑘=−10,   𝑜𝑢𝑡𝑝𝑢𝑡=3
Explaination: sub-arrays  [10,2,−2,−20],[2,−2,−20,10],[−20,10]  have sum =  −10
Approach Find cumulative sum at each index of the input array.
𝑐𝑢𝑚𝑠𝑢𝑚=[0,10,12,10,−10,0]  for each i, j indices in the list cumsum, if  𝑐𝑢𝑚𝑠𝑢𝑚[𝑖]−𝑐𝑢𝑚𝑠𝑢𝑚[𝑗]=𝑘 , increase the count as one.  𝑐𝑢𝑚𝑠𝑢𝑚[𝑖]−𝑐𝑢𝑚𝑠𝑢𝑚[𝑗]  represents sub-array sum for  𝑖𝑛𝑝𝑢𝑡[𝑖+1::𝑗]
Complexity Analysis
Time complexity :  𝑂(𝑛2)
Cumulative sum can be evaluated in  𝑂(𝑛)  time. Considering every possible subarray takes  𝑂(𝑛2)  time.

Space complexity :  𝑂(𝑛)  for storing cumulative sums
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cum_sum = [0]
        count = 0
        for num in nums:
            cum_sum.append(cum_sum[-1] + num)
        for i in range(1, len(cum_sum)):
            for j in range(i):
                sub_array_sum = cum_sum[i] - cum_sum[j]
                if sub_array_sum == k:
                    count +=1
        return count


"""
Solution 3: Cumulate sum approach and hashmap
𝑖𝑛𝑝𝑢𝑡=[10,2,−2,−20,10],𝑘=−10,   𝑜𝑢𝑡𝑝𝑢𝑡=3 
Explaination: sub-arrays  [10,2,−2,−20],[2,−2,−20,10],[−20,10]  have sum =  −10 
Approach Instead of evaluating every sub-array sum, cache sub-array sums and their counts in hashmap

Time Complexity:  𝑂(𝑛) 
Space Complexity:  𝑂(𝑛)
"""
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0

        ## prev_sum --> count
        prev_sum_counts = defaultdict(int)

        for num in nums:
            curr_sum += num

            if curr_sum == k:
                count += 1

            required_sum = curr_sum - k

            if required_sum in prev_sum_counts:
                count += prev_sum_counts[required_sum]
            prev_sum_counts[curr_sum] += 1

        return count
