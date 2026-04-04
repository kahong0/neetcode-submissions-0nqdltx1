# import statement 
from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs):
        # creates the dictionary that takes in a list
        anagrams_dict = defaultdict(list) 

        # loop through each word
        for s in strs:
            # create a 26-letter count array, one slot per letter
            count = [0] * 26
            # counts the amount of letters in the word
            for c in s:
                count[ord(c) - ord('a')] += 1

            # convert the list into a dictionary key
            key = tuple(count) 
            # add word to dictionary 
            anagrams_dict[key].append(s)

        # return the results
        return list(anagrams_dict.values())