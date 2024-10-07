class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map={}
        lst=s.split()
        if len(lst)!=len(pattern):
            return False
        for i in range (len(lst)):
            if pattern[i] not in map:
                if lst[i] not in map.values():
                    map[pattern[i]]=lst[i]
                else:
                    return False
            elif map[pattern[i]] != lst[i]:
                return False
        return True