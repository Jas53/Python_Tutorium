def calculate(nr_1:int = 1, nr_2:int = 1, operator:str = '+'):
    """add, sub, mulitply or divide two numbers
    
    Params:
        nr_1 (int): first number
        nr_2 (int): second number
        operator (string): the operator (+, -, * or /)
    
    Return:
        result or error
    """
    if operator == '+':
        return nr_1 + nr_2
    elif operator == '-':
        return nr_1 - nr_2
    elif operator == '*':
        return nr_1 * nr_2
    elif operator == '/':
        return nr_1 / nr_2
    return "Failed to identify the operator.\nPlease enter '+', '-', '*' or '/' as operator"