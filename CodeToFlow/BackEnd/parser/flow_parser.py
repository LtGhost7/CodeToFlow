# backend/parser/flow_parser.py

import ast

def parse_python_code(code):
    try:
        tree = ast.parse(code)
        # Basic structure for now
        result = []

        for node in ast.walk(tree):
            if isinstance(node, ast.If):
                result.append({'type': 'decision', 'text': 'if condition'})
            elif isinstance(node, ast.For):
                result.append({'type': 'loop', 'text': 'for loop'})
            elif isinstance(node, ast.While):
                result.append({'type': 'loop', 'text': 'while loop'})
            elif isinstance(node, ast.FunctionDef):
                result.append({'type': 'function', 'text': f'function {node.name}'})
            elif isinstance(node, ast.Assign):
                result.append({'type': 'process', 'text': 'assignment'})
            elif isinstance(node, ast.Expr):
                result.append({'type': 'expression', 'text': 'expression'})

        return result

    except Exception as e:
        return [{'error': str(e)}]
