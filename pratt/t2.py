class Node

    def __init__(self, data, id):
        self.data = data
        self.children = list()
        self.id = id

    def __str__(self):
        return str(self.data)

    def get_id(self):
        return self.id

class Tree:
    """
    Class tree will provide a tree as well as utility functions.
    """

    # max_id = 0

    def __init__(self, data):
        global max_id
        self.max_id = 0
        self.head = Node(data)

    # @staticmethod
    def insert(self, node, data):
        """
        Insert function will insert a node into tree.
        Duplicate keys are not allowed.
        """
        #if tree is empty , return a root node
        # if node is None:
        #     return Node(data)
        #
        #
        # else:
        node.children.append(Node(data, self.max_id))
        self.max_id += 1

        #
        # # if data is smaller than parent , insert it into left side
        # if data < node.data:
        #     node.left = self.insert(node.left, data)
        # elif data > node.data:
        #     node.right = self.insert(node.right, data)

        return node

    def traverseInorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            # depth += 1
            print(root)

            # for i in root.children:
            #     print(i.data)
            # print()

            for i in root.children:

                self.traverseInorder(i)

            # self.traverseInorder(root.left, depth)
            # print(depth * " " + str(root.data))
            # print(root.data)
            # self.traverseInorder(root.right, depth)
        else:
            print(root.data)

        # depth -= 1

    def __str__(self):
        return "todo"




if __name__ == "__main__":
    # root = N("prog")
    # tree = Tree()
    # root = tree.insert(root, 10)

    tree = Tree("program")
    root = tree.insert(Node("program"), 10)

    tree.insert(root, 20)
    tree.insert(root, 30)
    tree.insert(root, 40)
    tree.insert(root, 70)
    tree.insert(root, 60)
    tree.insert(root, 80)



    tree.traverseInorder(root)

    # head = Node("program", None)
    # instruction_1 = Node("instruction", head)
    # instruction_2 = Node("instruction", head)
    # instruction_3 = Node("instruction", head)
    #
    # print(head)
