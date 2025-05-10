import math
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
                
    def find_queue(self, member1, member2):
        node1 = member1
        node2 = member2
        counter = 0
        counter2 = 0
        if node1 == node2: return (0, 0)
        if node1.generation == node2.generation:
            while node1 != node2:
                counter += 1
                node1 = node1.parent
                node2 = node2.parent
            
            return (counter + 1, counter + 1)
        else:
            gen_diff = abs(member1.generation - member2.generation)
            if member1.generation > member2.generation:
                for i in range(gen_diff):
                    node1 = node1.parent
                    counter += 1
            else:
                for i in range(gen_diff):
                    node2 = node2.parent
                    counter2 += 1
            
            while node1 != node2:
                counter += 1
                counter2 += 1
                node1 = node1.parent
                node2 = node2.parent
            
            return (counter + 1, counter2 + 1)

        
    
    def ordinal(self, n: int):
        if 11 <= (n % 100) <= 13:
            suffix = 'th'
        else: 
            suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
        return str(n) + suffix
                
    def get_relationship(self, member1, member2):
        value = self.find_queue(member1, member2)
        if value[0] < 3 or value[1] < 3:
            if value[0] == value[1]:
                return f'sibling'
            elif abs(value[0] - value[1]) == 1 and min(value[0], value[1]) < 3:
                return f'nephew/niece'
            elif min(value[0], value[1]) == 1:
                if max(value[1], value[0]) == 2:
                    return f'child'
                elif max(value[1], value[0]) == 3:
                    return f'grandchild'
                elif max(value[1], value[0]) == 4 and min(value[1], value[0]) < 3:
                    return f'great grandchild'
                else:
                    return f'{self.ordinal(max(value[1], value[0]) - 3) } great grandchild'
            elif max(value[1], value[0]) == 4 and min(value[0], value[1]) < 3:
                return f'grand nephew or niece'

        elif value[0] >= 3 and value[1] >= 3:
            if value[0] == value[1]:
                return f'{self.ordinal(value[0] - 2)} cousin'
            else:
                return f'{self.ordinal(min(value[0], value[1]) - 2)} cousin {abs(value[0] - value[1])}x removed'

        elif value[0] == value[1]:
            return f'{self.ordinal(value[0] - 1)} cousin'
    
    def get_relationship_with_val(self,value):

        if value[0] <= value[1]:
            if value[0] < 3 or value[1] < 3:
                if min(value[0], value[1]) == 1:
                    if max(value[1], value[0]) == 2:
                        return f'child'
                    elif max(value[1], value[0]) == 3:
                        return f'grandchild'
                    elif max(value[1], value[0]) == 4 and min(value[1], value[0]) < 3:
                        return f'great grandchild'
                    else:
                        return f'{self.ordinal(max(value[1], value[0]) - 3) } great grandchild'
                elif value[0] == value[1]:
                    return f'sibling'
                elif abs(value[0] - value[1]) == 1 and min(value[0], value[1]) < 3:
                    return f'nephew/niece'
                elif max(value[1], value[0]) == 4 and min(value[0], value[1]) < 3:
                    return f'grand nephew or niece'

            elif value[0] >= 3 and value[1] >= 3:
                if value[0] == value[1]:
                    return f'{self.ordinal(value[0] - 2)} cousin'
                else:
                    return f'{self.ordinal(min(value[0], value[1]) - 2)} cousin {abs(value[0] - value[1])}x removed'

            elif value[0] == value[1]:
                return f'{self.ordinal(value[0] - 1)} cousin'
        else:
            if value[0] < 3 or value[1] < 3:
                if min(value[0], value[1]) == 1:
                    if max(value[1], value[0]) == 2:
                        return f'parent'
                    elif max(value[1], value[0]) == 3:
                        return f'grandparent'
                    elif max(value[1], value[0]) == 4 and min(value[1], value[0]) < 3:
                        return f'great grandparent'
                    else:
                        return f'{self.ordinal(max(value[1], value[0]) - 3) } great grandparent'
                elif value[0] == value[1]:
                    return f'sibling'
                elif abs(value[0] - value[1]) == 1 and min(value[0], value[1]) < 3:
                    return f'uncle'
                elif max(value[1], value[0]) == 4 and min(value[0], value[1]) < 3:
                    return f'grand uncle or aunt'

            elif value[0] >= 3 and value[1] >= 3:
                if value[0] == value[1]:
                    return f'{self.ordinal(value[0] - 2)} uncle'
                else:
                    return f'{self.ordinal(min(value[0], value[1]) - 2)} uncle {abs(value[0] - value[1])}x removed'

            elif value[0] == value[1]:
                return f'{self.ordinal(value[0] - 1)} uncle'


def get_relationship_with_val(value):

    if value[0] <= value[1]:
        if value[0] < 3 or value[1] < 3:
            if min(value[0], value[1]) == 1:
                if max(value[1], value[0]) == 2:
                    return f'child'
                elif max(value[1], value[0]) == 3:
                    return f'grandchild'
                elif max(value[1], value[0]) == 4 and min(value[1], value[0]) < 3:
                    return f'great grandchild'
                else:
                    return f'{ordinal(max(value[1], value[0]) - 3) } great grandchild'
            elif value[0] == value[1]:
                return f'sibling'
            elif abs(value[0] - value[1]) == 1 and min(value[0], value[1]) < 3:
                return f'nephew/niece'
            elif max(value[1], value[0]) == 4 and min(value[0], value[1]) < 3:
                return f'grand nephew or niece'

        elif value[0] >= 3 and value[1] >= 3:
            if value[0] == value[1]:
                return f'{ordinal(value[0] - 2)} cousin'
            else:
                return f'{ordinal(min(value[0], value[1]) - 2)} cousin {abs(value[0] - value[1])}x removed'

        elif value[0] == value[1]:
            return f'{ordinal(value[0] - 1)} cousin'
    else:
        if value[0] < 3 or value[1] < 3:
            if min(value[0], value[1]) == 1:
                if max(value[1], value[0]) == 2:
                    return f'parent'
                elif max(value[1], value[0]) == 3:
                    return f'grandparent'
                elif max(value[1], value[0]) == 4 and min(value[1], value[0]) < 3:
                    return f'great grandparent'
                else:
                    return f'{ordinal(max(value[1], value[0]) - 3) } great grandparent'
            elif value[0] == value[1]:
                return f'sibling'
            elif abs(value[0] - value[1]) == 1 and min(value[0], value[1]) < 3:
                return f'uncle'
            elif max(value[1], value[0]) == 4 and min(value[0], value[1]) < 3:
                return f'grand uncle or aunt'

        elif value[0] >= 3 and value[1] >= 3:
            if value[0] == value[1]:
                return f'{ordinal(value[0] - 2)} uncle'
            else:
                return f'{ordinal(min(value[0], value[1]) - 2)} uncle {abs(value[0] - value[1])}x removed'

        elif value[0] == value[1]:
            return f'{ordinal(value[0] - 1)} uncle'
        
def ordinal(self, n: int):
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else: 
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix
            