
# 👨‍👩‍👧‍👦 Family Tree Relationship Finder

This Python program allows users to input a family tree structure and determine the relationship between any two members. It supports handling direct family (parents, siblings, children) and extended family (cousins, removed cousins, great-grandchildren, etc.), with generational awareness built into the algorithm.

---

## 📜 Features

- Build a tree structure of family members
- Determine generation number of each member
- Calculate the degree of separation between any two members
- Classify relationships such as:
  - Siblings
  - Cousins (including nth cousins, removed)
  - Aunts/Uncles and Nieces/Nephews
  - Grandchildren and Great-Grandchildren

---

## 📦 File Structure

```
family-tree/
│
├── main.py                 # User input and interface logic
├── family_tree.py          # Node and Tree classes with all core logic
├── README.md               # This documentation
```

---

## 🧠 Design Explanation

The core design involves two primary data structures:

1. **Node** – Represents each family member with a name, a reference to the parent (converted to a Node object), a list of children (`kids`), and their generation number (root is generation 0).

2. **Tree** – Contains all nodes and functions to:
   - Build the tree (`generate_tree`)
   - Find how far apart two members are in the tree (`find_queue`)
   - Determine the relationship type based on generation and separation (`get_relationship`)

The relationships are derived by comparing both the *distance to a common ancestor* and *relative generations*.

---

## 🔍 Pseudocode

### `generate_tree()`

```
for each member in members:
    for each potential parent in members:
        if parent.name == member.parent:
            parent.kids.append(member)
            member.parent = parent

    node = member
    while node.parent is not None:
        member.generation += 1
        node = node.parent
```

### `find_queue(member1, member2)`

```
if member1 == member2:
    return (0, 0)

equalize generations:
    move up the tree from the lower generation node until both are at same level

move both nodes up until they meet (common ancestor)
    count steps taken from both sides

return (steps_from_member1, steps_from_member2)
```

### `get_relationship(member1, member2)`

```
call find_queue() to get (steps1, steps2)

if both steps < 3:
    if same steps:
        return 'sibling'
    elif difference is 1 and one is close to root:
        return 'nephew/niece'
    elif one is root and other is 2–4:
        return 'child' / 'grandchild' / 'great grandchild'
    elif one is 2 and other is 4:
        return 'grand nephew or niece'
elif both steps ≥ 3:
    if same steps:
        return 'nth cousin'
    else:
        return 'nth cousin x removed'
```

---

## 📈 Runtime Complexity (Big-O)

- `generate_tree`: O(n) in the worst case
- `find_queue`: O(h), where h is the tree height (log(n) for balanced tree, but linear for unbalanced)

    In tree terminology:

    The height of a tree (h) is defined as the number of edges on the longest path from the root node to a leaf.

    The depth or generation of a node is the number of edges from the root to that node.

    For your example:
    ```
      A
     / \
    B   C
    ```
    A is the root (depth 0)

    B and C are direct children (depth 1)

    ✅ So the height of the tree is 1 — because the longest path from root (A) to any leaf (B or C) has 1 edge.

    So talking relatively to the number of members, it would be similar to log(n) in the worst case, unless it is a linear tree, everybody is a child of the member before. For that case the algorithm would be `O(n) = O(h)` but that is not a really relaistic case and even though I've been trying to find and algorithm with a better performance in this case, for me it is been impossible.



- `get_relationship`: O(h), uses `find_queue`

**Overall complexity: Better than loglinear in every case, if not faster**

---


## ⚖️ Design Trade-offs

| Design Choice                             | Memory Impact             | Pros                                                                 | Cons                                                                 |
|------------------------------------------|----------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| ✅ Using a `name → Node` map              | Extra O(n) space           | Reduces `generate_tree()` from O(n²) to O(n). Fast parent linking.   | Slightly more memory used to store the map.                         |
| ✅ Replacing string parents with Node refs| Minimal (object references) | Enables fast upward traversal and accurate generation calculation.   | Requires mutation of original data; must manage references carefully. |
| ✅ Storing `generation` in each Node      | O(n) (1 int per node)      | Simplifies relationship logic and improves readability/performance. | Slightly more memory used (negligible).                            |
| ✅ Recursive traversal using `parent`     | No extra space             | Elegant and efficient for small to medium-depth trees.               | Stack overflow risk in deeply nested trees (though rare in real cases). |
| ❌ No caching of relationship results     | Lower memory usage         | Keeps implementation simple and memory-efficient.                    | Recalculates relationships on every query (can be slow if repeated). |
| ❌ No bi-directional links (no child-to-parent and vice versa mapping)| Saves memory               | Keeps model simple.                                                  | Makes some complex queries slower (e.g., all ancestors or descendants). |
| ✅ Relationship logic based on queue depth| No additional memory       | Easy to understand and extend; handles cousin removals cleanly.      | Limited to bloodline-only relationships; doesn't support marriages, etc. |


---

## 💡 Future Improvements

- ✅ Use a dictionary to map names to nodes → reduce `generate_tree` to O(n)
- 🔁 Add support for relationships via marriage (e.g. in-laws)
- 📊 Visualize the family tree using `graphviz` or a similar library
- 🌐 Create a web interface using Flask or React
- 🧪 Add unit tests for edge cases (same person, distant cousins, etc.)
- 📝 Support loading family data from JSON or CSV instead of hardcoding

---

## 🧪 Example Output

```
insert member 1 name: a
insert member 2 name: g

generation of a: 2
generation of g: 4
(3, 1)
nephew/niece
```

---

## 📜 License

This project is open-source under the MIT License.
