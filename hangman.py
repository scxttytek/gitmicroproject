import random

def get_word(category):
    words = {
        "animals": ["elephant", "giraffe", "penguin", "dolphin", "butterfly"],
        "programming": ["python", "function", "variable", "algorithm", "database"],
        "colors": ["purple", "orange", "violet", "magenta", "turquoise"],
        "space": ["galaxy", "asteroid", "nebula", "supernova", "telescope"]
    }
    return random.choice(words[category])

def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |      
           |      
           |     
           -
        """
    ]
    return stages[tries]

def display_board(tries, guessed_letters, word):
    print()
    print("=" * 50)
    print("          H A N G M A N")
    print("=" * 50)
    print()
    print(display_hangman(tries))
    print()
    
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("Word: " + display_word)
    print()
    print("Guessed: " + " ".join(sorted(guessed_letters)))
    print()

def play_game():
    categories = ["animals", "programming", "colors", "space"]
    print("Choose a category:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat.capitalize()}")
    
    choice = int(input("\nEnter number: ")) - 1
    category = categories[choice]
    word = get_word(category)
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    guessed_letters = set()
    tries = 6
    
    print(f"\nCategory: {category.capitalize()}")
    print("You have 6 tries!")
    input("Press Enter to start...")
    
    while len(word_letters) > 0 and tries > 0:
        display_board(tries, guessed_letters, word)
        guess = input("Guess a letter: ").lower()
        
        if guess in alphabet - guessed_letters:
            guessed_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
                print(f"Good! '{guess}' is in the word!")
            else:
                tries -= 1
                print(f"Sorry! '{guess}' is not in the word.")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'!")
        else:
            print("Invalid input!")
        
        input("Press Enter...")
    
    display_board(tries, guessed_letters, word)
    
    if tries == 0:
        print(f"Game Over! The word was: {word}")
    else:
        print(f"You won! Word: {word}")
    print()

def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
