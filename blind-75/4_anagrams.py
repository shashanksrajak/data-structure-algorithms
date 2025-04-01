class Solution:
    def groupAnagrams(self, strs):
        sorted_list = ["".join(sorted(str)) for str in strs]

        strs_map = {}

        for i in range(len(sorted_list)):
            str = sorted_list[i]
            if str in strs_map:
                strs_map[str].append(i)
            else:
                strs_map[str] = [i]

        output = []
        for key in strs_map:
            output.append([strs[i] for i in strs_map[key]])
        return output


# strs = ["act", "pots", "tops", "cat", "stop", "hat"]
strs = ["x"]

sol = Solution()
result = sol.groupAnagrams(strs)
print(result)
