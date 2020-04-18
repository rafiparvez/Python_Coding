from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for i, char in enumerate(order):
            order_map[char] = i

        for i in range(1, len(words)):
            word1 = words[i - 1]
            word2 = words[i]

            # check if first char mismatch is ordered
            for i in range(min(len(word1), len(word2))):
                char1 = word1[i]
                char2 = word2[i]
                if (char1 != char2):
                    # if mismatch is not ordered
                    if order_map[char1] > order_map[char2]:
                        return False
                    # if 1st mismatch is ordered, we
                    # dont need to check further for these words
                    break
            # in case no mismatch found in for loop
            # e.g. prefix "app" occurs after words "apple"
            else:
                if len(word1) > len(word2):
                    return False
        return True
