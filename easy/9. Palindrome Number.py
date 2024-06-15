class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_as_str = str(x)
        reverse_x = x_as_str[::-1]
        if x_as_str == reverse_x:
            return True
        else:
            return False
