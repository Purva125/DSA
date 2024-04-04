class Solution(object):
    def isPalindrome(self, x):
        k=str(x)
        if (k==k[::-1]):
            return True
        else:
            return False    
       
