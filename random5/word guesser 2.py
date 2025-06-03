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

#def main():
    
def select_random_words(word_list, count=10):
    return random.sample(word_list, count)

def printformat(word="_____"):
    print(word.split(sep="").join(" "))
    

def take_5_letter_word_input(prompt="Please enter your guess: "):
    while True:
        try:
            word = input(prompt).strip().lower()
            if len(word) == 5 and word.isalpha():
                word.split()
                return word
            else:
                print("Invalid input. Please enter a 5-letter word.")
        except EOFError:
            print("Invalid input. Please enter a 5 alphabet letters with no spaces, numbers or special characters.")
#main()