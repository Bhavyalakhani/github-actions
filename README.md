# GitHub Actions Lab — Calculator Project

A small Python calculator module used to practice testing (pytest and unittest) and GitHub Actions CI/CD.

## What This Project Does

This repo provides a **calculator library** in `src/calculator.py` with the following operations:

| Function | Description |
|----------|-------------|
| `fun1(x, y)` | Add two numbers |
| `fun2(x, y)` | Subtract `y` from `x` |
| `fun3(x, y)` | Multiply two numbers |
| `fun4(x, y, z)` | Add three numbers |
| `fun5(x, y)` | Divide `x` by `y` (raises if `y == 0` or non-numeric) |
| `fun6(x, y)` | Power: `x ** y` |
| `fun7(x, y)` | Modulo: `x % y` (raises if `y == 0` or non-numeric) |

Input validation is applied where needed: non-numeric inputs raise `ValueError`, and division/modulo by zero raise `ValueError` with clear messages.

Tests live in `test/` and are written in both **pytest** and **unittest**.

---

## Setup: Virtual Environment

Use a virtual environment so project dependencies don’t affect your system Python.

**1. Create the virtual environment** (from the project root):

```bash
python3 -m venv github_action_lab1
```

**2. Activate it:**

- **macOS / Linux:**
  ```bash
  source github_action_lab1/bin/activate
  ```
- **Windows (Command Prompt):**
  ```cmd
  github_action_lab1\Scripts\activate.bat
  ```
- **Windows (PowerShell):**
  ```powershell
  github_action_lab1\Scripts\Activate.ps1
  ```

**3. Install dependencies:**

```bash
pip install -r requirements.txt
```

**4. Deactivate when you’re done:**

```bash
deactivate
```

---

## Running Tests Locally

From the project root (with the virtual environment **activated**):

```bash
# Run pytest
pytest test/test_pytest.py -v

# Run unittest
python -m unittest test.test_unittest -v
```

---

## How GitHub Actions Are Configured

Workflows are defined under `.github/workflows/`. Here’s what each one does:

### 1. **Run tests on push** — `github_lab1_pytest_action.yml`

- **Trigger:** Push to `main`
- **Steps:** Checkout → Set up Python 3.8 → Install deps from `requirements.txt` → Run pytest with JUnit XML → Upload `pytest-report.xml` as an artifact → Echo success/failure
- **Purpose:** Run pytest in CI and keep test results as artifacts.

- **Steps:** Run `python -m unittest test/test_unittest.py` → Echo success/failure
- **Purpose:** Run the unittest suite on every push to `main`.

- **Steps:** Run `pytest -v` → Echo success/failure
- **Purpose:** Run the unittest suite on every push to `main`.

---

## Project Layout

```
.
├── .github/workflows/   # GitHub Actions definitions
├── src/
│   └── calculator.py   # Calculator functions
├── test/
│   ├── test_pytest.py  # Pytest tests
│   └── test_unittest.py # Unittest tests
├── requirements.txt   # pytest (unittest is stdlib)
└── README.md
```

**Note:** The workflows above use root fodler. To run the **calculator** tests from this repo in CI, you can add a workflow that uses the root `requirements.txt` and `test/` (and optionally `src/`) paths, or align your folder structure with those paths.
