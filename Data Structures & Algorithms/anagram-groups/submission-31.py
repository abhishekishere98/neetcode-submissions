class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        toup = {}
        # for i in strs:
        #     if ("".join(sorted(i))) in toup:
        #         toup[("".join(sorted(i)))].append(i)
        #     else:
        #         toup[("".join(sorted(i)))] = [i]
        # return list(toup.values())
        for word in strs:
            arr = [0]*26
            for char in word:
                index = ord(char) - ord('a')
                arr[index] += 1
            key = tuple(arr)
            if key in toup:
                toup[key].append(word)
            else:
                toup[key] = [word]
        return list(toup.values())