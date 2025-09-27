def contains(tree, value):
    if not isinstance(tree, tuple):
        return tree == value

    pivot, left, right = tree

    if value < pivot:
        return contains(left, value)
    elif value > pivot:
        return contains(right, value)
    else:
        return value == pivot


my_tree = (
    10,
    (7, None, 9),
    (13, 11, None),
)


for i in range(0, 14):
    print(i, contains(my_tree, i))


assert contains(my_tree, 9)
assert not contains(my_tree, 14)


def contains_match(tree, value):
    match tree:
        case pivot, left, _ if value < pivot:
            return contains_match(left, value)
        case pivot, _, right if value > pivot:
            return contains_match(right, value)
        case (pivot, _, _) | pivot:
            return pivot == value


assert contains_match(my_tree, 9)
assert not contains_match(my_tree, 14)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


obj_tree = Node(
    value=10,
    left=Node(value=7, right=9),
    right=Node(value=13, left=11),
)


def contains_class(tree, value):
    if not isinstance(tree, Node):
        return tree == value
    elif value < tree.value:
        return contains_class(tree.left, value)
    elif value > tree.value:
        return contains_class(tree.right, value)
    else:
        return tree.value == value


assert contains_class(obj_tree, 9)
assert not contains_class(obj_tree, 14)


def contains_match_class(tree, value):
    match tree:
        case Node(value=pivot, left=left) if value < pivot:
            return contains_match_class(left, value)
        case Node(value=pivot, right=right) if value > pivot:
            return contains_match_class(right, value)
        case Node(value=pivot) | pivot:
            return pivot == value


assert contains_match_class(obj_tree, 9)
assert not contains_match_class(obj_tree, 14)
