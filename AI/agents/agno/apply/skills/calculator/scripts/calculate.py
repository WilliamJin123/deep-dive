import sys
import math
import argparse

def calculate(expression):
    # Define a safe dictionary of allowed names
    allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    allowed_names.update({"abs": abs, "round": round})
    
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate a math expression.")
    parser.add_argument("expression", type=str, help="The math expression to evaluate")
    args = parser.parse_args()
    
    print(calculate(args.expression))
