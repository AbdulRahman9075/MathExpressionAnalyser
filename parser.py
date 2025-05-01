class RecursiveDescentParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def current_token(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None

    def eat(self, expected_type):
        token = self.current_token()
        if token and token[1] == expected_type:
            self.position += 1
            return token
        raise SyntaxError(f"Expected {expected_type}, got {token}")

    def parse(self):
        try:
            self.expr()
            if self.current_token() is not None:
                raise SyntaxError("Unexpected input after valid expression.")
            print("Accept")
            print("Syntax Analysis complete. The equation is syntactically correct.")
            return True
        except SyntaxError as e:
            print("Reject")
            print("Syntax Analysis complete. The equation is syntactically wrong.")
            print(f"Error: {e}")
            return None

    def expr(self):
        self.term()
        while self.current_token() and self.current_token()[1] in ("PLUS", "MINUS"):
            self.eat(self.current_token()[1])
            self.term()

    def term(self):
        self.power()
        while self.current_token() and self.current_token()[1] in ("TIMES", "DIVIDE"):
            self.eat(self.current_token()[1])
            self.power()

    def power(self):
        self.factor()
        if self.current_token() and self.current_token()[1] == "POWER":
            self.eat("POWER")
            self.power()

    def factor(self):
        token = self.current_token()
        if token and token[1] == "NUMBER":
            self.eat("NUMBER")
        elif token and token[1] == "IDENTIFIER":
            self.eat("IDENTIFIER")
        elif token and token[1] == "FUNCTION":
            self.eat("FUNCTION")
            self.eat("OPEN_PARENS")
            self.expr()
            while self.current_token() and self.current_token()[1] == "COMMA":
                self.eat("COMMA")
                self.expr()
            self.eat("CLOSE_PARENS")
        elif token and token[1] == "OPEN_PARENS":
            self.eat("OPEN_PARENS")
            self.expr()
            self.eat("CLOSE_PARENS")
        elif token and token[1] == "MINUS":
            self.eat("MINUS")
            self.factor()
        else:
            raise SyntaxError("Invalid factor.")
