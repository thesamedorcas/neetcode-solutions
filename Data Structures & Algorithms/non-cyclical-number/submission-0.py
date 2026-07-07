class Solution:
    def isHappy(self, n: int) -> bool:
        slow=n
        fast=self.calc(n)

        while slow!=fast:
            fast= self.calc(fast)
            fast= self.calc(fast)
            slow= self.calc(slow)
        return True if fast ==1 else False


    def calc(self, n):
        output=0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output
