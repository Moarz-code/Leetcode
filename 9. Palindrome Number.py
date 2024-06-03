def isPalindrome( x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: 
            return False 
        
        inString = str(x)
        
        if inString == inString[::-1]: 
            return True 
        else: 
            return False  

    
    
isPalindrome(121)