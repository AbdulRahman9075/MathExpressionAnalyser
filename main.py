from lexicalanalyser import Lexer
from parser import RecursiveDescentParser
import pprint
import math

# Safe eval function to evaluate mathematical expressions
def safe_eval(exp):
    
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
        "e": math.e
    }
    exp = exp.replace("^", "**")
    try:
        # Evaluate the expression in a safe environment
        result = eval(exp, {"__builtins__": None}, allowed_names)
        return result
    except Exception as e:
        print(f"Evaluation error: {e}")
        return None


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

    # Syntax analysis
    print("SYNTAX ANALYSIS OUTPUT:")
    parser = RecursiveDescentParser(tokens)

    # Perform syntax analysis
    if parser.parse(): 
        result = safe_eval(equation)
        if result is not None:
            print(f"Result = {result}")

    user_input = input("Enter Q to STOP | Press Enter to continue: ").strip().lower()
    if user_input == 'q':
        running = False
        print("\n\nProgram stopped.\n\n")