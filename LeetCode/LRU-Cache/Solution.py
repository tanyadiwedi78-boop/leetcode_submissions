1class Node:
2    def __init__(self , key , value):
3        self.key = key
4        self.value = value
5        self.prev= None
6        self.next = None
7
8class LRUCache:
9
10    def __init__(self, capacity: int):
11        self.capacity = capacity
12
13        # Hashmap : key-> Node
14        self.cache = {}
15
16        # Dummy Nodes
17        self.left = Node(0, 0) # LRU side
18        self.right = Node(0 , 0) # MRU side
19
20        self.left.next = self.right
21        self.right.prev = self.left
22
23    # Remove node from linked list
24    def remove(self , node):
25        prev_node = node.prev
26        next_node = node.next
27
28        prev_node.next = next_node
29        next_node.prev = prev_node
30
31    # Insert node at MRU
32    def insert(self , node):
33        prev_node = self.right.prev
34        next_node = self.right
35
36        prev_node.next = node
37        node.prev = prev_node
38
39        node.next = next_node
40        next_node.prev = node
41
42
43
44
45        
46
47
48
49
50        
51
52    def get(self, key: int) -> int:
53        # key does't exists
54        if key not in self.cache:
55            return -1
56        node = self.cache[key]
57        # this key was recently used
58        self.remove(node)
59        self.insert(node)
60        return node.value
61        
62
63    def put(self, key: int, value: int) -> None:
64        # if key exists in cache
65        if key in self.cache:
66            node = self.cache[key]
67            # remove old node
68            self.remove(node)
69            # create new node
70        node = Node(key , value)
71        # store in hashmap
72        self.cache[key] = node
73
74        #New recently used key becomes MRU
75        self.insert(node)
76        # cache exceede capacity
77        if len(self.cache) > self.capacity:
78            lru_node = self.left.next
79
80            # Remove linked list
81            self.remove(lru_node)
82            # Remove from hashmap
83            del self.cache[lru_node.key]
84        
85
86
87# Your LRUCache object will be instantiated and called as such:
88# obj = LRUCache(capacity)
89# param_1 = obj.get(key)
90# obj.put(key,value)