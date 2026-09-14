1class MyCircularQueue:
2
3    def __init__(self, k: int):
4        self.size = k
5        self.queue = [None] * k
6        self.front = -1
7        self.rear = -1
8        
9
10    def enQueue(self, value: int) -> bool:
11        """Insert an element into the circular queue. Return True if successful."""
12        if self.isFull():
13            return False
14        
15        # If inserting the very first element, set front to index 0
16        if self.isEmpty():
17            self.front = 0
18            
19        # Circularly increment the rear pointer
20        self.rear = (self.rear + 1) % self.size
21        self.queue[self.rear] = value
22        return True
23
24    def deQueue(self) -> bool:
25        """Delete an element from the circular queue. Return True if successful."""
26        if self.isEmpty():
27            return False
28        
29        # If there's only one element left, resetting the queue clears it
30        if self.front == self.rear:
31            self.front = -1
32            self.rear = -1
33        else:
34            # Circularly increment the front pointer
35            self.front = (self.front + 1) % self.size
36            
37        return True
38
39    def Front(self) -> int:
40        """Get the front item from the queue."""
41        if self.isEmpty():
42            return -1
43        return self.queue[self.front]
44
45    def Rear(self) -> int:
46        """Get the last item from the queue."""
47        if self.isEmpty():
48            return -1
49        return self.queue[self.rear]
50
51    def isEmpty(self) -> bool:
52        """Checks whether the circular queue is empty."""
53        return self.front == -1
54
55    def isFull(self) -> bool:
56        """Checks whether the circular queue is full."""
57        return (self.rear + 1) % self.size == self.front
58