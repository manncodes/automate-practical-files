# Implementations of Data structures in python
from dataclasses import dataclass


# Class implementation of a Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


@dataclass
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1
        return self

    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.length -= 1
            return
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.data == data:
                prev.next = curr.next
                self.length -= 1
                return
            prev = curr
            curr = curr.next
        return

    def search(self, data):
        if self.head is None:
            return
        curr = self.head
        while curr:
            if curr.data == data:
                return curr
            curr = curr.next
        return


# Class implementation of a Stack
@dataclass
class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, data):
        self.stack.add(data)

    def pop(self):
        self.stack.remove(self.stack.tail.data)

    def peek(self):
        return self.stack.tail.data

    def size(self):
        return self.stack.length

    def isEmpty(self):
        return self.stack.length == 0


# Class implementation of a Queue
@dataclass
class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, data):
        self.queue.add(data)

    def dequeue(self):
        self.queue.remove(self.queue.head.data)

    def front(self):
        return self.queue.head.data

    def size(self):
        return self.queue.length

    def isEmpty(self):
        return self.queue.length == 0


# Class implementation of a Binary Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Class implementation of a dequeue
@dataclass
class Dequeue:
    def __init__(self):
        self.dequeue = LinkedList()

    def addFront(self, data):
        self.dequeue.add(data)

    def addRear(self, data):
        self.dequeue.add(data)

    def removeFront(self):
        self.dequeue.remove(self.dequeue.head.data)

    def removeRear(self):
        self.dequeue.remove(self.dequeue.tail.data)

    def isEmpty(self):
        return self.dequeue.length == 0

    def size(self):
        return self.dequeue.length

    def front(self):
        return self.dequeue.head.data

    def rear(self):
        return self.dequeue.tail.data


