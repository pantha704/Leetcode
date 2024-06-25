# Code 1 :

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = 0
        neg = False
        if x<0:
            neg = True
            x *= -1

        while x>0:
            r = r*10 + x%10
            x /= 10

        if neg:
            x = x - r
        else:
            x = x + r
        print(x)

        if not -2**31 <= x <= 2**31 - 1:
            return 0
        return x









# Code 2 :

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if x < 0:
            x *= -1
            neg = True

        x = int(str(x)[::-1])

        if neg:
            x *= -1

        if -2**31 <= x <= 2**31-1:
            return x
        return 0 
