from lexicalanalyser import Lexer
from parser import RecursiveDescentParser
import pprint
import math
import re

# Safe eval function to evaluate mathematical expressions
def safe_eval(exp, variables):
    allowed_names = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "asin": math.asin,
        "acos": math.acos,
        "atan": math.atan,
        "sqrt": math.sqrt,
        "log": math.log,         # natural log
        "log10": math.log10,     # base-10 log
        "exp": math.exp,
        "pow": pow,
        "abs": abs,
        "round": round,
        "pi": math.pi,
        "e": math.e,
    }

    allowed_names.update(variables)
    exp = exp.replace("^", "**")
    try:
        result = eval(exp, {"__builtins__": None}, allowed_names)
        return result
    except Exception as e:
        print(f"Evaluation error: {e}")
        return None


# Extract variable names (simple alphabetic tokens not in math functions)
def extract_variables(tokens):
    keywords = {
        "sin", "cos", "tan", "asin", "acos", "atan", "sqrt", "log",
        "log10", "exp", "pow", "abs", "round", "pi", "e"
    }
    variables = set()
    for token in tokens:
        if token['type'] == 'IDENTIFIER':
            name = token['value']
            if name not in keywords:
                variables.add(name)
    return variables


# Main function
running = True
while running:
    equation = input("Enter an Expression: ")
    
    # Lexical analysis
    lexer = Lexer(equation)
    tokens = lexer.lexer()
    print("LEXICAL ANALYSIS OUTPUT:")
    pprint.pprint(tokens)
    print("\n\n")

    # Extract variables and get values
    var_names = extract_variables(tokens)
    user_vars = {}
    for var in var_names:
        while True:
            val = input(f"Enter value for '{var}': ")
            try:
                user_vars[var] = float(val)
                break
            except ValueError:
                print("Please enter a valid number.")

    # Syntax analysis
    print("SYNTAX ANALYSIS OUTPUT:")
    parser = RecursiveDescentParser(tokens)

    if parser.parse():
        result = safe_eval(equation, user_vars)
        if result is not None:
            print(f"Result = {result}")

    user_input = input("Enter Q to STOP | Press Enter to continue: ").strip().lower()
    if user_input == 'q':
        running = False
        print("\n\nProgram stopped.\n\n")
