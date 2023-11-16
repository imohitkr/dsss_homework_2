import random


def generate_random_integer(min, max):
    """
    Generate a random integer between min and max (inclusive).

    Args:
        min (int): The minimum value of the range.
        max (int): The maximum value of the range.

    Returns:
        int: A random integer between min and max (inclusive).
    """
    return random.randint(min, max)


def generate_random_operator():
    """
    This function returns a random arithmetic operator from the list ['+', '-', '*'].
    """
    return random.choice(["+", "-", "*"])


def evaluate_expression(num1, num2, operator):
    """
    Evaluates a mathematical expression consisting of two numbers and an operator.

    Args:
        num1 (int): The first number in the expression.
        num2 (int): The second number in the expression.
        operator (str): The operator to apply to the two numbers. Can be "+", "-", or "*".

    Returns:
        tuple: A tuple containing the original problem as a string and the answer as an integer.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem, answer


def math_quiz():
    """
    This function presents the user with a math quiz game consisting of three questions.
    For each question, the function generates two random integers and a random operator,
    and asks the user to evaluate the expression. The user's score is displayed at the end.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print(
        "You will be presented with math problems, and you need to provide the correct answers."
    )

    for _ in range(total_questions):
        # Generate two random integers and a random operator
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        # Evaluate the expression and ask the user for their answer
        problem, answer = evaluate_expression(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        user_answer = input("Your answer: ")
        try:
            user_answer = int(user_answer)
            # Check if the user's answer is correct and update the score
            if user_answer == answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {answer}.")
        except ValueError:
            print("Invalid input")

    # Display the user's score
    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
