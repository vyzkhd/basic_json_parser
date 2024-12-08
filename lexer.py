from .constants import *
JSON_SYNTAX = [JSON_COMMA, JSON_COLON, JSON_LEFTBRACKET, JSON_RIGHTBRACKET,
               JSON_LEFTBRACE, JSON_RIGHTBRACE]

def lex(str):
    tokens = []
    while str:
        json_str, str = lex_string(str)
        if json_str is not None:
            tokens.append(json_str)
            continue

        json_number, str = lex_number(str)
        if json_number is not None:
            tokens.append(json_number)
            continue

        json_bool, str = lex_bool(str)
        if json_bool is not None:
            tokens.append(json_bool)
            continue

        json_null, str = lex_null(str)
        if json_null is not None:
            tokens.append(json_null)
            continue 

        if str[0] in JSON_WHITESPACE:
            str = str[1:]
        elif str[0] in JSON_SYNTAX:
            tokens.append(str[0])
            str = str[1:]
        else:
            raise Exception(f"Unexpected character {str[0]}")
    return tokens 

def lex_string(str):
    # check if there's an initial quote, if so select till the ending quote
    json_str = ''
    if str[0] == JSON_QUOTE:
        str = str[1:]
    else:
        return None, str 
    
    for char in str:
        if char == JSON_QUOTE:
            return json_str, str[1:]
        else:
            json_str += char 
            str = str[1:]
    raise Exception("Expect EOL quote")
         

def lex_number(str):
    json_number = ''
    for c in str:
        if c in NUMBERS_LIST:
            json_number += c
            str = str[1:]
        else:
            break 
    if '.' in json_number:
        return float(json_number), str 
    if not json_number:
        return None, str 
    return int(json_number), str 

def lex_bool(str):
    if str[:4] == 'true':
        return True, str[4:]
    elif str[:5] == 'false':
        return False, str[5:]
    else:
        return None, str 

def lex_null(str):
    if str[:4] == 'null':
        return None, str[4:]
    else:
        return None, str 
