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


    def insert(self, word):
        cur_node = self.head
        for c in f"{word}$":
            if c not in cur_node.children.keys():
                cur_node.children[c] = Node(c)
            
            cur_node = cur_node.children[c]

    
    def _get_word_node_branch(self, word):
        if len(word) == 0:
            char = "$"
        else:
            char = word[0]
        
        char_node = Node(char)
        
        if len(word) > 0:
            next_char_node = self.get_word_node_branch(word[1:])
            char_node.children[next_char_node.value] = next_char_node
        
        return char_node


    def search(self, word):
        cur_node = self.head
        return self._search_full(cur_node, word, "")


    def _search_full(self, cur_node: Node, word, traversed_word):
        if len(word) == 0:
            return self._get_prefix_words(cur_node, traversed_word)
       
        else:
            if word[0] in cur_node.children.keys():
                chosen_child = cur_node.children[word[0]]
                traversed_word += word[0]
                matching_words = self._search_full(chosen_child, word[1:], traversed_word)
                return matching_words
            else:
                return []


    def _get_prefix_words(self, cur_node: Node, traversed_word):
        words_found = []
        if len(cur_node.children) > 0:
                for child in cur_node.children.values():
                    traversed_word += child.value
                    words_found += self._get_prefix_words(child, traversed_word)
                return words_found
        else:
            if cur_node.value == "$":
                return [traversed_word[:-1]]
            else:
                return [None]

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
