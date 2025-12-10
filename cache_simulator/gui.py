# gui.py
import tkinter as tk
from tkinter import scrolledtext, ttk
from cache_simulator import CacheSimulator

class CacheSimulatorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Cache Simulator")
        # Log area
        self.log_text = scrolledtext.ScrolledText(master, width=100, height=2,)
        self.log_text.pack(padx=10, pady=10, expand=True, fill="both")

        # Cache configuration
        self.cache_size_label = tk.Label(master, text="Cache Size (bytes):")
        self.cache_size_label.pack()
        self.cache_size_entry = tk.Entry(master, width=10)
        self.cache_size_entry.pack()

        self.block_size_label = tk.Label(master, text="Block Size (bytes):")
        self.block_size_label.pack()
        self.block_size_entry = tk.Entry(master, width=10)
        self.block_size_entry.pack()

        self.associativity_label = tk.Label(master, text="Associativity:")
        self.associativity_label.pack()
        self.associativity_entry = tk.Entry(master, width=10)
        self.associativity_entry.pack()

        # Dropdown menu for replacement policy
        self.policy_label = tk.Label(master, text="Replacement Policy:")
        self.policy_label.pack()

        self.policy_var = tk.StringVar(value="LRU")
        self.policy_menu = ttk.Combobox(
            master,
            textvariable=self.policy_var,
            values=["LRU", "FIFO", "Random"],
            state="readonly",
            width=10
        )
        self.policy_menu.pack()

        # Memory access input
        self.mem_label = tk.Label(
            master,
            text="Memory Accesses (comma-separated hex addresses, e.g., 0x0A, 0x522, 0x1034, 0x10, 0x64):"
        )
        self.mem_label.pack()
        self.mem_entry = tk.Entry(master, width=50)
        self.mem_entry.pack()

        # Buttons
        self.run_simulation_button = tk.Button(master, text="Run Simulation", command=self.run_simulation)
        self.run_simulation_button.pack(pady=5)

        self.update_stats_button = tk.Button(master, text="Update Statistics", command=self.update_stats)
        self.update_stats_button.pack(pady=5)

    def run_simulation(self):
        # Parse cache configuration
        try:
            cache_size = int(self.cache_size_entry.get())
            block_size = int(self.block_size_entry.get())
            associativity = int(self.associativity_entry.get())
        except ValueError:
            self.log_text.delete(1.0, tk.END)
            self.log_text.insert(tk.END, "Cache size, block size, and associativity must be integers.\n")
            return

        # Validate powers of 2
        if (cache_size & (cache_size - 1)) != 0:
            self.log_text.delete(1.0, tk.END)
            self.log_text.insert(tk.END, "Cache size must be a power of 2.\n")
            return

        if (block_size & (block_size - 1)) != 0:
            self.log_text.delete(1.0, tk.END)
            self.log_text.insert(tk.END, "Block size must be a power of 2.\n")
            return

        if (associativity & (associativity - 1)) != 0:
            self.log_text.delete(1.0, tk.END)
            self.log_text.insert(tk.END, "Associativity must be a power of 2.\n")
            return

        if block_size * associativity > cache_size:
            self.log_text.delete(1.0, tk.END)
            self.log_text.insert(tk.END, "Block size × associativity cannot exceed cache size.\n")
            return

        # Read selected policy
        policy = self.policy_var.get()

        # Initialize simulator
        self.cache_simulator = CacheSimulator(cache_size, block_size, associativity, policy)

        # Parse memory accesses
        mem_text = self.mem_entry.get()
        try:
            addresses = [int(x.strip(), 16) for x in mem_text.split(',') if x.strip()]
            memory_accesses = [(addr, 0) for addr in addresses]
        except ValueError:
            self.log_text.delete(1.0, tk.END)
            self.log_text.insert(tk.END, "Invalid memory access input! Use hex addresses separated by commas.\n")
            return

        # Run simulation
        self.log_text.delete(1.0, tk.END)
        self.cache_simulator.simulate_memory_accesses(memory_accesses, self.log_text)

    def update_stats(self):
        self.log_text.delete(1.0, tk.END)
        self.cache_simulator.print_stats(self.log_text)
