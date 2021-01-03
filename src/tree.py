
def remove_parenthesis(edges):
  edges_list = []
  for index in range(len(edges)):
    edge = []
    for char in edges[index]:
      if char != '(' or char != ')':
        edge.append(char)
    edges_list.append(edge)
  return edges_list

def get_children(value, edges_list):
  edges_list = list(remove_parenthesis(edges_list))
  edges = []
  for index in range(len(edges_list)):
    if edges_list[index][0] == value:
      edges.append(edges_list[index][1])
  return(edges)

def get_parents(value, edges): 
  edges_list = list(remove_parenthesis(edges))
  edges = []
  for index in range(len(edges_list)):
    if edges_list[index][1] == value:
      edges.append(edges_list[index][0])
  return(edges)

def get_root(edges):
  edges_list = list(remove_parenthesis(edges))
  parents = []
  for index in range(len(edges_list)):
    parents.append(edges_list[index][0])
  for char in parents:
    if get_parents(char, edges) == []:
      return char

class Node():
  def __init__(self, value):
    self.value = value
    self.children = next

class Tree():

  def __init__(self, edges):
    self.edges = edges
    self.root = Node(get_root(self.edges))

  def  build_from_edges(self):
    node_array = [self.root]
    
    while len(node_array) > 0:
      children_array = []
      for parent in node_array:
        parent.children = get_children(parent.value, self.edges)
        for index in range(len(parent.children)):
          parent.children[index] = Node(parent.children[index])
          children_array.append(parent.children[index])
      node_array = children_array


edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('g','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('c','k')]
tree = Tree(edges)
tree.build_from_edges()

assert tree.root.value == 'e'

assert [node.value for node in tree.root.children] == ['g', 'i', 'a']


assert [node.value for node in tree.root.children[0].children] == ['b']


assert [node.value for node in tree.root.children[1].children] == []

assert [node.value for node in tree.root.children[2].children] == ['c', 'd']

assert [node.value for node in tree.root.children[2].children[0].children] == ['k']

assert [node.value for node in tree.root.children[2].children[1].children] == ['f', 'j']

assert [node.value for node in tree.root.children[0].children[0].children] == []

assert [node.value for node in tree.root.children[2].children[0].children[0].children] == []

assert [node.value for node in tree.root.children[2].children[1].children[1].children] == []

assert [node.value for node in tree.root.children[2].children[1].children[0].children] == ['h']

assert [node.value for node in tree.root.children[2].children[1].children[0].children[0].children] == []
