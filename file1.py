from WordFile import *

while guess != input_string:
    # I didn't know how else to start everything up other than with an input function
    guess = random.choice(Convert(characters)).upper() + random.choice(Convert(characters)).upper() + random.choice(Convert(characters)).upper()
    attempts += 1
    if guess in three_letter_words.upper():
        # If the generated word is an actual word, print it and log it as "actual word"
        print(guess)
        actual_words += 1
    if attempts == 1000000:
    # 1 million generated strings
        print(f"{attempts} random strings generated, {actual_words} 3-letter words produced.")
        break
print("\n" + conclusion)
