class Solution { 
    public boolean hasDuplicate(int[] nums){ 
    HashSet<Integer> set = new HashSet<Integer>(); 
    
    for(int n : nums) 
    { 
        if (set.contains(n)) 
    { 
        return true; 
    } 

    set.add(n); 

    } 

    { 

    return false; 

    } 
    
    /*create a hashset 
    create a for loop to loop through the array 
    for each iteration add the unique value in the hashset 
    if a number is already in the hashset, then program returns false 
    if all numbers are added in the hashset, then return true */ 

        } 
     }