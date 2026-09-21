"""ITECC04 Laboratory 4, Part A2: the linked-list-based stack.

Same public interface as ArrayStack. Different storage, same contract. That
is the point of the exercise: code that uses a stack should not be able to
tell which one it was handed.

The HEAD of the list is the top. Pushing means making a new node whose next
is the old top. Popping means moving the head forward one node. Neither walks
the list, so both are O(1), the same as the array version.

You wrote Node in Chapter 3. This one is given so you can spend the time on
the stack itself.
"""


class Node:
    """Written for you."""

    __slots__ = ("value", "next")

    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


class LinkedStack:

    def __init__(self):
        """Step 1. An empty stack has no top node and holds no items.

        Keep a running count. Walking the list to answer size() would make an
        O(1) question cost O(n).
        """
        raise NotImplementedError("Step 1: set self._top to None and self._size to 0")

    def push(self, item):
        """Step 2. New node on the front, then update the count.

        Order matters. Build the node pointing at the current top FIRST,
        then move self._top. Reverse the two lines and you lose the list.
        """
        raise NotImplementedError("Step 2: make a Node whose next is the old top, then move self._top")

    def pop(self):
        """Step 3. Remove and return the value at the top.

        Guard for empty with IndexError. Hold the node, move self._top to
        its next, decrement the count, then return the value.
        """
        raise NotImplementedError("Step 3: guard for empty, unlink the head node, return its value")

    def peek(self):
        """Step 4. Return the top value without unlinking anything."""
        raise NotImplementedError("Step 4: guard for empty, then return the value at self._top")

    def is_empty(self):
        """Step 5. True when there is no top node."""
        raise NotImplementedError("Step 5: return whether self._top is None")

    def size(self):
        """Step 6. Return the running count, not a walk of the list."""
        raise NotImplementedError("Step 6: return self._size")

    def __len__(self):
        """Written for you."""
        return self.size()
