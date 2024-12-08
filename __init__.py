from .lexer import lex
from .parse import parse

def from_string(string):
    tokens = lex(string)
    return parse(tokens, is_root=True)[0]
  