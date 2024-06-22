import math
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        elif -2**31 <= dividend <= 2**31 - 1 and -2**31 <= divisor <= 2**31 - 1 and divisor != 0:
            res = int(float(dividend)/float(divisor))
            result = res
            return result
        else: 
            return 0
