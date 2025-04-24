import re
import sys

class Lexer:
    def __init__(self, text):
        self.text = text
        self.tokenNames = ["OPEN_PARENS", "CLOSE_PARENS", "PLUS", "MINUS", "TIMES", "DIVIDE", "POWER", "NUMBER", "FUNCTION", "COMMA"]
        self.numOrSymbol = re.compile(r'(\d+\.\d+|\d+|[a-zA-Z_][a-zA-Z_0-9]*|[^\s\d\w])')  # match numbers, functions, or any non-space, non-digit, non-word character
        self.tokens = []
        self.errors = []

    def lexer(self):
        self.tokenize = re.findall(self.numOrSymbol, self.text)
        for tok in self.tokenize:
            if tok == '(':
                self.tokens.append([tok, self.tokenNames[0]])  # OPEN_PARENS
            elif tok == ')':
                self.tokens.append([tok, self.tokenNames[1]])  # CLOSE_PARENS
            elif tok == '+':
                self.tokens.append([tok, self.tokenNames[2]])  # PLUS
            elif tok == '-':
                self.tokens.append([tok, self.tokenNames[3]])  # MINUS
            elif tok == '*':
                self.tokens.append([tok, self.tokenNames[4]])  # TIMES
            elif tok == '/':
                self.tokens.append([tok, self.tokenNames[5]])  # DIVIDE
            elif tok == '^':
                self.tokens.append([tok, self.tokenNames[6]])  # POWER
            elif tok == ',':
                self.tokens.append([tok, self.tokenNames[9]])  # COMMA
            elif tok.isnumeric() or re.match(r'\d+\.\d+', tok):  # For floating point numbers as well
                self.tokens.append([tok, self.tokenNames[7]])  # NUMBER
            elif tok in ["sin", "cos", "tan", "log", "sqrt", "abs", "pow", "acos", "asin", "atan", "exp"]:  # Add functions here
                self.tokens.append([tok, self.tokenNames[8]])  # FUNCTION
            else:
                self.errors.append(tok)

        if not self.errors:
            return self.tokens
        else:
            print("Error! Found unknown tokens.")
            print(self.errors)
            sys.exit()

