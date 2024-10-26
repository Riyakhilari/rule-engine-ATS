# ast_node.py

class ASTNode:
    def __init__(self, type, value, left=None, right=None):
        self.type = type  # 'operator' or 'operand'
        self.value = value  # 'AND', 'OR', or comparison expressions
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node(type={self.type}, value={self.value})"
