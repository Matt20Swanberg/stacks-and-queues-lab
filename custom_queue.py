import random

class Queue:
    """
    Implement a First In, First Out (FIFO) queue.

    Customers are stored in a Python list and processed
    in the order they were added.
    """

    def __init__(self):
        """Initialize an empty queue"""
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue"""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the first item, or None if empty"""
        if not self.items:
            return None
        return self.items.pop(0)
    
    def peek(self):
        """Return the first item without removing it"""
        if not self.items:
            return None
        return self.items[0]

    def is_empty(self):
        """Return True if the queue is empty; otherwise False"""
        if not self.items:
            return True
        return False

    def select_and_announce_winner(self):
        """
        Randomly select a customer from the queue.

        Remove all customers ahead of the winner, including
        the winner, while preserving FIFO order.

        Returns:
            The selected customer's name, or None if the
            queue is empty.
        """

        # Prevent selecting a winner from an empty queue
        if self.is_empty():
            return None

        # Randomly select a customer without removing them
        random_winner = random.choice(self.items)

        # Dequeue customers until the winner reaches the front
        while self.peek() != random_winner:
            self.dequeue()

        # Remove the selected winner from the queue
        self.dequeue()

        # Return the winner's name after removal
        return random_winner