class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def helper(s, n):
            
            if n <= 0:
                return s

            s_rev = s[::-1]
            s_inverted = ''

            for x in s_rev:
                if x == '0':
                    s_inverted += '1'
                else:
                    s_inverted += '0'
            # print(s_inverted)
            return helper(s + "1" + s_inverted, n -1 )
        
        sn = helper("0", n)

        return sn[k-1]

