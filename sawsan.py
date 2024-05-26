#question 1
#A
LI = ['HTTP', 'HTTPS', 'FTP', 'DNS']
L2 = [80, 443, 21, 53]
d = dict(zip(LI, L2))
print(d)

#B
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

x = int(input("Enter number for factorial: "))
print("factorial is :", factorial(x))

#C
L = ['Network', 'Bio', 'Programming', 'Physics', 'Music']
for item in L:
    if item.startswith('B'):
        print(item)

#D

d = {i: i+1 for i in range(11)}
print(d)

----------------------------------------
#question 2
def binary_to_decimal_alt(binary_str):
    """Converts a binary string to its equivalent decimal number using bitwise operations.

    Args:
        binary_str: The binary string to convert.

    Returns:
        The decimal equivalent of the binary string, or None if the input is invalid.

    Raises:
        ValueError: If the input string contains non-binary digits.
    """

    decimal_value = 0
    for i, digit in enumerate(reversed(binary_str)):
        if digit not in '01':
            raise ValueError("Invalid binary number: Input contains non-binary digits.")

        # Convert binary digit to integer
        digit_int = int(digit)

        # Calculate decimal contribution using bitwise operations
        decimal_value += digit_int << i

    return decimal_value

if __name__ == "__main__":
    while True:
        try:
            binary_str = input("Enter a binary number (or 'sawsan' to quit): ")

            if binary_str.lower() == 'q':
                break

            decimal_value = binary_to_decimal_alt(binary_str)
            print("The decimal equivalent of", binary_str, "is", decimal_value)
        except ValueError as e:
            print(e)
-----------------------------------------------------
#question 3

import json

def load_quiz(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def take_quiz(questions):
    score = 0
    for question in questions:
        print(question['question'])
        answer = input("Enter answer: ")
        if answer.lower() == question['answer'].lower():
            score += 1
    return score

#  'quiz.json' 
questions = load_quiz('quiz.json')
user_score = take_quiz(questions)
user_name = input("Enter your name: ")
with open ("result.csv","a") as file:
    file.write(f'{user_name},{user_score}')
print("result is:", user_score)
------------------------------------------------
#question 4
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f" deposit {amount}. balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("balance doesn’t enough ")
        else:
            self.balance -= amount
            print(f" withdraw {amount}. balance is {self.balance}")

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate, balance=0.0):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f" apply interest {self.interest_rate}. balance is{self.balance}")

account = SavingsAccount('12345', 'sawsan', 0.05)
account.deposit(1000)
account.withdraw(500)
account.apply_interest()
