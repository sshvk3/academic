"""Trie class that supports spell checking and auto-completion

Author: K Shivashankar
Date: 07/10/2023

"""

class Trie:
    """
    Trie class that supports spell checking and auto-completion.
    """

    def __init__(self):
        """
        Create a new empty Trie.
        """
        self.root = {}

    def insert(self, word):
        """
        Insert a word into the Trie.

        Args:
            word (str): The word to insert.

        Returns:
            None
        """
        current_node = self.root
        for char in word:
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]
        current_node['_end'] = True

    def search(self, word):
        """
        Check if a word is in the Trie.

        Args:
            word (str): The word to search for.

        Returns:
            bool: True if the word is in the Trie, False otherwise.
        """
        current_node = self.root
        for char in word:
            if char not in current_node:
                return False
            current_node = current_node[char]
        return '_end' in current_node

    def starts_with(self, prefix):
        """
        Check if there are words in the Trie that start with a given prefix.

        Args:
            prefix (str): The prefix to check.

        Returns:
            bool: True if there are words with the specified prefix, False otherwise.
        """
        current_node = self.root
        for char in prefix:
            if char not in current_node:
                return False
            current_node = current_node[char]
        return True

    def __len__(self):
        """
        Return the number of words stored in this Trie.

        Returns:
            int: The number of words in the Trie.
        """
        return self._count_words(self.root)

    def _count_words(self, node):
        count = 0
        if '_end' in node:
            count += 1
        for char, child_node in node.items():
            if char != '_end':
                count += self._count_words(child_node)
        return count

    def __contains__(self, word):
        """
        Check if a word is in the Trie using the 'in' operator.

        Args:
            word (str): The word to check.

        Returns:
            bool: True if the word is in the Trie, False otherwise.
        """
        return self.search(word)

    def __iter__(self):
        """
        Return an iterator that allows iteration over all words in the Trie in lexicographical (alphabetical) order.

        Returns:
            iterator: An iterator over words in the Trie.
        """
        return self._iterate_words(self.root, "")

    def _iterate_words(self, node, current_word):
        if '_end' in node:
            yield current_word
        for char, child_node in node.items():
            if char != '_end':
                yield from self._iterate_words(child_node, current_word + char)

    def contains_prefix(self, prefix):
        """
        Check if a string is a word in the Trie or is a prefix of any word in the Trie.

        Args:
            prefix (str): The string to check.

        Returns:
            bool: True if the string is a word or a prefix, False otherwise.
        """
        return self.starts_with(prefix)

    def prefix_iter(self, prefix):
        """
        Return an iterator that allows iteration over all words in the Trie that have the specified prefix,
        in lexicographic (alphabetical) order.

        Args:
            prefix (str): The prefix to filter words.

        Returns:
            iterator: An iterator over words with the specified prefix in the Trie.
        """
        current_node = self.root
        for char in prefix:
            if char not in current_node:
                return
            current_node = current_node[char]
        yield from self._iterate_words(current_node, prefix)
