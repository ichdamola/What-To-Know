def count_binary_substrings(s: str) -> int:
  sub = [1]
  xrange = range
  for i in xrange(1, len(s)):
    if s[i-1] != s[i]:
      sub.append(1)
    else:
      sub[-1] += 1
     
    res = 0
    for i in xrange(1, len(sub)):
      res += min(sub[i-1], sub[i])
  return res