class Solution:
    def scoreDifference(self, nums: list[int]) -> int:
        p1active = True
        p1 = 0
        p2 = 0
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                p1active = not p1active
                print(f"Switched! due to odd points on game {i + 1}")
            if (i + 1) % 6 == 0 and i != 0:
                p1active = not p1active
                print(f"Switched! due to every 6th game rule on game {i+1}")
            if p1active:
                p1 += nums[i]
            else:
                p2 += nums[i]
            print(
                f"game{i + 1}, points{nums[i]},"
                f" p1active{p1active}, p1, p2 points{p1, p2}")
        return p1 - p2

sol = Solution()
nums = [57,47,98,35,14,17,12,24,56,58,72,72,
        66,53,14,4,12,46,71,12,77,77,42,50,2,
        38,53,50,100,11,93,72,32,74,67,22,88,
        49,22,18,35,39,35,64,19,9,22,56,36]
print(sol.scoreDifference(nums))