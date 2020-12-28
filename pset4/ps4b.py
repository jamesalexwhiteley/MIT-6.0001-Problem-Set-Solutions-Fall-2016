import string

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

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


word_list = load_words('words.txt')





class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object       
        text (string): the message's text
        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text 
        self.valid_words = load_words('words.txt')

    def get_message_text(self):
        return self.message_text 

    def get_valid_words(self):
        return self.valid_words

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that applies a cipher to a letter.

        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by k, where 0 <= k < 26

        The dictionary has 52 keys (all the uppercase letters and 
        all the lowercase letters)      

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        def shift_alphabet(alphabet,shift): 

            position = 0
            shift_dictionary = {}

            if shift > 26:
                shift = shift % 26

            for letter in alphabet:
                if position + shift > (len(alphabet)-1):
                    shift -= (shift + position)
                shift_dictionary.update( {letter : alphabet[position + shift]} )
                position += 1

            return shift_dictionary

        lower_shift_dictionary = shift_alphabet('abcdefghijklmnopqrstuvwxyz',shift)
        upper_shift_dictionary = shift_alphabet('ABCDEFGHIJKLMNOPQRSTUVWXYZ',shift)
        complete_shifted_dictionary = dict(lower_shift_dictionary, ** upper_shift_dictionary)   

        return complete_shifted_dictionary           


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        message_text = self.get_message_text() 

        string = ''
        for letter in message_text:
            if letter == ' ' or letter == ',' or letter == '.':
                string = string + letter
            else:
                string = string + self.build_shift_dict(shift)[letter]
  
        return string





class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift 
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        return self.shift 

    def get_encryption_dict(self):
        return self.encryption_dict

    def get_message_text_encrypted(self):
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)



class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        store = []
        self.message_text
        for i in range(0,26):
            sentence = self.apply_shift(i)
            for word in sentence.split():
                if is_word(word_list, word) == True:                  
                    store.append(i)

        key = max(set(store), key = store.count)
        text = self.apply_shift(key)
        return (key,text)

        

if __name__ == '__main__':

   #Example test case (PlaintextMessage)
   plaintext = PlaintextMessage('hello', 2)
   print('Expected Output: jgnnq')
   print('Actual Output:', plaintext.get_message_text_encrypted())

   #Example test case (CiphertextMessage)
   ciphertext = CiphertextMessage('jgnnq')
   print('Expected Output:', (24, 'hello'))
   print('Actual Output:', ciphertext.decrypt_message())
   

print()
encoded_message = get_story_string()
print(encoded_message)

print()
ctm = CiphertextMessage(encoded_message)
print(ctm.decrypt_message())






