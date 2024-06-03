def isPalindrome( x):
        """
        :type x: int
        :rtype: bool
        """
        inString = str(x)
        
        if len(inString) % 2 != 0: 
           left=  inString[:(len(inString) -1)/2]
           right = inString[:-(len(inString) -1)/2]
           print(right)
           print(left)

isPalindrome(121)