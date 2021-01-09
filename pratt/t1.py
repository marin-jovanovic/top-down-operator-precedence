class Node:

    def __init__(self, value, id):
        self.children = list()
        self.value = value
        self.id = id

    def __str__(self):
        return str(self.id) + " : " + str(self.value)

class Tree:

    def __init__(self, head_value):
        # global max_id
        self.max_id = 0

        self.head = Node(head_value, self.max_id)
        self.max_id += 1

    def add(self, parent_index, value):
        # global max_id

        # print(self.max_id)

        if parent_index == 0:
            self.head.children.append(Node(value, self.max_id))

        else:

            print("Iteriraj po elems")


        self.max_id += 1




        pass


    def print_tree(self, current):
        if current == "head":
            current = self.head

        print(current.value)

        for i in current.children:
            print(i)
            self.print_tree(i)


        pass



if __name__ == '__main__':

    tree = Tree("program") # 0

    tree.add(0, "naredba") # 1
    tree.add(0, "naredba") # 2
    tree.add(1, "int x")
    tree.add(1, "=")
    tree.add(1, "5")

    tree.print_tree("head")