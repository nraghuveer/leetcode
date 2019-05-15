# https://leetcode.com/problems/fraction-to-recurring-decimal/

class Solution:
    def fractionToDecimal(self, num: int, den: int) -> str:
        if not num:
            return '0'
        if not den:
            return
        res = []
        if (num < 0) ^ (den < 0):
            res.append('-')
        num = abs(num)
        den = abs(den)
        res.append(str(num//den))
        rmd = num % den
        if not rmd:
            return ''.join(res)
        res.append('.')
        d = {}
        while rmd:
            if rmd in d:
                res.insert(d[rmd],'(')
                res.append(')')
                break

            d[rmd] = len(res)
            div, rmd = divmod(rmd*10, den)
            res.append(str(div))
        return ''.join(res)

if __name__ == "__main__":
    assert Solution().fractionToDecimal(2,3) == '0.(6)'
    assert Solution().fractionToDecimal(1,2) == '0.5'
    assert Solution().fractionToDecimal(4,333) == '0.(012)'
    assert Solution().fractionToDecimal(0,3) == '0'
    assert Solution().fractionToDecimal(1,6) == '0.1(6)'
    print('done')