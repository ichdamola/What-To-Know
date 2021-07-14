
  
# write pls
  
# BFS or DFS algorithm to solve this problem
# I think you should use a stack or a queue for tranversing the tree.
# If you need more help, just type it out here, ok? - ok
# below is the test for the example, you can use it to test your code. right!
# How many years of experience do you have? 
# Which company that you are trying?
# If you use BFS, you should use queue instead of a stack!!!

  
def get_cheapest_cost(rootNode):
  
  result = float("inf")
  stack = []
  stack.append((rootNode, rootNode.cost))
  seen = set()
  seen.add(rootNode)
  
  while stack:
    current_node, path_sum = stack.pop()
    if len(current_node.children) == 0:
      if path_sum < result:
        result = path_sum
    else:
      for child in current_node.children:
        if child not in seen and path_sum + child.cost <= result:
          stack.append((child, path_sum + child.cost))
          seen.add(child)
  return result

########################################## 
# Use the helper code below to implement #
# and test your function above           #
##########################################
  
  
# A node 
class Node:

  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None
 

if __name__ == '__main__':
  root = Node(0)
  
  one = Node(5)
  two = Node(3)
  three = Node(6)
  
  four = Node(0)
  five = Node(2)
  six = Node(0)
  seven = Node(1)
  eight = Node(0)
  
  nine = Node(1)
  ten = Node(10)
  eleven = Node(1)
  
  
  
  root.children.extend([one, two, three])
  one.children.append(four)
  two.children.extend([five, six])
  three.children.extend([seven, eight])
  
  five.children.append(nine)
  six.children.append(ten)
  
  nine.children.append(eleven)
  
  print(get_cheapest_cost(root))