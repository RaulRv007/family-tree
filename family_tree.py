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
    
    def find_faster(self, member1, member2):
        if member1.generation == 0 or member2.generation == 0:
            lower_gen = min(member1.generation, member2.generation)
        else:
            counter = 0
            node1 = member1
            node2 = member2
            while node1.parent is not node2.parent:
                counter += 1
                if node1.parent is not None:
                    node1 = node1.parent
                    node2 = node2.parent
                else:
                    break
            counter += 1
            lower_gen = min(member1.generation, member2.generation) - counter

        return (member1.generation - lower_gen + 1, member2.generation - lower_gen + 1)
    
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
    
    def get_relationship2(self,value):

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

    
    
def find_mine(long_input):

    relation_dict = {
        'great-grandparent' : 3,
        'grandparent' : (2, 0),
        'parent' : (1, 0),
        'uncle' : (1, 0),
        'sibling' : (1, 1), 
        'cousin' : (2, 2),
        'nephew' : (1, 2),
        'child' : (0, 1),
        'nothing': (0, 0),
        'grandchild' : (0, 2)
    }
    owns = []
    relation = ""

    long_input = str(long_input).lower().split()

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
            if owns[i] == "sibling" and owns[i - 1] == "cousin"  and len(owns) >= 1:
                owns.pop(i)
                continue
            if owns[i] == "cousin" and owns[i - 1] == "sibling"  and len(owns) >= 1:
                owns.pop(i - 1)
                i -= 1
                continue

        if owns[i] == "cousin" and relation == "sibling"  and len(owns) >= 1:
            relation = "cousin"
            owns.pop(i)
            continue
        if owns[i] == "sibling" and relation == "cousin" and len(owns) >= 1:
            owns.pop(i)
            continue
        if owns[i] == "sibling" and relation == "sibling" and len(owns) >= 1:
            owns.pop(i)
            continue
        i += 1


    print("Final owns list:", owns)
    print("Final relation:", relation)

    if owns == []:
        return relation


    owner_relation = 1
    member_relation = 1

    for owner in owns:
        if owner not in relation_dict:
            print(f"Unknown relation: {owner}")
            continue
            '''if owner == 'child' or owner == 'grandchild':
            owner_relation += relation_dict[owner][1]
            member_relation += relation_dict[owner][0]'''
        else:
            owner_relation += relation_dict[owner][0]
            member_relation += relation_dict[owner][1]


    if relation == 'parent' and owns == []:
        owner_relation = max(0, owner_relation + relation_dict[relation][0] - 1)
        member_relation += relation_dict[relation][1] - 1
    if relation == 'child' and owns == []:
        owner_relation = max(0, owner_relation + relation_dict[relation][0] - 1)
        member_relation += relation_dict[relation][1] - 1
        
    else:
        owner_relation += relation_dict[relation][0]
        member_relation += relation_dict[relation][1]

    return 


def get_relationship2(value):

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
            