'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_substring_list = []
        def FirstLongestSubstring(s):
            #print("s intputted into func is", s)
            substring = []
            for i in range(len(s)):
                if s[i] not in substring:
                    substring.append(s[i])
                else:
                    #print("appending substring as similar character occured", substring)
                    len_substring_list.append(len(substring))
                    cut_s = s[s.index(s[i]) + 1 :]
                    #print(cut_s)
                    substring = []
                    FirstLongestSubstring(cut_s)
                    break # Without this we don't even make min time...
            #print("catch leftover append", substring)
            len_substring_list.append(len(substring))
            substring = []
        FirstLongestSubstring(s)
        if len_substring_list:
            return max(len_substring_list)
        else:
            return 0
# this is worst 5% speeds of all solutions that pass...... let me try again
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l_idx = 0
        max_len = 0

        for r_idx in range(len(s)):
            char = s[r_idx]

            if (char in seen) and (seen[char] >= l_idx):
                l_idx = seen[char] + 1

            seen[char] = r_idx
            max_len = max(max_len, r_idx + 1 - l_idx)
        return max_len