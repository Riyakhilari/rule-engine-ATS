# evaluator.py

import re
from ast_node import Node

def evaluate_rule(node, data):
    if node.type == "operand":
        key, operator, value = re.split(r"\s*([<>=]+)\s*", node.value)
        value = int(value) if value.isdigit() else value.strip("'")

        data_value = data.get(key)
        result = False

        if operator == ">":
            result = data_value > value
        elif operator == "<":
            result = data_value < value
        elif operator == "=":
            result = data_value == value

        print(f"Evaluating: {key} {operator} {value} with data value {data_value} -> {result}")
        return result

    elif node.type == "operator":
        left_result = evaluate_rule(node.left, data) if node.left else False
        right_result = evaluate_rule(node.right, data) if node.right else False

        print(f"Operator {node.value}: left_result = {left_result}, right_result = {right_result}")

        if node.value == "AND":
            final_result = left_result and right_result
            print(f"AND operation: {left_result} AND {right_result} -> {final_result}")
            return final_result
        elif node.value == "OR":
            final_result = left_result or right_result
            print(f"OR operation: {left_result} OR {right_result} -> {final_result}")
            return final_result

    return False
