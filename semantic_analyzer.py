class SemanticAnalyzer:
    def __init__(self, ast):
        self.ast = ast

    def analyze(self):
        self.visit(self.ast)

    def visit(self, node):
        method_name = 'visit_' + node.type.lower()
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        for child in node.children:
            self.visit(child)
        return node.data_type

    def visit_number(self, node):
        print(f"Visiting number node: {node.value} and node type is {node.type}")
        node.data_type = 'number'
        return node.data_type

    def visit_plus(self, node):
        print(f"Visiting plus node: {node.value}")
        return self.visit_binary_op(node)

    def visit_minus(self, node):
        print(f"Visiting minus node: {node.value}")
        return self.visit_binary_op(node)

    def visit_mul(self, node):
        print(f"Visiting mul node: {node.value}")
        return self.visit_binary_op(node)

    def visit_div(self, node):
        print(f"Visiting div node: {node.value}")
        return self.visit_division_op(node)

    def visit_binary_op(self, node):
        print(f"Visiting binary_op node: {node.value}")
        left_type = self.visit(node.children[0])
        right_type = self.visit(node.children[1])
        print(f"The type of the first child is {left_type} the type of the second child is {right_type}.")
        if left_type != 'number' or right_type != 'number':
            raise Exception(f"Type error: {left_type} {node.type} {right_type}")
        node.data_type = 'number'
        return node.data_type
    
    def visit_division_op(self, node):
        print(f"Visiting division_op node: {node.type}")
        left_type = self.visit(node.children[0])
        right_type = self.visit(node.children[1])
        print(f"The type of the first child is {left_type}, the type of the second child is {right_type}.")
        if left_type != 'number' or right_type != 'number':
            raise Exception(f"Type error: {left_type} {node.type} {right_type}")
        if node.children[1].type == 'NUMBER' and node.children[1].value == '0':
            raise Exception("Semantic error: Division by zero")
        node.data_type = 'number'
        return node.data_type

