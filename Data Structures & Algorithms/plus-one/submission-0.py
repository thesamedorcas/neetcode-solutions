class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()

        i=0
        digits[i]+=1
        while i<len(digits):
            curr= digits[i]

            if curr> 9:
                curr= curr%10
                if i+1<len(digits):
                    digits[i+1]+=1
                else:
                    digits.append(1)
                digits[i]= curr
                i+=1
            else:
                i+=1
                continue
            
        digits.reverse()
        return digits
        