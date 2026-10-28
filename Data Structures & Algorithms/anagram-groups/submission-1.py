from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Declare a dictionary whose values are lists
        groups = defaultdict(list)

        # Loop through the words
        for word in strs:
            # Sort the letters and join them into a string key
            key = "".join(sorted(word))

            # Add the original word to that key's bucket
            groups[key].append(word)

        # Return all the buckets as a list
        return list(groups.values())