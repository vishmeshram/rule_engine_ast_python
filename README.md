#Rule Engine using Abstract Syntax Tree (AST)
##Overview
This project is a simple Rule Engine that uses Python's Abstract Syntax Tree (AST) to dynamically evaluate rules based on user data. The application consists of a Flask-based web interface where users can enter rules and data to determine eligibility or other conditions using custom logic.

##Features
Parse and evaluate logical rules dynamically.
Supports basic logical operators (and, or, >, <, ==).
Custom functions, such as is_senior(age), can be included in the rules.
Simple user interface to input rules and data in JSON format.
Validates the syntax and attributes used in rules.
Provides feedback on evaluation results (True/False).

##Technologies Used
Python (AST for rule parsing and evaluation)
Flask (Web framework for serving the UI and API endpoints)
HTML + JavaScript (Frontend interface)

##Installation and Setup
###Prerequisites
Make sure you have Python 3.7+ installed on your machine.

###Steps to Run Locally
Clone the Repository:


git clone https://github.com/yourusername/rule-engine-ast.git
cd rule-engine-ast
Create and Activate a Virtual Environment:


python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install Required Dependencies: Install the necessary dependencies from requirements.txt:

pip install -r requirements.txt
Run the Flask Application: Start the Flask development server:

###bash
Copy code
python app.py
Open the Application in Your Browser: Open your browser and go to http://127.0.0.1:5000/ to access the UI.

###Usage
Enter a Rule
In the "Enter Rule" field, enter a logical rule using Python syntax:

Example Rule: age > 30 and department == 'Sales'
Enter the corresponding data in the "Enter Data (as JSON)" field:

Example Data:
json
Copy code
{
    "age": 35,
    "department": "Sales",
    "salary": 60000
}
Click Submit to evaluate the rule against the provided data. The result (True or False) will be displayed.

Example Rule and Data
Rule: age > 30 and department == 'Sales'
Data:
json
Copy code
{
    "age": 35,
    "department": "Sales"
}
The rule evaluates to True because the age is greater than 30 and the department is 'Sales'.



##File Structure

/rule-engine-ast
├── app.py                  # Main Flask application
├── ast_datastructure.py     # Logic for AST parsing and rule evaluation
├── test_ast.py              # Test cases for AST and rule evaluation
├── templates
│   └── index.html           # Simple UI for rule input and result display
├── requirements.txt         # List of dependencies
└── README.md                # Project documentation

##Running Tests
To run the test cases for rule creation and evaluation, run the test_ast.py file:


##python test_ast.py
This will test if the rule engine is working correctly by creating rules and evaluating them against sample data.

##Known Issues
The current implementation supports only basic logical operators and simple custom functions. More complex rule structures can be added in future versions.
Ensure that the rule syntax follows Python's logical operator format (and, or, ==).
Contributing
If you’d like to contribute to this project, feel free to submit a pull request. Please include detailed descriptions of your changes.
