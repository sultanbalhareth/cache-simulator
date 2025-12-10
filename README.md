# **Cache Simulator**

## **Table of Contents**

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Launch the Application](#1-launch-the-application)
  - [Configure Cache Parameters](#2-configure-cache-parameters)
  - [Run Simulation](#3-run-simulation)
  - [Update Statistics](#4-update-statistics)
- [Implementation Details](#implementation-details)
- [Screenshots](#screenshots)

## **Overview**

The Cache Simulator project provides a graphical user interface (GUI) application for simulating memory accesses and analyzing cache system performance. The simulator allows users to configure cache parameters and visualize the behavior of different cache configurations.

## **Features**

- **Graphical User Interface (GUI)** for easy interaction.
- Configurable cache parameters: cache size, block size, and associativity.
- Simulation of memory accesses with hit/miss tracking.
- Display of simulation statistics, including hit rate.
- Hexadecimal Memory Access Input: Users can enter comma-separated hex addresses for simulation. (added by sultan balhareth)
- Automatic Memory Access Option: Provided default memory accesses for quick testing. (added by sultan balhareth)
- Input Validation: Ensured cache size, block size, and associativity are powers of 2 and compatible. (added by sultan balhareth)
- Different replacment policies are applied such as LFU, FIFO, and Random replacment (added by sultan balhareth)

## **Project Structure**

The project is organized into the following main files:

1. **`cache_simulator.py`**: Contains the `CacheSimulator` class, which represents the cache memory system and its operations.
2. **`gui.py`**: Contains the `CacheSimulatorGUI` class, responsible for creating the graphical user interface using Tkinter.
3. **`main.py`**: The main script that initializes the Tkinter application and runs the GUI.

## **Installation**

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/sultanbalhareth/cache-simulator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd cache-simulator
   ```

3. Run the main script:

   ```bash
   python main.py
   ```

   _Note: Make sure you have Python installed on your system._

   _Tkinter is usually included with standard Python installations, so you typically don't need to install it separately using `pip`. However, if you encounter issues or if you're using a virtual environment, you can try the following command:_

   ```bash
   pip install tk
   ```

   _Keep in mind that the actual package name might vary depending on your operating system. If you're on Linux, you might need to use:_

   ```bash
   sudo apt-get install python3-tk
   ```

   _On macOS, you can use Homebrew:_

   ```bash
   brew install python-tk
   ```

## **Usage**

### 1. Launch the Application

- Follow the installation instructions.
- Execute the main script to launch the GUI.

### 2. Configure Cache Parameters

- Enter the desired cache parameters (cache size, block size, associativity) in the GUI.

### 3. Run Simulation

- Click the "Run Simulation" button to simulate memory accesses and view the results.

### 4. Update Statistics

- Click the "Update Statistics" button to display simulation statistics.

## **Implementation Details**

The core functionality is encapsulated in the `CacheSimulator` class, providing methods for cache initialization, LRU-based updates, FIFO updates, Random updates, and visual representation. The `CacheSimulatorGUI` class utilizes Tkinter for the GUI implementation.

You don't need to adjust the code and enter memory access values via the code, now the GUI provides a text input to insert memory access that you want.

```python

# Create and run the GUI
root = tk.Tk()
gui = CacheSimulatorGUI(root)
root.mainloop()
```

This code snippet demonstrates how to use the `CacheSimulator` and `CacheSimulatorGUI` classes in your Python script.

## **Screenshots**

(cache_simulator.PNG) <img width="624" alt="image" src="https://github.com/aksh1009/cache-simulator/assets/143216212/935b9181-083e-4ea7-93fe-807f06c8a090">
