'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        t = ''
        n = len(s)
        k = 0
        if n <= numRows or numRows == 1:
            return s
        while k < n:
            t = t + s[k]
            k = k + (2 * numRows - 2)
        for i in range(1, numRows - 1):
            k = i
            p = 1
            while k < n:
                t = t + s[k]
                if p == 1:
                    k = k + (2 * numRows - 2 - 2 * i)
                    p = 0
                else:
                    k = k + 2 * i
                    p = 1
        k = numRows - 1
        while k < n:
            t = t + s[k]
            k = k + (2 * numRows - 2)
        return t
A = Solution()
print(A.convert('PAYPALISHIRING', 3))
print(A.convert('PAYPALISHIRING', 4))