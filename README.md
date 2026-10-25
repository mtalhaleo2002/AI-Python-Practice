# DigiSkills AI with Python — Exercise 1

Solutions for Hands-on Exercise 1 of the DigiSkills 3.0 Batch-04 Artificial Intelligence using Python course. The exercises cover Python loops and conditionals, NumPy arrays, and object-oriented programming.

## Project structure

```text
.
├── .gitignore
├── README.md
├── requirements.txt
├── task1.py
├── task2.py
├── task3.py
├── generate_docx.py
└── generate_html.py
```

The `output/` and `output_solution/` folders contain local test results and generated submission files. They are excluded from Git and will not be present when this repository is cloned. The local virtual environment and Python cache files are also excluded.

## Exercises

### Task 1 — Sales and tax

Prompts for the daily sales amounts of five employees, applies the specified tax rate (5% below Rs. 50,000; 10% from Rs. 50,000 to Rs. 100,000; 15% above Rs. 100,000), and prints each employee's tax along with total and average sales.

### Task 2 — NumPy array

Creates a NumPy array with the marks `[78, 85, 92, 67, 88]`, displays its data type, converts it to a float array, and displays the result.

### Task 3 — Bank account and OOP

Demonstrates `Customer` and `Account` classes, including account creation, deposits, withdrawals, and balance display.

## Requirements

- Python 3.8 or later
- Packages listed in [`requirements.txt`](requirements.txt)

## Setup

From the repository directory, create and activate a virtual environment.

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the exercises

```bash
python task1.py
python task2.py
python task3.py
```

Task 1 prompts for five sales amounts. Tasks 2 and 3 run without additional input.

## Optional report scripts

`generate_docx.py` creates a Word report under `output_solution/`. It expects the task screenshots (`task1.png`, `task2.png`, and `task3.png`) to already exist in that folder; the script does not create those screenshots. The output folder and generated report are ignored by Git.

`generate_html.py` defines a helper that formats a Python source file and a saved output file as HTML. It does not run the task scripts or create screenshots.
