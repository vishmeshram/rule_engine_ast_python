import ast
from ast_datastructure import create_rule, evaluate_rule

# Test data
data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}

# Sample rules
rule_string = "age > 30 and department == 'Sales'"

def test_create_rule():
    try:
        rule_ast = create_rule(rule_string)
        print("AST created successfully!")
        print(rule_ast)
    except Exception as e:
        print(f"Error creating AST: {e}")

def test_evaluate_rule():
    try:
        rule_ast = create_rule(rule_string)
        result = evaluate_rule(rule_ast, data)
        print(f"Rule Evaluation Result: {result}")
    except Exception as e:
        print(f"Error evaluating rule: {e}")

if __name__ == "__main__":
    test_create_rule()
    test_evaluate_rule()
    

