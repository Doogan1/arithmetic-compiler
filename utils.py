import networkx as nx

def print_ast(node, level=0):
    print('  ' * level + f"{node.type}: {node.value}")
    for child in node.children:
        print_ast(child, level + 1)

def ast_to_networkx(ast):
    g = nx.DiGraph()
    positions = {}
    current_level = {0: 0}
    
    def add_edges(node, parent_id=None, level=0):
        node_id = id(node)
        g.add_node(node_id, type=node.type, value=node.value)
        if parent_id is not None:
            g.add_edge(parent_id, node_id)
        
        if level in current_level:
            positions[node_id] = (current_level[level], -level)
            current_level[level] += 1
        else:
            current_level[level] = 1
            positions[node_id] = (0, -level)

        for child in node.children:
            add_edges(child, node_id, level + 1)

    add_edges(ast)
    return g, positions