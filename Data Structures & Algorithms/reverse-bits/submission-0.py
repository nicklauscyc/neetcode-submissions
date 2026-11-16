class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []

        m = n
        count = 0
        while m > 0 or count < 32:
            bits.append(m & 1)
            m >>= 1
            count += 1
        
        #print('{:032b}'.format(n))
        #print(''.join(map(str,bits)))

        res = 0
        for i in range(len(bits)):
            j = len(bits) - 1 - i 
            res += (bits[j] << i)
            #print(bin(res))
        
        return res



        