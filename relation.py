from family_tree import Node, Tree
#from number_parser import parse_ordinal

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

#My parent’s sibling’s child
#is my cousin
relation_dict = {
    'great grandparent' : 3,
    'grandparent' : (2, 0),
    'parent' : (1, 0),
    'uncle' : (1, 0),
    'sibling' : (1, 1), 
    'cousin' : (2, 2),
    'nephew' : (2, 3),
    'child' : (0, 1),
    'nothing': (0, 0),
    'grandchild' : -2
}
long_input = input("enter relation: ").lower().split()
print("Original input tokens:", long_input)

owns = []
relation = ""

for word in long_input:
    if word.endswith("'s"):
        owns.append(word[:-2])
    elif word != "my":
        relation = word

filtered_owns = []
for i in range(len(owns)):
    if i > 0 and owns[i] == "sibling" and owns[i - 1] == "sibling":
        continue
    filtered_owns.append(owns[i])

owns = filtered_owns

i = 0
while i < len(owns):
    if i > 0:
        if owns[i] == "sibling" and owns[i - 1] == "cousin":
            owns.pop(i)
            continue
        if owns[i] == "cousin" and owns[i - 1] == "sibling":
            owns.pop(i - 1)
            i -= 1
            continue

    if owns[i] == "cousin" and relation == "sibling":
        relation = "cousin"
        owns.pop(i)
        continue
    if owns[i] == "sibling" and relation == "cousin":
        owns.pop(i)
        continue
    if owns[i] == "sibling" and relation == "sibling":
        owns.pop(i)
        continue
    i += 1

if owns[0] == 'sibling' and len(owns) == 1:
    owns[0] = 'nothing'

print("Final owns list:", owns)
print("Final relation:", relation)


owner_relation = 1
member_relation = 1

for owner in owns:
    owner_relation += relation_dict[owner][0]
    member_relation += relation_dict[owner][1]

if relation == 'parent':
    owner_relation += relation_dict[relation][0] - 1
    member_relation += relation_dict[relation][1] - 1
else:
    owner_relation += relation_dict[relation][0]
    member_relation += relation_dict[relation][1]



print(owner_relation)
print(member_relation)

print(owns)
print(relation)
print(f'relation: {tree.get_relationship2((owner_relation, member_relation))}')





'''
for i in members:
    if input1 == i.name:
        member1 = i
    if input2 == i.name:
        member2 = i
'''

'''print(f'generation of {member1.name}: {member1.generation}')
print(f'generation of {member2.name}: {member2.generation}')
print(tree.find_queue(member1, member2))
print(tree.get_relationship(member1, member2))'''