import networkx as nx

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class ASTNode:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
        self.children = []

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        return self.expression()

    def eat(self, token_type):
        if self.tokens[self.pos].type == token_type:
            self.pos += 1
        else:
            raise Exception(f"Expected token {token_type}, got {self.tokens[self.pos].type}")

    def expression(self):
        node = self.term()
        while self.pos < len(self.tokens) and self.tokens[self.pos].type in ('PLUS', 'MINUS'):
            token = self.tokens[self.pos]
            if token.type == 'PLUS':
                self.eat('PLUS')
            elif token.type == 'MINUS':
                self.eat('MINUS')
            new_node = ASTNode(token.type)
            new_node.children.append(node)
            new_node.children.append(self.term())
            node = new_node
        return node

    def term(self):
        node = self.factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos].type in ('MUL', 'DIV'):
            token = self.tokens[self.pos]
            if token.type == 'MUL':
                self.eat('MUL')
            elif token.type == 'DIV':
                self.eat('DIV')
            new_node = ASTNode(token.type)
            new_node.children.append(node)
            new_node.children.append(self.factor())
            node = new_node
        return node

    def factor(self):
        token = self.tokens[self.pos]
        if token.type == 'NUMBER':
            self.eat('NUMBER')
            return ASTNode('NUMBER', token.value)
        elif token.type == 'LPAREN':
            self.eat('LPAREN')
            node = self.expression()
            self.eat('RPAREN')
            return node
        else:
            raise Exception(f"Unexpected token {token.type}")
