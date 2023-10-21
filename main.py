import random
import nltk
nltk.download("words")

from nltk.corpus import words

# Get a list of English words
english_words = words.words()

# Generate a random word
random_word = random.choice(english_words)
check_word=[]
for i in range(len(random_word)):
	check_word.append("_")
	
print(check_word)

random_word = random_word.lower()
incorrect_letters = []
your_heart = 10
while True:
	# Ask the user to guess letters of the word
	print(f"You have {your_heart} heart")
	guess = input("Guess a letter: ").lower()
	if("".join(check_word)==random_word):
		print("You win!")
		print("".join(check_word))

		break
	
	# Check if the guess is correct
	if guess in random_word:
		if(guess not in check_word):
			print("Correct!")
			indexes_of_word = []
			for index, letter in enumerate(random_word):
				if letter == guess:
					indexes_of_word.append(index)
			for indexes in indexes_of_word:
				check_word[indexes] = guess
			print("".join(check_word))
			print(indexes_of_word)
			# print(random_word)
			
		else:
			print("You wrote it")
		
	else:
		print("Incorrect!")
		print("".join(check_word))
		your_heart -= 1
		print("You have",your_heart,"heart")
		if(guess not in incorrect_letters):
			incorrect_letters.append(guess+" ")
		print("Incorrect letters:","".join(incorrect_letters))
	
		
	if("_" in check_word):
		print("Press enter button when you found all letters")
		# Replace the underscores with the correct letters
	if(your_heart == 0):
		print("You lose!")
		print("The word was",random_word)
		break

print(random_word)
