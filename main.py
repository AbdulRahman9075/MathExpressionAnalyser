from lexicalanalyser import Lexer
from parser import RecursiveDescentParser
import pprint
import math

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
        print(f"Evaluation error: {e}")
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

# Main loop
running = True
while running:
    equation = input("Enter an Expression: ")
    lexer = Lexer(equation)
    tokens = lexer.lexer()
    print("LEXICAL ANALYSIS OUTPUT:")
    pprint.pprint(tokens)
    print("\n")

    print("SYNTAX ANALYSIS OUTPUT:")
    parser = RecursiveDescentParser(tokens)
    if parser.parse():
        var_values = get_variable_values(tokens)
        substituted_equation = substitute_variables(equation, var_values)
        result = safe_eval(substituted_equation)
        if result is not None:
            print(f"Result = {result}")

    user_input = input("Enter Q to STOP | Press Enter to continue: ").strip().lower()
    if user_input == 'q':
        running = False
        print("\nProgram stopped.\n")
