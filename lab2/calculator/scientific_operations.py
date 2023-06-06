import math


def scientific_calculate(operation, num1):
    """
    Performs the given scientific operation on the given number, which may be either an integer or a float.

    args:
        - operation: the operation to perform (sin, cos, tan, ln)
        - num1: the number to perform the operation on

    returns:
        - the result of the operation on the given number
    """

    if operation == 'sin':
        return math.sin(num1)

    elif operation == 'cos':
        # TODO 4: finish this statement
        # - should return the cosine of num1
        pass  # Replace this line with your code

    elif operation == 'tan':
        # TODO 5: finish this statement
        # - should return the tangent of num1
        pass  # Replace this line with your code

    elif operation == 'ln':
        # TODO 6: finish this statement
        # - should return the natural log of num1
        pass  # Replace this line with your code

    else:
        raise ValueError(
            'Invalid Operation: Scientific Operations are (sin, cos, tan, ln, sqrt, !, ^, and %)')
