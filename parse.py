from .constants import *

def parse(tokens, is_root = False):
    t = tokens[0]
    if is_root and t != JSON_LEFTBRACE:
        raise Exception('Root must be an object')
    if t == JSON_LEFTBRACKET:
        return parse_array(tokens[1:])
    elif t == JSON_LEFTBRACE:
        return parse_object(tokens[1:])
    else:
        return t, tokens[1:]

def parse_array(tokens):
    json_array = []
    t = tokens[0]
    if t == JSON_RIGHTBRACKET:
        return json_array, tokens[1:] 
    while True:
        json, tokens = parse(tokens)
        json_array.append(json)

        t = tokens[0]
        if t == JSON_RIGHTBRACKET:
            return json_array, tokens[1:]
        elif t != JSON_COMMA:
            raise Exception("JSON comma expected")
        tokens = tokens[1:]
    raise Exception("Expected EOL JSON bracket")

def parse_object(tokens):
    json_object = {}
    t = tokens[0]
    if t == JSON_RIGHTBRACE:
        return json_object, tokens[1:]
    while True:
        json_key = tokens[0]
        if type(json_key) is str:
            tokens = tokens[1:]
        else:
            raise Exception("Excpected string keys")
        if tokens[0] != JSON_COLON:
            raise Exception("Expected a colon after key")
        json_value, tokens = parse(tokens[1:])
        json_object[json_key] = json_value

        t = tokens[0]
        if t == JSON_RIGHTBRACE:
            return json_object, tokens[1:]
        elif t != JSON_COMMA:
            raise Exception("Expected comma after key value pair")
        tokens = tokens[1:]
    raise Exception("Expected End of Object brace")