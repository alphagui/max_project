import itertools
from fractions import Fraction


def find_max_value(numbers):
    max_value = 0
    max_expression = ""

    # Generate all permutations of the 5 numbers
    for nums in itertools.permutations(numbers):
        # Generate all possible operator combinations
        for ops in itertools.product(['+', '-', '*', '/'], repeat=4):
            # Generate all possible ways to place parentheses
            # We'll consider different ways to group operations

            # No parentheses: a op1 b op2 c op3 d op4 e
            expressions = []

            # Try all possible groupings with parentheses
            # Representation 1: ((((a op1 b) op2 c) op3 d) op4 e)
            exp1 = f"(((({nums[0]} {ops[0]} {nums[1]}) {ops[1]} {nums[2]}) {ops[2]} {nums[3]}) {ops[3]} {nums[4]})"
            expressions.append(exp1)

            # Representation 2: (((a op1 b) op2 c) op3 (d op4 e))
            exp2 = f"((({nums[0]} {ops[0]} {nums[1]}) {ops[1]} {nums[2]}) {ops[2]} ({nums[3]} {ops[3]} {nums[4]}))"
            expressions.append(exp2)

            # Representation 3: ((a op1 b) op2 ((c op3 d) op4 e))
            exp3 = f"(({nums[0]} {ops[0]} {nums[1]}) {ops[1]} (({nums[2]} {ops[2]} {nums[3]}) {ops[3]} {nums[4]}))"
            expressions.append(exp3)

            # Representation 4: ((a op1 (b op2 c)) op3 (d op4 e))
            exp4 = f"(({nums[0]} {ops[0]} ({nums[1]} {ops[1]} {nums[2]})) {ops[2]} ({nums[3]} {ops[3]} {nums[4]}))"
            expressions.append(exp4)

            # Representation 5: (a op1 ((b op2 c) op3 (d op4 e)))
            exp5 = f"({nums[0]} {ops[0]} (({nums[1]} {ops[1]} {nums[2]}) {ops[2]} ({nums[3]} {ops[3]} {nums[4]})))"
            expressions.append(exp5)

            for expr in expressions:
                try:
                    # Use Fraction to handle division properly
                    result = eval(expr, {"__builtins__": {}}, {"Fraction": Fraction})

                    # Check if result is an integer
                    if isinstance(result, Fraction):
                        if result.denominator == 1 and 0 <= result <= 100:
                            int_result = int(result)
                            if int_result > max_value:
                                max_value = int_result
                                max_expression = expr
                    elif isinstance(result, int) and 0 <= result <= 100:
                        if result > max_value:
                            max_value = result
                            max_expression = expr
                except (ZeroDivisionError, ValueError, SyntaxError):
                    continue

    return max_value, max_expression


