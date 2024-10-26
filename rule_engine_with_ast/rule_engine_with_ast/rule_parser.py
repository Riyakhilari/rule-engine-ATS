# rule_parser.py

import re
from ast_node import Node

def parse_rule(rule_str):
    def create_operator_node(op, left, right):
        return Node(node_type="operator", value=op, left=left, right=right)

    def create_operand_node(condition):
        return Node(node_type="operand", value=condition)

    tokens = re.split(r"(\(|\)|AND|OR)", rule_str)
    tokens = [t.strip() for t in tokens if t.strip()]

    stack = []
    current_node = None

    for token in tokens:
        if token == "(":
            stack.append(current_node)
            current_node = None
        elif token == ")":
            child = current_node
            current_node = stack.pop()
            if current_node and isinstance(current_node, Node):
                if not current_node.left:
                    current_node.left = child
                else:
                    current_node.right = child
        elif token in ("AND", "OR"):
            current_node = create_operator_node(token, current_node, None)
        else:
            operand_node = create_operand_node(token)
            if not current_node:
                current_node = operand_node
            else:
                if not current_node.left:
                    current_node.left = operand_node
                else:
                    current_node.right = operand_node

    return current_node
