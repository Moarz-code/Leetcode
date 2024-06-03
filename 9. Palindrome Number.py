def isPalindrome( x):
        """
        :type x: int
        :rtype: bool
        """
        inString = str(x)
        # Compare the string with its reverse
        return inString == inString[::-1]
    
    
isPalindrome(121)