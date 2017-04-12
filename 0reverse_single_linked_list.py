#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 单链表反转

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError('Data not in list')
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

linked_list = LinkedList()
linked_list.insert('a')
linked_list.insert('b')
linked_list.insert('c')
linked_list.insert('d')
linked_list.insert('e')

# current_node = linked_list.head
# while current_node is not None:
#     print current_node.get_data()
#     current_node = current_node.get_next()


def reverse_linkedlist():
    a = linked_list.head
    b = linked_list.head.get_next()

    while b is not None:
        a.set_next(b.get_next())
        linked_list.insert(b.get_data())
        b = a.get_next()

    current_node = linked_list.head
    while current_node is not None:
        print current_node.get_data()
        current_node = current_node.get_next()

reverse_linkedlist()
