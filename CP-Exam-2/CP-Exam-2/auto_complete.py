""" 
A simple autocompletion application.  The only purpose is to illustrate
some of the functionality of the Trie class. 

Author: Nathan Sprague
Version: 4/10/13 
"""


import tkinter as tk

import trie

# Globals controlling layout
NUM_LINES = 24
TEXT_WIDTH = 40
ENTRY_WIDTH = 30


class AutoCompleter(tk.Frame):
    """This class represents the Autocompletion Frame widget."""

    def __init__(self, parent, dictionaryFile):
        """Create the necessary widgets and pack them into the frame."""

        tk.Frame.__init__(self, parent)
        self.dictionary = trie.Trie()
        self._read_dictionary(dictionaryFile)
        parent.title("CS240 Auto Completion")

        self.entry = tk.Entry(parent, width=ENTRY_WIDTH)
        self.entry.grid(row=0, column=0)
        self.entry.bind("<KeyRelease>", self._entry_callback)
        self.entry.pack()

        self.text = tk.Text(self, height=NUM_LINES, width=TEXT_WIDTH)
        self.text.grid(row=1, column=0)
        self.text.config(state=tk.DISABLED)

        self.pack()

    def _read_dictionary(self, dict_loc):
        """
        Build the Trie from a dictionary file. The file should have
        one word per line.
        """
        with open(dict_loc, "r") as f:
            for line in f:
                self.dictionary.insert(line.rstrip())

    def _entry_callback(self, *args):
        """
        This will be called every time a key is released in the entry
        box.  Updates the text box with possible completions (in no
        particular order).
        """
        count = 0
        result = ""
        if len(self.entry.get()) > 0:
            for word in self.dictionary.prefix_iter(self.entry.get()):
                result += word + "\n"
                count += 1
                if count >= NUM_LINES:
                    break
        self.text.config(state=tk.NORMAL)
        self.text.delete("0.0", "end")
        self.text.insert("0.0", result)
        self.text.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    sc = AutoCompleter(root, "american-english.txt")
    root.mainloop()
