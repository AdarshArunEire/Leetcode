class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        t1count = t.count("1")
        max_t = []
        for i in range(len(t)):
            if s[i] == "0" and t1count > 0:
                max_t.append("1")
                t1count -= 1
                #print("1 Placed! Done in first for loop")

            else:
                max_t.append("0")
        #print(max_t)
        for i in range(len(max_t)):
            if t1count > 0 and max_t[-(i+1)] == "0":
                max_t[-(i+1)] = "1"
                t1count -= 1
                #print("1 Placed! Done in second for loop")

        ans = ""
        #print(s, max_t)
        for i in range(len(s)):
            if (s[i] == "1" or max_t[i] == "1") and not(s[i] == "1" and max_t[i] == "1"):
                ans += "1"
            else:
                ans += "0"
        return ans

#sol = Solution()
#s = "0110"
#t = "1110"
#print(sol.maximumXor(s, t))
