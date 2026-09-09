1class MyStack:
2
3    def __init__(self):
4        self.q = deque()
5        
6
7    def push(self, x: int) -> None:
8        self.q.append(x)
9
10        # move previous elements behind x
11        for _ in range(len(self.q) - 1):
12            self.q.append(self.q.popleft())
13    def pop(self):
14        if not self.q:
15            return -1
16        return self.q.popleft()
17
18    def top(self) -> int:
19        if not self.q:
20            return -1
21        return self.q[0]
22
23    def empty(self):
24        return len(self.q) == 0
25
26
27        
28
29    
30        
31
32
33# Your MyStack object will be instantiated and called as such:
34# obj = MyStack()
35# obj.push(x)
36# param_2 = obj.pop()
37# param_3 = obj.top()
38# param_4 = obj.empty()