class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        
        def squarer(num):
            num = str(num)
            total = 0
            for digit in num:
                digit = int(digit)
                total += (digit*digit)
            return total
        
        while n not in seen:
            seen.add(n)
            n = squarer(n)
            if n == 1:
                return True
            
        return False