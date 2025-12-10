from doctest import master
import tkinter as tk
import random
from tkinter import scrolledtext

class CacheSimulator:
    def __init__(self, cache_size, block_size, associativity, policy="LRU",):
    
        self.cache_size = cache_size
        self.block_size = block_size
        self.associativity = associativity
        self.policy = policy

        self.num_blocks = cache_size // block_size
        self.num_sets = self.num_blocks // self.associativity

        self.cache = [[] for _ in range(self.num_sets)]
        self.hits = 0
        self.misses = 0

        self.index_bits = self._log2(self.num_sets)
        self.offset_bits = self._log2(block_size)

    def _log2(self, x):
        return (x.bit_length() - 1) if x > 0 else 0

    # --- Replacement Policies ---
    def _apply_replacement(self, index, tag):
    # CASE 1: There is empty space → insert normally
        if len(self.cache[index]) < self.associativity:
            self.cache[index].append(tag)
            return

    # CASE 2: Set is full → apply replacement policy
        if self.policy == "LRU":
            # Remove least recently used (front)
            self.cache[index].pop(0)
            self.cache[index].append(tag)

        elif self.policy == "FIFO":
            # FIFO = same as LRU, but order is never updated on hit
            self.cache[index].pop(0)
            self.cache[index].append(tag)

        elif self.policy == "Random":
            # Random replacement
            evict = random.randrange(self.associativity)
            self.cache[index][evict] = tag

    def _lru_update(self, index, tag):
        self.cache[index].remove(tag)
        self.cache[index].append(tag)

    # --- Display Cache ---
    def display_cache(self, text_widget):
        text_widget.insert(tk.END, "Cache\n")
        text_widget.insert(tk.END, "-" * 120 + "\n")

        for i, cache_set in enumerate(self.cache):
            text_widget.insert(tk.END, f"Set {i:<2} | ")
            for tag in cache_set:
                text_widget.insert(tk.END, f"{tag:<32} ")
            text_widget.insert(tk.END, "\n" + "-" * 120 + "\n")

    # --- Memory Access ---
    def access_memory(self, address, text_widget):
        word_address = address // 4
        binary_address = format(address, "032b")

        offset = int(binary_address[-self.offset_bits:], 2)
        index = int(binary_address[-(self.offset_bits + self.index_bits):-self.offset_bits], 2)
        tag = binary_address[:-self.offset_bits]

        if tag in self.cache[index]:
            self.hits += 1
            hit_or_miss = "HIT"

            if self.policy == "LRU":
                self._lru_update(index, tag)

        else:
            self.misses += 1
            hit_or_miss = "MISS"

            if len(self.cache[index]) < self.associativity:
                self.cache[index].append(tag)
            else:
                self._apply_replacement(index, tag)

        text_widget.insert(tk.END, "{:<15}{:<40}{:<40}{:<40}{:<40}{:<30}\n".format(
            word_address, binary_address, tag, index, offset, hit_or_miss))

    # --- Run Simulation ---
    def simulate_memory_accesses(self, memory_accesses, text_widget):
        text_widget.insert(tk.END, "{:<15}{:<40}{:<40}{:<40}{:<40}{:<30}\n".format(
            "WordAddr", "BinAddr", "Tag", "Index", "Offset", "Hit/Miss"))
        text_widget.insert(tk.END, "-" * 250 + "\n")

        for address, _ in memory_accesses:
            self.access_memory(address, text_widget)

        text_widget.insert(tk.END, "-" * 250 + "\n")
        self.display_cache(text_widget)

    # --- Statistics ---
    def print_stats(self, text_widget):
        text_widget.insert(tk.END, "\n" + "-" * 60 + "\n")
        text_widget.insert(tk.END, "Simulation Statistics\n")
        text_widget.insert(tk.END, f"Replacement Policy: {self.policy}\n")
        text_widget.insert(tk.END, f"Cache Size: {self.cache_size} bytes\n")
        text_widget.insert(tk.END, f"Block Size: {self.block_size} bytes\n")
        text_widget.insert(tk.END, f"Associativity: {self.associativity}\n")
        text_widget.insert(tk.END, f"Number of Sets: {self.num_sets}\n")
        text_widget.insert(tk.END, f"Hits: {self.hits}\n")
        text_widget.insert(tk.END, f"Misses: {self.misses}\n")

        if self.hits + self.misses > 0:
            hit_rate = self.hits / (self.hits + self.misses) * 100
            text_widget.insert(tk.END, f"Hit Rate: {hit_rate:.2f}%\n")
        else:
            text_widget.insert(tk.END, "Hit Rate: N/A\n")
