import random

words = ['father', 'enterprise', 'science', 'programming', 'resistance', 'fiction', 'condition']
word = random.choice(words)

jumble = ''.join(random.sample(word, len(word)))

print(f"The Jumble word is {jumble}")
guess = input("Write your guess:")

if guess == word:
    print("correct")

else:
    print("wrong!")