from enum import Enum

class Types(Enum):
    LEFT_PAREN = 101
    RIGHT_PAREN = 102
    LEFT_BRACE = 103
    RIGHT_BRACE = 104
    COMMA = 105
    DOT = 106
    MINUS = 107
    PLUS = 108
    SEMICOLON = 109
    SLASH = 110
    STAR = 111

    BANG,
    BANG_EQUAL,
    EQUAL,
    EQUAL_EQUAL,
    GREATER,
    GREATER_EQUAL,
    LESS,
    LESS_EQUAL,

    IDENTIFIER,
    STRING,
    NUMBER,

    AND,
    CLASS,
    ELSE,
    FALSE,
    FUN,
    FOR,
    IF,
    NIL,
    OR,
    PRINT,
    RETURN,
    SUPER,
    THIS,
    TRUE,
    VAR,
    WHILE,

    EOF = -0