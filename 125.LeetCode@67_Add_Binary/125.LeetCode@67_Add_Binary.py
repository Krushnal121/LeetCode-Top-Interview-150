class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0

        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum += int(a[i])
                i -= 1
            if j >= 0:
                sum += int(b[j])
                j -= 1
            carry = 1 if sum > 1 else 0
            res.append(str(sum % 2))

        if carry:
            res.append('1')

        return ''.join(res[::-1])
