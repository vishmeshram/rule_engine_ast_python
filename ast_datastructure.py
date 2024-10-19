class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type
        self.left = left
        self.right = right
        self.value = value

    def __repr__(self):
        return f"Node(type={self.type}, value={self.value})"

import ast
import operator

VALID_ATTRIBUTES = {'age', 'department', 'salary', 'experience'}
OPERATORS = {
    ast.And: operator.and_,
    ast.Or: operator.or_,
    ast.Gt: operator.gt,
    ast.Lt: operator.lt,
    ast.Eq: operator.eq
}

# Custom function
def is_senior(age):
    if age > 60:
        return True
    return False

# Validating the attributes
def validate_attributes(rule_ast):
    for node in ast.walk(rule_ast):
        if isinstance(node, ast.Name) and node.id not in VALID_ATTRIBUTES:
            raise ValueError(f"Invalid attribute used: {node.id}. Must be one of {VALID_ATTRIBUTES}")

# Creating the rule
def create_rule(rule_string):
    try:
        tree = ast.parse(rule_string, mode='eval')
        print(ast.dump(tree, indent=4))  # Print the AST structure for debugging
        # validate_attributes(tree)
        return tree
    except SyntaxError:
        raise ValueError("Invalid rule syntax. Please check the rule format.")


# Evaluating the expression
def eval_expr(node, data):
    if isinstance(node, ast.Call):  # Handling function calls like is_senior(age)
        func_name = node.func.id  # Get the function name
        if func_name == 'is_senior':  # Check if the function is is_senior
            arg_value = eval_expr(node.args[0], data)  # Evaluate the function argument (age)
            return is_senior(arg_value)  # Call the is_senior function with the evaluated argument
        else:
            raise ValueError(f"Undefined function: {func_name}")
    elif isinstance(node, ast.BoolOp):  # Handling AND, OR
        values = [eval_expr(value, data) for value in node.values]
        return all(values) if isinstance(node.op, ast.And) else any(values)
    elif isinstance(node, ast.Compare):  # Handling comparisons (like age > 30)
        left = eval_expr(node.left, data)
        right = eval_expr(node.comparators[0], data)
        return OPERATORS[type(node.ops[0])](left, right)
    elif isinstance(node, ast.Name):  # Handling variables like age
        return data[node.id]  # Get the value from the input data
    elif isinstance(node, ast.Constant):  # Handling constants like 30 or 'Sales'
        return node.value
    else:
        raise ValueError(f"Unsupported operation: {node}")



# Evaluating the rule
def evaluate_rule(rule_ast, data):
    return eval_expr(rule_ast.body, data)

# Combining rules
def combine_rules(rules):
    combined_rule = " or ".join(rules)
    return create_rule(combined_rule)
