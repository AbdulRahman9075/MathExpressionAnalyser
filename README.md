# Math Expression Evaluator with Lexer and Recursive Descent Parser

This Python program performs lexical and syntax analysis of mathematical expressions using a custom `Lexer` and `RecursiveDescentParser`. It then safely evaluates the expression, allowing user-defined variables.

---

## Features

- Tokenizes input expressions (Lexical Analysis)
- Parses expressions using Recursive Descent Parsing (Syntax Analysis)
- Identifies and prompts for values of variables (e.g., `x`, `a`, `b`)
- Supports standard math functions:
  - `sin`, `cos`, `tan`, `asin`, `acos`, `atan`
  - `sqrt`, `log`, `log10`, `exp`, `pow`
  - Constants: `pi`, `e`
- Handles power using `^` or `**`
- Safe evaluation using restricted environment

---

## Requirements

- Python 3.x
- `math` module (built-in)

Make sure you have `Lexer` and `RecursiveDescentParser` classes implemented in:

- `lexicalanalyser.py`
- `parser.py`

---

## How to Run

```bash
python main.py
