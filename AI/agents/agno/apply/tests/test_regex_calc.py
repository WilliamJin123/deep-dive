import re
import math

def calculate(expression):
    print(f"Original: {expression}")
    # Preprocess the expression to handle e-notation (e.g., e5 -> 1e5)
    expression = re.sub(r'\b([eE])(\d+)\b', r'1\1\2', expression)
    print(f"After regex: {expression}")
    # Replace ^ with ** for power
    expression = expression.replace('^', '**')
    print(f"After replace: {expression}")

    # Define a safe dictionary of allowed names
    allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    allowed_names.update({"abs": abs, "round": round, "ln": math.log})
    
    try:
        # Compile the expression to code object
        code = compile(expression, "<string>", "eval")
        
        # Check for disallowed names in the expression to prevent unsafe execution
        for name in code.co_names:
            if name not in allowed_names:
                raise NameError(f"Use of '{name}' is not allowed")
        
        # Evaluate the expression
        result = eval(code, {"__builtins__": {}}, allowed_names)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

print(f"Result: {calculate('ln(e^5)')}")
