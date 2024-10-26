# tests/test_ast_engine.py

from ast_engine import create_rule, evaluate_rule, combine_rules, Node

def test_create_rule():
    rule = "age > 30 AND salary > 50000"
    ast = create_rule(rule)
    assert ast.type == "operator"
    assert ast.value == "AND"
    assert ast.left.value == "age > 30"
    assert ast.right.value == "salary > 50000"

def test_evaluate_rule():
    rule = "age > 30"
    ast = create_rule(rule)
    data = {"age": 35}
    assert evaluate_rule(ast, data) == True

def test_combine_rules():
    rule1 = "age > 30"
    rule2 = "salary > 50000"
    combined_ast = combine_rules([rule1, rule2])
    assert combined_ast.type == "operator"
    assert combined_ast.value == "AND"

    data = {"age": 35, "salary": 60000}
    assert evaluate_rule(combined_ast, data) == True

    data = {"age": 25, "salary": 60000}
    assert evaluate_rule(combined_ast, data) == False
