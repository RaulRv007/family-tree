class Node():
    def __init__(self, name, parent, kids):
        self.parent = parent
        self.kids = []
        self.name = name
        self.generation = 0

class Tree():
    def __init__(self, members):
        self.members = members
    
    def generate_tree(self):
        for member in self.members:
            for parent in self.members:
                if parent.name == member.parent:
                    parent.kids.append(member)
                    member.parent = parent

            node = member
            while node.parent != None:
                member.generation += 1
                node = node.parent
                
    def find_relation(self, member1, member2):
        counter1 = 0
        counter2 = 0
        lower_gen = 0
        node = member1
        if member1.parent and member2.parent is not None:
            if member1.generation >= member2.generation:
                lower_gen = member2.generation - 1
            else:
                lower_gen = member1.generation - 1

            node = member1
            node2 = member2
            print(f'lower generation: {lower_gen}')
            
            while node.generation > lower_gen:
                counter1 += 1
                if node.parent is not None:
                    node = node.parent
                else:
                    break
            
            while node2.generation > lower_gen:
                counter2 += 1
                if node.parent is not None:
                    node2 = node2.parent
                else:
                    break
            return (counter1 + 1, counter2 + 1)
        
        else:
            if member1.parent == None:
                lower_gen = member1.generation
                counter1 = 1
            elif member2.parent == None:
                lower_gen = member2.generation
                counter2 = 1

            node = member1
            node2 = member2

            if counter1 == 1:
                while node2.generation > lower_gen:
                    counter2 += 1
                    if node.parent is not None:
                        node2 = node2.parent
                    else:
                        break
                return (counter1, counter2 + 1)
            else:
                while node.generation > lower_gen:
                    counter1 += 1
                    if node.parent is not None:
                        node = node.parent
                    else:
                        break
                return (counter1 + 1, counter2)
                

        
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
]
tree = Tree(members)
tree.generate_tree()
print(f'generation of O: {tree.members[-1].generation}')
print(f'generation of E: {tree.members[4].generation}')

print(tree.find_relation(members[4], members[-1]))
