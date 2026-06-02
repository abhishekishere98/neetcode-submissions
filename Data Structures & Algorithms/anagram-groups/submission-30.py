class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        toup = {}
        for i in strs:
            if ("".join(sorted(i))) in toup:
                toup[("".join(sorted(i)))].append(i)
            else:
                toup[("".join(sorted(i)))] = [i]
        return list(toup.values())