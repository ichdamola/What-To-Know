"""
Bracket Match
A string of brackets is considered correctly matched if every opening bracket in the string can be paired up with a later closing bracket, and vice versa. For instance, “(())()” is correctly matched, whereas “)(“ and “((” aren’t. For instance, “((” could become correctly matched by adding two closing brackets at the end, so you’d return 2.

Given a string that consists of brackets, write a function bracketMatch that takes a bracket string as an input and returns the minimum number of brackets you’d need to add to the input in order to make it correctly matched.

Explain the correctness of your code, and analyze its time and space complexities.
"""

def bracket_match(text):
  res = 0
  deficitChar = 0
  
  for ch in text:
    if ch == '(':
        deficitChar += 1
    elif ch == ')':
        deficitChar -= 1
    if deficitChar < 0:
        deficitChar += 1
        res += 1
  return res + deficitChar 

if __name__ == '__main__':
    assert bracket_match('())(') == 2, "Test case failed!"