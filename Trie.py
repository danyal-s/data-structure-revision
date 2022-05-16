# Goal: Implement a data structure that returns a list of words
# words that are added into it when a prefix is used to search
# in it.
class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node("*")
        self.output = []


    def insert(self, word):
        cur_node = self.head
        for c in f"{word}$":
            if c not in cur_node.children.keys():
                cur_node.children[c] = Node(c)
            
            cur_node = cur_node.children[c]


    def search(self, word):
        cur_node = self.head
        for c in word:
            if c in cur_node.children.keys():
                cur_node = cur_node.children[c]
            else:
                return []
        self.dfs(cur_node, word)
        return self.output


    def dfs(self, node, word):
        for child in node.children.values():
            self.dfs(child, word + child.value)
            if child.value == "$":
                self.output.append(word)


def test():
    t = Trie()        

    t.insert("hello")
    t.insert("hell")
    t.insert("helga")
    t.insert("halo")
    t.insert("abc")
    t.insert("abcc")
    t.insert("abcd")

    k = t.search("hel")
    print(k)


def main():
    test()


if __name__ == "__main__":
    main()
