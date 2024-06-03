def isPalindrome( x):
        """
        :type x: int
        :rtype: bool
        """
        inString = str(x)
        
        if len(inString) % 2 != 0: 
           num = (len(inString) - 1)//2
        else:
           num = len(inString)//2
        
        left=  inString[:num]
        right=  inString[-num:]
        print(left)
        print(right)
        
        if left == right[::-1]: 
            return True  
        else: 
           return False 

isPalindrome(121)