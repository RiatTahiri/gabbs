from ast import literal_eval


class Lex:
    def __init__(self, userInput):
        tokenType = ''
        lexeme = ''
        literal = ''
        line = ''