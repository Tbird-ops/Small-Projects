import random
import sys

# Pick a random word from a provided list
def pick_random_word(list):
    return random.choice(list)

# Get a code name made up of the number of words specified
def get_code_name(list, num_words, word):
    if num_words.isdigit() == False:
        return 'Error: incorrect argument provided. You must provide an integer.'
	#if word.isalpha() == False:
        #return "Error: incorrect argument given. You must provide a word!"
      
    num_words = int(num_words)
    code_name = ''
	
    code_name += word + ' '
    num_words -= 1
    
    for x in range(1,num_words+1):
        word = pick_random_word(list)
        code_name += word + ' '

    return code_name.rstrip()

# List of words to use
word_list = ['Aurora', 'Avalanche', 'Blizzard', 'Cyclone', 'Eagle', 'Edison', 'Frost', 'Hawk', 'Hexagon', 'Hornet', 'Medusa', 'Neptune', 'Orion', 'Osprey', 'Plato', 'Portal', 'Raven', 'Sand', 'Shadow', 'Storm', 'Sunset', 'Thunder', 'Vector', 'Vista', 'Vortex', 'Volcano']

if len(sys.argv) > 1:
    # Retrieve the command line argument
    words_to_pick = sys.argv[1]
    word_to_use = sys.argv[2]

    # Create a code name and print it to the screen
    code_name = get_code_name(word_list, words_to_pick, word_to_use)
    print(code_name)
else:
    print('Error: You must provide the number of words as an argument.')