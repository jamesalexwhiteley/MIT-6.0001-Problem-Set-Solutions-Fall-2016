import string
import random as rs
from ps4a import permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text 
        self.valid_words = load_words('words.txt')
    
    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        def build_dictionary(alphabet):
            pos = 0
            transpose_dict = {}
            for i in list(alphabet):
                transpose_dict.update({key: i for key in list(alphabet)[pos]})
                pos += 1 
            return transpose_dict

        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        transpose_dict = build_dictionary(alphabet)

        def replace_vowels(transpose_dict, vowels, vowels_permutation):
            pos = 0
            for letter in vowels:
                transpose_dict[letter] = vowels_permutation[pos]
                pos += 1 
            return transpose_dict

        replace_vowels(transpose_dict, VOWELS_LOWER, vowels_permutation)
        replace_vowels(transpose_dict, VOWELS_UPPER, vowels_permutation.upper())

        return transpose_dict

    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        transposed_word = ''
        exceptions = ' ,.!:0123456789-'
        for letter in self.message_text:
            if letter in exceptions:
                transposed_word += letter
            else:
                transposed_word += transpose_dict[letter]
        return transposed_word

        



class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        encoded_message = self.get_message_text()
        # print(self.get_valid_words())


        store = []
        for permutation in permutations('aeiou'):
            transpose_dict = self.build_transpose_dict(permutation)
            sentence = self.apply_transpose(transpose_dict)
            for word in sentence.split(' '):
                if is_word(self.valid_words, word) == True:
                    store.append(permutation)

        key = max(set(store), key = store.count)
        transpose_dict = self.build_transpose_dict(key)
        message = self.apply_transpose(transpose_dict)
        
        return message


if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), '.', "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    print()

    # Test case No. 2 
    message = SubMessage("Ah must be a valid word")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), '.', "Permutation:", permutation)
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())

    # Test case No. 3 
    message = SubMessage("Guttag, John. Introduction to Computation and Programming Using Python: With Application to Understanding Data Second Edition. MIT Press, 2016. ISBN: 9780262529624. The book and the course lectures parallel each other, though there is more detail in the book about some topics. It is available both in hard copy and as an e-book.")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), '.', "Permutation:", permutation)
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())




# new_vowel_list = 'eaiuo'

# message = SubMessage('A new toy')
# transpose_dict = message.build_transpose_dict(new_vowel_list)
# encrypted_message = message.apply_transpose(transpose_dict)

# print(EncryptedSubMessage(encrypted_message).decrypt_message())