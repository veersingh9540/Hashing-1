class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0 or strs == None:
          return []
        dict = {}
        for astrs in strs:
          sorted_str = sorted(astrs)
          s = ''.join(sorted_str)
          if s not in dict:
            dict[s] = []
          dict[s].append(astrs)
        
        return dict.values()