@dataclass
class Tree:
    def __init__(self):
        self.root = None

    def add(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        curr = self.root
        while curr:
            if data < curr.data:
                if curr.left is None:
                    curr.left = node
                    return
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = node
                    return
                curr = curr.right

    def search(self, data):
        if self.root is None:
            return
        curr = self.root
        while curr:
            if data < curr.data:
                curr = curr.left
            elif data > curr.data:
                curr = curr.right
            else:
                return curr
        return

    def remove(self, data):
        if self.root is None:
            return
        curr = self.root
        while curr:
            if data < curr.data:
                if curr.left is None:
                    return
                curr = curr.left
            elif data > curr.data:
                if curr.right is None:
                    return
                curr = curr.right
            else:
                if curr.left is None and curr.right is None:
                    return
                if curr.left is None:
                    temp = curr.right
                    curr.data = temp.data
                    curr.right = None
                    return
                if curr.right is None:
                    temp = curr.left
                    curr.data = temp.data
                    curr.left = None
                    return
                temp = curr.left
                while temp.right:
                    temp = temp.right
                curr.data = temp.data
                temp.right = curr.right
                curr.left = None
                return
        return


# Class implementation of a Binary Search Tree
@dataclass
class BST:
    def __init__(self):
        self.root = None

    def add(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        curr = self.root
        while curr:
            if data < curr.data:
                if curr.left is None:
                    curr.left = node
                    return
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = node
                    return
                curr = curr.right

    def search(self, data):
        if self.root is None:
            return
        curr = self.root
        while curr:
            if data < curr.data:
                curr = curr.left
            elif data > curr.data:
                curr = curr.right
            else:
                return curr
        return

    def remove(self, data):
        if self.root is None:
            return
        curr = self.root
        while curr:
            if data < curr.data:
                if curr.left is None:
                    return
                curr = curr.left
            elif data > curr.data:
                if curr.right is None:
                    return
                curr = curr.right
            else:
                if curr.left is None and curr.right is None:
                    return
                if curr.left is None:
                    temp = curr.right
                    curr.data = temp.data
                    curr.right = None
                    return
                if curr.right is None:
                    temp = curr.left
                    curr.data = temp.data
                    curr.left = None
                    return
                temp = curr.left
                while temp.right:
                    temp = temp.right
                curr.data = temp.data
                temp.right = curr.right
                curr.left = None
                return
        return


# Class implementation of a Heap
@dataclass
class Heap:
    def __init__(self):
        self.heap = LinkedList()

    def add(self, data):
        self.heap.add(data)

    def remove(self):
        self.heap.remove(self.heap.tail.data)

    def size(self):
        return self.heap.size()

    def isEmpty(self):
        return self.heap.isEmpty()

    def peak(self):
        return self.heap.head.data

    def get_parent(self, index):
        if index == 0:
            return None
        return int(index / 2)

    def get_left(self, index):
        if 2 * index + 1 > self.heap.length - 1:
            return None
        return 2 * index + 1

    def get_right(self, index):
        if 2 * index + 2 > self.heap.length - 1:
            return None
        return 2 * index + 2

    def get_top(self):
        return self.heap.head.data

    def get_top_left(self):
        return self.heap.head.left.data

    def get_top_right(self):
        return self.heap.head.right.data

    def sift_up(self, index):
        parent = self.get_parent(index)
        if parent is None:
            return
        if self.heap.head.data < self.heap.head.left.data:
            self.swap(index, self.heap.head.left.index)
            self.sift_up(parent)
            return
        if self.heap.head.data < self.heap.head.right.data:
            self.swap(index, self.heap.head.right.index)
            self.sift_up(parent)
            return
        return

    def sift_down(self, index):
        left = self.get_left(index)
        right = self.get_right(index)
        if left is None and right is None:
            return
        if left is None:
            if self.heap.head.data < self.heap.head.right.data:
                self.swap(index, self.heap.head.right.index)
                self.sift_down(self.get_right(index))
            return
        if right is None:
            if self.heap.head.data < self.heap.head.left.data:
                self.swap(index, self.heap.head.left.index)
                self.sift_down(self.get_left(index))
            return
        if self.heap.head.data < self.heap.head.left.data:
            self.swap(index, self.heap.head.left.index)
            self.sift_down(self.get_left(index))
            return
        if self.heap.head.data < self.heap.head.right.data:
            self.swap(index, self.heap.head.right.index)
            self.sift_down(self.get_right(index))
            return
        return


# Class implementation of a Hash
@dataclass
class Hash:
    def __init__(self):
        self.hash = {}

    def add(self, data):
        if data in self.hash:
            return
        self.hash[data] = True

    def remove(self, data):
        if data in self.hash:
            del self.hash[data]

    def search(self, data):
        return data in self.hash

    def size(self):
        return len(self.hash)

    def isEmpty(self):
        return self.size() == 0


# Class implementation of a Graph
@dataclass
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = LinkedList()

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        self.graph[vertex1].add(vertex2)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            return
        if vertex2 not in self.graph:
            return
        self.graph[vertex1].remove(vertex2)

    def search_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            return
        if vertex2 not in self.graph:
            return
        return vertex2 in self.graph[vertex1]

    def get_neighbors(self, vertex):
        if vertex not in self.graph:
            return
        return self.graph[vertex]

    def get_degree(self, vertex):
        if vertex not in self.graph:
            return
        return self.graph[vertex].size()

    def is_empty(self):
        return self.size() == 0

    def get_vertices(self):
        return self.graph.keys()

    def get_edges(self):
        edges = []
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                edges.append((vertex, neighbor))
        return edges

    def dfs(self, vertex, visited):
        visited[vertex] = True
        print(vertex)
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def bfs(self, vertex, visited):
        visited[vertex] = True
        queue = Dequeue()
        queue.append(vertex)
        while queue:
            vertex = queue.popleft()
            print(vertex)
            for neighbor in self.graph[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)


# Class implementation of a Segment Tree
@dataclass
class SegmentTree:
    def __init__(self, array, func):
        self.array = array
        self.func = func
        self.length = len(array)
        self.tree = [0] * (4 * self.length)
        self.construct()

    def construct(self):
        for index in range(self.length):
            self.tree[index + self.length] = self.array[index]
        for index in range(self.length - 1, -1, -1):
            self.tree[index] = self.func(self.tree[2 * index], self.tree[2 * index + 1])

    def update(self, index, value):
        index += self.length
        self.tree[index] = value
        while index > 0:
            index = (index - 1) // 2
            self.tree[index] = self.func(self.tree[2 * index], self.tree[2 * index + 1])

    def get(self, left, right):
        return self._query(left + self.length, right + self.length, 0)

    def _query(self, left, right, index):
        if left > right:
            return None
        if left == right:
            return self.tree[index]
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        mid = left_index + (right_index - left_index) // 2
        if left >= self.array[mid]:
            return self._query(left, right, left_index)
        elif right <= self.array[mid]:
            return self._query(left, right, right_index)
        else:
            return self.func(
                self._query(left, self.array[mid], left_index),
                self._query(self.array[mid], right, right_index),
            )
