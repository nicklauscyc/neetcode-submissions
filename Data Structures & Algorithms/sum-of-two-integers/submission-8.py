class Solution:
    # python negative numbers have an infinite number of leading 1s
    def getSum(self, a: int, b: int) -> int:
        # Iterate from LSB (Least Significant Bit)
        # to MSB (Most Significant Bit) and have a carry
        carry = 0
        res = 0
        neg = (a)
        print(bin(a), bin(b))
        a = a & 0xFFFFFFFF
        b = b & 0xFFFFFFFF

        for i in range(32):
            mask = 1 << i
            carry <<= 1
            ai = a & mask
            bi = b & mask
            res = res | (ai ^ bi ^ carry)
            #print(i, "ai", bin(ai), "bi", bin(bi), "carry", bin(carry), "res", res)
            carry = (ai & bi) | (ai & carry) | (bi & carry)
            
        if res & 0x80000000: # if negative
            return res | ~0xFFFFFFFF
        return res

