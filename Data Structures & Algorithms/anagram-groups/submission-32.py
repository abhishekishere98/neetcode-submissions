class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        toup = {}
        # for i in strs:
        #     if ("".join(sorted(i))) in toup:
        #         toup[("".join(sorted(i)))].append(i)
        #     else:
        #         toup[("".join(sorted(i)))] = [i]
        # return list(toup.values())
        # Iterate through the given string
        for word in strs:
            # Create an array of 26 0s 
            arr = [0]*26
            # Save the frequency of each character at required index starting at 0
            for char in word:
                index = ord(char) - ord('a')
                arr[index] += 1
            # convert each word char count as a key for creating a touple
            key = tuple(arr)
            # For every set of alphabet and frequency combination add words to touple
            if key in toup:
                toup[key].append(word)
            else:
                toup[key] = [word]
        # Return the final touple having words that have same alphabet and frequency combination
        return list(toup.values())