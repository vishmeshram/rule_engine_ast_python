from flask import Flask, request, jsonify, render_template
from ast_datastructure import create_rule, evaluate_rule

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    rule_string = request.json['rule']
    rule_ast = create_rule(rule_string)
    return jsonify({'rule_ast': str(rule_ast)})

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    try:
        rule_string = request.json['rule']  # Get the rule as a string
        user_data = request.json['data']  # Get the data as JSON
        
        # Log the incoming rule and data for debugging
        print(f"Rule: {rule_string}")
        print(f"Data: {user_data}")
        
        rule_ast = create_rule(rule_string)  # Parse the rule into an AST
        print(f"AST: {rule_ast}")  # Log the parsed AST for debugging
        
        result = evaluate_rule(rule_ast, user_data)  # Evaluate the AST against data
        print(f"Evaluation Result: {result}")  # Log the evaluation result
        
        return jsonify({'result': result})  # Return the evaluation result (True/False)
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")  # Log any error for debugging
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
