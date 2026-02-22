from math import factorial as f


def permute(s):
    if len(s) == 1:
        return [s]

    result = []
    finalresult = []
    for i in range(len(s)):
        rest = s[:i] + s[i + 1:]
        for p in permute(rest):
            result.append(s[i] + p)
    for i in range(len(result)):
        if result[i][0] != 0:
            finalresult.append(result[i])
    return finalresult

class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        ans = 0
        strn = str(n)
        for i in strn:
            print(i)
            ans += f(int(i))
        for p in permute(strn):
            if int(p) == ans:
                return True
        return False


sol = Solution()
n = 415
print(sol.isDigitorialPermutation(n))
l = []
#for i in range(len(str(n))):
 #   l.append("")
#print(permute(str(n)))

#str = "Hello World!"
#for i in range(len(str)):
  #  rest = str[:i] + str[i + 1:]
  #  print(str[i], rest)