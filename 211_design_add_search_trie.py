'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' 
where dots can be matched with any letter.

Example:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
'''
# TRIE SOLUTION TC O(M) where M is length of word, O(1) Space
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_leaf = False
        
class WordDictionary(object):
    def __init__(self):
		self.root = TrieNode()
        
    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_leaf = True
        
    def find(self, word, root):
        node = root
        for i, c in enumerate(word):
            if c == '.':
                for next_node in node.children.values():
                    if self.find(word[i + 1:], next_node):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                node = node.children[c]
                        
        return node.is_leaf
    
    
    def search(self, word):
        return self.find(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Hash map solution 

class WordDictionary(object):
    def __init__(self):
		self.h = collections.defaultdict(list)
        ##O(N)space
        ##O(1)time
    
    ##O(1) time and O(1) space
    def addWord(self, word):
        if word not in self.h[len(word)]:
            self.h[len(word)].append(word)
            
    #O(M)*O(N) time
    #O(1) Space
    def search(self, word):
        if not self.h[len(word)]:
            return False
        all_ix = [i for i,e in enumerate(word) if e!='.']
        if not all_ix:
            return True
        
        this_key = ''.join([word[i] for i in all_ix])
        tmp = set()
        for e in self.h[len(word)]:
            key = ''.join([e[i] for i in all_ix])
            tmp.add(key)
        
        if this_key in tmp:
            return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
