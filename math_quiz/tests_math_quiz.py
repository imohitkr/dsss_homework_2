import unittest
from math_quiz import (
    generate_random_integer,
    generate_random_operator,
    evaluate_expression,
)


class TestMathGame(unittest.TestCase):
    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        for _ in range(1000):
            operator = generate_random_operator()
            self.assertIn(operator, ["+", "-", "*"])

    def test_evaluate_expression(self):
        test_cases = [
            (5, 2, "+", "5 + 2", 7),
            (7, 3, "-", "7 - 3", 4),
            (3, 4, "*", "3 * 4", 12),
            (10, 5, "+", "10 + 5", 15),
            (6, 2, "*", "6 * 2", 12),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = evaluate_expression(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
