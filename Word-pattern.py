class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
      string = s.split(" ")

      if len(string) != len(pattern):
        return False
      dict = {}
      for i in range(len(pattern)):
        if pattern[i] not in dict:
          dict[pattern[i]] = set()
        dict[pattern[i]].add(string[i])
      res = []
      for key, values in dict.items():
        if len(values) >1 :
          return False
        if values not in res:
          res.append(values)
      
      if len(res) == len(dict.keys()):
        return True
      else:
        return False