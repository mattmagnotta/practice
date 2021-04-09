import random

print("hello, welcome to magic 8 ball.")
User_input = input("what is your question for the ball?: ")

choices_list = [
                "It is certain",
                "It is decidedly so",
                "Without a doubt",
                "Yes definitely",
                "You may rely on it",
]

print(random.choice(choices_list))
