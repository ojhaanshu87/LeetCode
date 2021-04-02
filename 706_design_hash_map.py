'''
Design a HashMap without using any built-in hash table libraries.
Implement the MyHashMap class:
MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

Example 1:
Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
'''

# There are two main issues that we should tackle, in order to design an efficient hashmap data structure:
    # 1). HASH FUNCTION DESIGN -> the purpose of hash function is to map a key value to an address in the storage space, similarly to the system that we assign a
                                  # postcode to each mail address. As one can image, for a good hash function,
                                  # it should map different keys evenly across the storage space, so that we don't end up with the case that the majority of the 
                                  # keys are concentrated in a few spaces. 
      
    # 2). COLLISION HANDLLING -> essentially the hash function reduces the vast key space into a limited address space. 
                                 # As a result, there could be the case where two different keys are mapped to the same address, which is what we call 'collision'. 
                                 # Since the collision is inevitable, it is important that we have a strategy to handle the collision.

# MODULO + ARRAY METHOD ------>>>>  O(N/K) TC and O(K + M) Space where N number of possible key, K is predefined bucket i.e. 2069. M is number of unique key

class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break

        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]
                
class MyHashMap(object):
    def __init__(self):
        # better to be a prime number, less collision
        self.key_space = 2069
        self.hash_table = [Bucket() for i in range(self.key_space)]

    def put(self, key, value):
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key, value)
        

    def get(self, key):
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)
        

    def remove(self, key):
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
