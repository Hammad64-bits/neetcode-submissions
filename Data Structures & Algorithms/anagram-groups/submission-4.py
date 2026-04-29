class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        lookup = dict()

        for word in strs:

            cpy = list(word)
            cpy.sort()
            cpy = ''.join(cpy)

            if lookup.get(cpy) == None:
                lookup[cpy] = [word]

            else:
                lookup[cpy].append(word)
        
        return [*lookup.values()]