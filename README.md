# Letter Usage Counter

A simple Python program to count the frequency of letters in a user-provided text string. This tool filters out non-alphabetic characters, treats letters case-insensitively, and provides a clear summary of letter usage.

## Features

- Counts only alphabetic characters (ignores numbers, symbols, and spaces).
- Case-insensitive counting (e.g., 'A' and 'a' are treated as the same letter).
- Displays results in alphabetical order.

## Getting Started

### Prerequisites

Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/letter-usage-counter.git
    cd letter-usage-counter
    ```

2. (Optional) Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. Install dependencies (if any are added in the future):
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the program:
    ```bash
    python letter_counter.py
    ```

2. Enter a string when prompted.

3. View the results:
    ```
    Enter a string: Hello, World!
    
    Letter Usage Count:
    d: 1
    e: 1
    h: 1
    l: 3
    o: 2
    r: 1
    w: 1
    ```

### Example Input and Output

**Input:**
