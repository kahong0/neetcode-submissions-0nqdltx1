class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length())
        {
            return false; 
        }

        if(s.length() == t.length())
        {
            Map<Character, Integer> letters = new HashMap<>();

            for (char chars : s.toCharArray())
            {
                letters.put(chars, letters.getOrDefault(chars, 0) + 1);
            }

            for (char chars : t.toCharArray())
            {
                letters.put(chars, letters.getOrDefault(chars, 0) - 1);
            }

            for (Integer chars : letters.values())
            {
                if (chars != 0)
                {
                    return false;
                }
            }
        }
        return true;
    }
}

/* 
        check if the strings are the same length, if it's not return false
        if they are the same length, create a new hashmap 
        for loop to iterate through each string s and keep track of the occurances of each value
        then repeat for string t and subtract count from the letter
        if all values are equal to 0 then return true 
        if not return false
*/
