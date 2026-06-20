class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # first, check if the two strings are the same size
        # if they aren't the same size, they automatically aren't anagrams
        if len(s) != len(t):
            return False

        # create a hash table to compare the two values
        countS, countT = {}, {}

        # loops through the string
        for i in range (len(s)):
            # add 1 to keep count of the num of times letter occurs
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        # loops through and compares the occurance values
        for c in countS:
            if countS[c] != countT.get(c,0): 
                return False # if there is a value that doesn't match with the other table, return false

        return True # if all values occur at the same time, then return true 



        