from math import factorial as f


def permute(s):
    if len(s) == 1:
        return [s]

    if s == "1000000000":
        return s

    result = []
    for i in range(len(s)):
        rest = s[:i] + s[i + 1:]
        for p in permute(rest):
            #if (s[i] + p)[0] != "0":
            result.append(s[i] + p)
    return result

class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        ans = 0
        strn = str(n)
        for i in strn:
            #print(i)
            ans += f(int(i))
        #for p in permute(str(ans)):
            #if p == strn:
                #return True
        if sorted(str(ans)) == sorted(strn):
            return True
        else:
            return False


#sol = Solution()
#n = 100000000
#print(sol.isDigitorialPermutation(n))
#l = []
#for i in range(len(str(n))):
 #   l.append("")
#print(permute(str(n)))

#str = "Hello World!"
#for i in range(len(str)):
  #  rest = str[:i] + str[i + 1:]
  #  print(str[i], rest)
