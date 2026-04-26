class Solution:

    # Given a string s

    #     it is a palindrome

    #         return true
        
    #     otherwise return false

    # palindrome is a string that reads the same forward and backward

    # case-insensitive and ignores all non-alphanumeric characters.

    # take s 
    #     make it lowercase
    #     remove the spaces
    
    # create asscii checker fun
    #     get char
    #     return char

    # approch two pointers

    # i , j = 0 , size - 1

    # while(i < j):
    #     if(!assciicheker(s[i])):
    #         i+=1
    #     if(!assciicheker(s[j])):
    #         j-=1

    #     if(asscii(s[i]) != asscii(s[i])):
    #         return False
        
    #     i += 1
    #     j -= 1
    
    # return True





    def isPalindrome(self, s: str) -> bool:
        def assciiChecker(c):
            return ((ord(c) >= 65 and ord(c) <= 90) or
             (ord(c) >= 97 and ord(c) <= 122) or
             (ord(c) >= 48 and ord(c) <= 57)  )

        i , j = 0 , len(s) - 1
        while(i < j):
            while(not assciiChecker(s[i]) and i < j):
                i+=1
            while(not assciiChecker(s[j]) and i < j):
                j-=1
            if(ord(s[i].lower()) != ord(s[j].lower())):
                return False
        
            i += 1
            j -= 1
        return True


