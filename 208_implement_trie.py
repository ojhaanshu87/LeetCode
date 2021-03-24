'''
Trie (we pronounce "try") or prefix tree is a tree data structure used to retrieve a key in a strings dataset. There are various applications of this very efficient data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() initializes the trie object.
void insert(String word) inserts the string word to the trie.
boolean search(String word) returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
'''

class Trie(object):

    def __init__(self):
        Trie = lambda : defaultdict(Trie)
        self.trie = Trie()
        self.END_OF_WORD_INDICATOR = '#'
        
    def insert(self, word):
        t = self.trie
        for c in word:
            t = t[c]
        t[self.END_OF_WORD_INDICATOR] = word
        

    def search(self, word):
        t = self.trie
        for c in word:
            if c not in t:
                return False
            else:
                t = t[c]
        return self.END_OF_WORD_INDICATOR in t
        

    def startsWith(self, prefix):
        t = self.trie
        for c in prefix:
            if c not in t:
                return False
            else:
                t = t[c]
        return bool(t)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
