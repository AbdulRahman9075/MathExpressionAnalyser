from lexicalanalyser import Lexer
from parser import RecursiveDescentParser
import pprint
import math
import os


def clear_screen():
     os.system('cls' if os.name == 'nt' else 'clear')

def safe_eval(exp):
    allowed_names = {
        "sin": math.sin, "cos": math.cos, "tan": math.tan,
        "asin": math.asin, "acos": math.acos, "atan": math.atan,
        "sqrt": math.sqrt, "log": math.log, "log10": math.log10,
        "exp": math.exp, "pow": pow, "abs": abs, "round": round,
        "pi": math.pi, "e": math.e
    }
    exp = exp.replace("^", "**")
    try:
        result = eval(exp, {"__builtins__": None}, allowed_names)
        return result
    except Exception as e:
        print(f"\n[!] Evaluation Error: {e}\n")
        return None

def get_variable_values(tokens):
    variables = {tok[0] for tok in tokens if tok[1] == "IDENTIFIER"}
    values = {}
    for var in variables:
        val = input(f"Enter value for {var}: ")
        try:
            values[var] = str(float(val))
        except ValueError:
            print(f"Invalid input for {var}, defaulting to 0")
            values[var] = "0"
    return values

def substitute_variables(expr, values):
    for var, val in values.items():
        expr = expr.replace(var, val)
    return expr

def main():
     clear_screen()
     print("=" * 60)
     print("\t\t MATH EXPRESSION ANALYZER.....")
     print("=" * 60)
     print("Supported functions: sin, cos, tan, sqrt, log, log10, exp, pi, e, etc.")
     print("Use '^' for power (e.g., 2^3), it will be auto-converted.")
     print("=" * 60)

     running = True
     while running:
        print("\n\n Enter a mathematical expression to evaluate:")
        equation = input(">>> ")
        print("\n🔍 LEXICAL ANALYSIS OUTPUT")
        print("-" * 60)
        lexer = Lexer(equation)
        tokens = lexer.lexer()
    
        pprint.pprint(tokens)
        print("\n\n")

        print("\n SYNTAX ANALYSIS OUTPUT")
        print("-" * 60)
        parser = RecursiveDescentParser(tokens)
        if parser.parse():
            var_values = get_variable_values(tokens)
            substituted_equation = substitute_variables(equation, var_values)
            result = safe_eval(substituted_equation)
            if result is not None:
                print(f"\n Evaluation Result: {result}")
       
        else:
             print("\n Syntax Error in Expression!")

        print("\n" + "-" * 60)
        user_input = input("Enter [Q] to quit or press [Enter] to try again: ").strip().lower()
        if user_input == 'q':
             running = False
             print("\n Program exited.\n")

if __name__ == "__main__":
     main()