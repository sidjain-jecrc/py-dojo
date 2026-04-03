# py-dojo

A lightweight, AI-assisted environment for practicing real-world Python coding problems. Problems come with a skeleton and pre-written test cases — you just write the solution and run the tests.

---

## How it works

1. You describe a problem to Claude
2. Claude creates a `solution.py` skeleton and `tests.py` with test cases
3. You write your solution in `solution.py`
4. You run the test runner to see what passes and what doesn't

---

## Setup

**Requirements:** Python 3.10+

```bash
git clone <repo-url>
cd py-dojo
```

No dependencies. No virtual environment needed. The runner uses only the standard library.

---

## Solving a problem

Each problem lives in its own folder under `problems/`:

```
problems/
└── two_sum/
    ├── solution.py   ← you edit this
    └── tests.py      ← don't touch this
```

**Steps:**

1. Open `problems/<problem_name>/solution.py`
2. Read the problem description at the top of the file
3. Implement the function (replace `raise NotImplementedError`)
4. Run the tests:

```bash
python3 runner.py <problem_name>
```

**Example:**

```bash
python3 runner.py two_sum
```

```
=======================================================
  Problem: Two Sum
=======================================================

  [1] Basic case
       PASS

  [2] Target at end of list
       PASS

  [3] Duplicate values
       PASS

  [4] Negative numbers
       FAIL
       Input:    [-1, -2, -3, -4, -5]
       Expected: [2, 4]
       Got:      [1, 3]

  [5] Single pair in longer list
       PASS

=======================================================
  Results: 4/5 passed  -- 1 failed
=======================================================
```

---

## Getting a new problem

Open a Claude Code session in this directory and describe the problem you want to practice:

```
I want to practice: given a binary tree, return its level-order traversal as a list of lists.
```

Claude will create the problem folder, skeleton, and test cases for you. Then just open `solution.py` and start coding.

---

## Problems included

| Problem | Folder | Description |
|---------|--------|-------------|
| Two Sum | `two_sum` | Find indices of two numbers that add up to a target |
| Claim Assignment Balancing | `claim_assignment` | Assign claims to specialists while balancing workloads |

---

## Project structure

```
py-dojo/
├── README.md
├── runner.py          # Test runner — do not modify
└── problems/
    └── <problem_name>/
        ├── solution.py    # Your code goes here
        └── tests.py       # Test cases — do not modify
```

---

## Tips

- Tests run in order — fix failures from the top down
- A `SKIP` means you haven't implemented the function yet (`raise NotImplementedError` is still there)
- An `ERROR` means your code threw an unexpected exception — the traceback is printed below it
- The runner exits with code `0` if all tests pass, `1` otherwise (useful for scripting)
