from family_tree import Node, Tree

members = [
    Node('A', None, None),
    Node('B', 'A', None),
    Node('C', 'A', None),
    Node('D', 'A', None),
    Node('E', 'D', None),
    Node('F', 'D', None),
    Node('G', 'E', None),
    Node('H', 'E', None),
    Node('K', 'F', None),
    Node('L', 'F', None),
    Node('M', 'L', None),
    Node('N', 'L', None),
    Node('Ñ', 'N', None),
    Node('O', 'N', None),
    Node('a', 'B', None),
    Node('b', 'B', None),
    Node('c', 'B', None),
    Node('d', 'a', None),
    Node('f', 'a', None),
    Node('g', 'f', None),
    Node('h', 'f', None),
]
tree = Tree(members)
tree.generate_tree()

input1 = input('insert member 1 name: ')
input2 = input('insert member 2 name: ')
member1 = members[1]
member2 = members[9]

for i in members:
    if input1 == i.name:
        member1 = i
    if input2 == i.name:
        member2 = i

print(f'generation of {member1.name}: {member1.generation}')
print(f'generation of {member2.name}: {member2.generation}')
print(tree.find_queue(member1, member2))
print(tree.get_relationship(member1, member2))