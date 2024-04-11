# List Slicing

mixture = [1, 2, 3, "one", "two", "three"]
print(mixture)

print(mixture[1:3]) # This will return [2, 3]
print(mixture[::3]) # Returns every third result in the list


original_word = "recommendation"
scrambled_word = "noittadnemmocer"

hint1_slice = original_word[4:6] # The 5th and 6th letters
hint2_slice = original_word[-3:] # Last 3 letters
hint3_slice = original_word[7:10] # 8th-10th letters
hint4_slice = original_word[:2] # first 2 letters are

print("Scrambled word: ", scrambled_word)
print("Guess the original word")
print("Here are some hints: ")

print("Hint 1: The 5th and 6th letters are: ", hint1_slice)
print("Hint 2: The last 3 letters are: ", hint2_slice)
print("Hint 3: The 8th, 9th and 10th letters are: ", hint3_slice)
print("Hint 4: The first 2 letters are: ", hint4_slice)

print("What's your guess?")
user_guess = input()
if user_guess == original_word:
    print("That's correct")
else:
    print("Sorry, that's not correct, please play again")