class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
          return False

        sdict = {}
        tdict = {}

        for i in range(len(s)):
          if s[i] not in sdict:
            sdict[s[i]] = set()
          sdict[s[i]].add(t[i])

          if t[i] not in tdict:
            tdict[t[i]] = set()
          tdict[t[i]].add(s[i])

        s_keys = []
        t_keys = []

        for key, values in sdict.items():
          s_keys.append(key)
        
        for key, values in tdict.items():
          t_keys.extend(values)
        
        if s_keys == t_keys:
          return True
        else:
          return False


 
