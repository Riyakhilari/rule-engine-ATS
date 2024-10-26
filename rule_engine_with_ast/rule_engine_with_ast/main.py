# main.py

from ast_node import ASTNode

def parse_rule_to_ast(rule):
    """Parses a rule string into an AST."""
    tokens = rule.split()

    if "AND" in tokens:
        operator_index = tokens.index("AND")
        left_expr = " ".join(tokens[:operator_index])
        right_expr = " ".join(tokens[operator_index + 1:])
        return ASTNode("operator", "AND",
                       left=ASTNode("operand", left_expr),
                       right=ASTNode("operand", right_expr))

    elif "OR" in tokens:
        operator_index = tokens.index("OR")
        left_expr = " ".join(tokens[:operator_index])
        right_expr = " ".join(tokens[operator_index + 1:])
        return ASTNode("operator", "OR",
                       left=ASTNode("operand", left_expr),
                       right=ASTNode("operand", right_expr))

    return ASTNode("operand", rule)

def evaluate_rule(node, data):
    """Evaluates the AST based on provided data."""
    if node.type == "operand":
        var, op, value = node.value.split()
        data_value = data.get(var)

        if op == '>':
            return data_value > int(value)
        elif op == '<':
            return data_value < int(value)
        elif op == '=':
            return data_value == value.strip("'")

    elif node.type == "operator":
        left_result = evaluate_rule(node.left, data)
        right_result = evaluate_rule(node.right, data)

        if node.value == "AND":
            return left_result and right_result
        elif node.value == "OR":
            return left_result or right_result

    return False

# Example rules
rule1 = "salary > 50000 AND experience > 5"

ast_root = parse_rule_to_ast(rule1)

def print_ast(node, indent=0):
    if node is None:
        return
    print('  ' * indent + f"Node(type={node.type}, value={node.value})")
    if node.left:
        print_ast(node.left, indent + 1)
    if node.right:
        print_ast(node.right, indent + 1)

print("AST for rule 1:")
print_ast(ast_root)

data = {"salary": 60000, "experience": 6}

result = evaluate_rule(ast_root, data)
print(f"Evaluation result for rule 1: {result}")
