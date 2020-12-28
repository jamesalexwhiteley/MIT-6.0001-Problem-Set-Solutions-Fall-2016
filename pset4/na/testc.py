# import random as rs

# print(rs.random())

# def build_dictionary(alphabet):
#             pos = 0
#             dictionary = {}
#             for i in list(alphabet):
#                 dictionary.update({key: i for key in list(alphabet)[pos]})
#                 pos += 1 

#             return dictionary


# alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
# dictionary = build_dictionary(alphabet)


# dictionary = {'A': 1,'B': 2,'C': 3}

# letters = list('ABC')
# permutation = list('CBA')

# pos = 0
# for letter in letters:
# 	dictionary[letter] = permutation[pos]
# 	print(permutation[0])
# 	pos += 1 

# print(dictionary)


# for i in dictionary.keys():
# 	print(i)


# def load_words(file_name):
#     '''
#     file_name (string): the name of the file containing 
#     the list of words to load    
    
#     Returns: a list of valid words. Words are strings of lowercase letters.
    
#     Depending on the size of the word list, this function may
#     take a while to finish.
#     '''
#     # inFile: file
#     inFile = open(file_name, 'r')
#     # wordlist: list of strings
#     wordlist = []
#     for line in inFile:
#         wordlist.extend([word.lower() for word in line.split(' ')])
#     return wordlist

# def is_word(word_list, word):
#     '''
#     Determines if word is a valid word, ignoring
#     capitalization and punctuation

#     word_list (list): list of words in the dictionary.
#     word (string): a possible word.
    
#     Returns: True if word is in word_list, False otherwise

#     Example:
#     >>> is_word(word_list, 'bat') returns
#     True
#     >>> is_word(word_list, 'asdf') returns
#     False
#     '''
#     word = word.lower()
#     word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
#     return word in word_list

# words = load_words('words.txt')

# if 'Hello' in words:
# 	print('hello')

test = 'ahh%!>>'
exceptions = '%!>'
for letter in test:
	if letter in exceptions:
		print(letter)