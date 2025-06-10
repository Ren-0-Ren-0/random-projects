import random
sample_words = [
    "apple", "bread", "crane", "drink", "eagle", "flame", "grape", "house", "image", "jelly",
    "knock", "lemon", "mango", "noble", "ocean", "piano", "queen", "radio", "snake", "table",
    "umbra", "vivid", "whale", "xenon", "yacht", "zebra", "aloof", "brave", "charm", "dealt",
    "epoch", "fable", "gloom", "haste", "ideal", "jumps", "karma", "latch", "mirth", "noisy",
    "optic", "pride", "quiet", "rival", "sling", "trunk", "urban", "vapor", "wrist", "yield",
    "zonal", "angry", "bliss", "climb", "drove", "ember", "feast", "glory", "honor", "input",
    "joist", "kites", "lunar", "meaty", "niche", "onset", "picky", "quirk", "risky", "sassy",
    "tense", "unite", "vigor", "weary", "xerox", "young", "zesty", "adore", "blame", "cabin",
    "debut", "eager", "facet", "gamer", "haunt", "inlet", "jazzy", "kneel", "liver", "mince",
    "abide", "baker", "cider", "dodge", "evoke", "frost", "glide", "harsh", "inbox", "joint",
    "kudos", "laden", "motel", "novel", "oxide", "prank", "quail", "reign", "shard", "tango",
    "unzip", "vowel", "wrath", "xenon", "youth", "zonal", "aptly", "brisk", "comet", "diver",
    "eject", "faint", "grind", "honey", "icily", "joust", "kneel", "laced", "moist", "nudge",
    "orbit", "plant", "quirk", "rhyme", "slant", "throb", "utter", "vault", "woven", "xerox",
    "yodel", "zebra", "amble", "bloom", "chant", "daisy", "elite", "frank", "gorge", "hinge",
    "ideal", "jaunt", "kinky", "latch", "mirth", "nerdy", "omega", "perch", "quest", "rough",
    "siren", "thief", "upper", "vixen", "wiser", "xylem", "yummy", "zesty", "adore", "beach",
    "charm", "drown", "enjoy", "fable", "gamer", "haiku", "inlet", "jelly", "karma", "loyal"    
]

def choose_word():
    random_number = random.randint(0, len(sample_words) - 1)
    return sample_words[random_number]

def validate_input_letter(letter1):
    if len(letter1) != 1 or not letter1.isalpha():
        return False
    return True

def validate_letter_in_word(letter2, word):
    return letter2 in word

def main():
    chosen_word = choose_word()
    
    print("Welcome to the Word Guessing Game!")
    print("Try to guess the word by entering one letter at a time.")
    print("The word has 5 letters.")
    print("Good luck!\n")
    guessed_letters = []
    attempts = 10
    print(" _ _ _ _ _ ")
    while attempts > 0:
        print(f"Attempts left: {attempts}")
        guess = input("Enter a letter: ").lower()
        
        if not validate_input_letter(guess):
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        guessed_letters.append(guess)
        
        if validate_letter_in_word(guess, chosen_word):
            print(f"Good guess! '{guess}' is in the word.")
            # Display guessed letters
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1
        print("Guessed letters so far:", ' '.join(guessed_letters))
        
        # Display current state of guessed letters
        display_word = ' '.join([letter if letter in guessed_letters else '_' for letter in chosen_word])
        print("Current word:", display_word)
        
        if '_' not in display_word:
            print("Congratulations! You've guessed the word:", chosen_word)
            break
    else:
        print("Game over! The word was:", chosen_word)
    
main()
# This code implements a simple word guessing game where the player has to guess a randomly chosen 5-letter word by entering one letter at a time.  


