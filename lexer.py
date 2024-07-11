from parser import Token

def lexer(input_string):
    import re
    token_specification = [
        ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
        ('PLUS',     r'\+'),           # Addition operator
        ('MINUS',    r'-'),            # Subtraction operator
        ('MUL',      r'\*'),           # Multiplication operator
        ('DIV',      r'/'),            # Division operator
        ('LPAREN',   r'\('),           # Left parenthesis
        ('RPAREN',   r'\)'),           # Right parenthesis
        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH', r'.'),            # Any other character
    ]
    tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
    get_token = re.compile(tok_regex).match
    line = input_string
    mo = get_token(line)
    while mo is not None:
        typ = mo.lastgroup
        if typ != 'SKIP' and typ != 'MISMATCH':
            val = mo.group(typ)
            yield Token(typ, val)
        mo = get_token(line, mo.end())
    yield Token('EOF', '')