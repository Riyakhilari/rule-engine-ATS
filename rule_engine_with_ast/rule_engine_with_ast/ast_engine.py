class Node:
    def __init__(self, type, value=None, left=None, right=None):
        self.type = type  # 'operator' or 'operand'
        self.value = value  # 'AND', 'age > 30'
        self.left = left  # Left child node
        self.right = right  # Right child node

def create_rule(rule_string):
    
    if " AND " in rule_string:
        left_rule, right_rule = rule_string.split(" AND ")
        return Node(type='operator', value='AND',
                    left=create_rule(left_rule.strip()),
                    right=create_rule(right_rule.strip()))
    else:
        return Node(type='operand', value=rule_string.strip())

def evaluate_rule(ast, data):

    if ast.type == 'operator' and ast.value == 'AND':
        return (evaluate_rule(ast.left, data) and
                evaluate_rule(ast.right, data))
    return eval_operand(ast.value, data)

def eval_operand(condition, data):
    
    key, op, val = condition.split()
    val = int(val)
    if op == '>':
        return data[key] > val
    elif op == '<':
        return data[key] < val
    elif op == '==':
        return data[key] == val
    return False

def combine_rules(rules):
    
    if not rules:
        return None  

    
    root = Node(type='operator', value='AND')
    
    root.left = create_rule(rules[0])
    current = root  
    
    
    for rule in rules[1:]:
        
        new_node = create_rule(rule)
        current.right = new_node  
        current = new_node  
    
    return root
