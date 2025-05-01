import re
import sys

class Lexer:
    def __init__(self, text):
        self.text = text
        self.tokenNames = [
            "OPEN_PARENS", "CLOSE_PARENS", "PLUS", "MINUS", "TIMES", "DIVIDE",
            "POWER", "NUMBER", "FUNCTION", "COMMA", "IDENTIFIER"
        ]
        self.numOrSymbol = re.compile(r'(\d+\.\d+|\d+|[a-zA-Z_][a-zA-Z_0-9]*|[^\s\d\w])')
        self.tokens = []
        self.errors = []

    def lexer(self):
        self.tokenize = re.findall(self.numOrSymbol, self.text)
        for tok in self.tokenize:
            if tok == '(':
                self.tokens.append([tok, "OPEN_PARENS"])
            elif tok == ')':
                self.tokens.append([tok, "CLOSE_PARENS"])
            elif tok == '+':
                self.tokens.append([tok, "PLUS"])
            elif tok == '-':
                self.tokens.append([tok, "MINUS"])
            elif tok == '*':
                self.tokens.append([tok, "TIMES"])
            elif tok == '/':
                self.tokens.append([tok, "DIVIDE"])
            elif tok == '^':
                self.tokens.append([tok, "POWER"])
            elif tok == ',':
                self.tokens.append([tok, "COMMA"])
            elif tok.isnumeric() or re.match(r'^\d+\.\d+$', tok):
                self.tokens.append([tok, "NUMBER"])
            elif tok in [
                "sin", "cos", "tan", "log", "sqrt", "abs", "pow",
                "acos", "asin", "atan", "exp", "log10"
            ]:
                self.tokens.append([tok, "FUNCTION"])
            elif re.match(r'^[a-zA-Z_][a-zA-Z_0-9]*$', tok):
                self.tokens.append([tok, "IDENTIFIER"])
            else:
                self.errors.append(tok)

        if not self.errors:
            return self.tokens
        else:
            print("Error! Found unknown tokens.")
            print(self.errors)
            sys.exit()
