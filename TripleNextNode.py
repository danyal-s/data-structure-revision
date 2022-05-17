class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.triple_next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            
            new_node.next = self.head
            self.head = new_node
            
            if self.has_triple(new_node):
                new_node.triple_next = new_node.next.next.next


    def has_triple(self, node):
        is_triple = True
        for _ in range(0, 3):
            if node.next is None:
                is_triple = False
                break
            node = node.next

        return is_triple


    def delete(self, idx):
        if idx == 0:
            self.head = self.head.next
            return
        else:
            cur_node = self.head
            nodes_to_modify = []
            for i in range(0, idx):
                if i >= idx - 3 and i != idx:
                    nodes_to_modify.append(cur_node)
                
                cur_node = cur_node.next
            
            nodes_to_modify[-1].next = nodes_to_modify[-1].next.next

            for x in list(reversed(nodes_to_modify))[1:]:
                x.triple_next = x.next.next.next if self.has_triple(x) else None
        
    
    def __iter__(self):
        self.cur_node = None
        return self
    

    def __next__(self):
        if self.cur_node is None:
            self.cur_node = self.head
            return self.cur_node
        else:
            if self.cur_node.next is None:
                raise StopIteration
            else:
                self.cur_node = self.cur_node.next
                return self.cur_node


    def __str__(self):
        return ",".join(str(x.value) for x in self)
            


def test():
    l = LinkedList()
    l.prepend(0)
    l.prepend(1)
    l.prepend(2)
    l.prepend(3)
    l.prepend(4)
    l.prepend(5)
    l.prepend(6)
    l.prepend(7)
    l.prepend(8)
                

    print(l)

    print("Delete 0:")
    l.delete(0)
    print(l)

    print("Delete 1:")
    l.delete(1)
    print(l)

    print("Delete 2:")
    l.delete(2)
    print(l)

    print("Delete 3:")
    l.delete(3)
    print(l)

    print("Delete 4:")
    l.delete(4)
    print(l)


def main():
    test()

if __name__ == "__main__":
    main()
