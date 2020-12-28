# class Coordinate(object):
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y


# c = Coordinate(1,2)
# print(c.x)

# c.x = 5
# print(c.x)

# shift = 26
# while shift >= 26:
# 	shift -= 26

# print(shift)


# shift = 1
# shift_alphabet = []
# alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
# position = 0
# for letter in alphabet[0:3]:
# 	shift_letter = alphabet[position + shift]
# 	print(letter)
# 	print(shift_letter)
# 	print()
# 	shift_alphabet.append(shift_letter)
# 	position += 1 

# print(shift_alphabet)



# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# shift_alphabet = []
# position = 0

# shift = 2
# for letter in alphabet:
# 	if position + shift > (len(alphabet)-1):
# 		shift -= (shift + position)
# 	shift_letter = alphabet[position + shift]
# 	# print(letter)
# 	# print(shift_letter)
# 	# print()
# 	shift_alphabet.append(shift_letter)
# 	position += 1

# print(shift_alphabet)






# def shift_alphabet(alphabet,shift):

# 	position = 0
# 	shift_dictionary = {}

# 	if shift > 26:
# 		shift = shift % 26

# 	for letter in alphabet:
# 		if position + shift > (len(alphabet)-1):
# 			shift -= (shift + (position))
# 		shift_letter = alphabet[position + shift]

# 		shift_dictionary.update( {letter : shift_letter} )
# 		position += 1

# 	return shift_dictionary


# shift = 27
# lower_shift_dictionary = shift_alphabet('abcdefghijklmnopqrstuvwxyz',shift)
# upper_shift_dictionary = shift_alphabet('ABCDEFGHIJKLMNOPQRSTUVWXYZ',shift)

# print(dict(lower_shift_dictionary, **upper_shift_dictionary))


# # word = 'hi there'
# # word = word.replace(" ","")
# # print(word)

# # string = 'hello'
# # nstring = string + 'world'
# # print(nstring)


# ################MAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
# shift = 2732932930


# class Coordinate(object):
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y


# c = Coordinate(1,2)
# print(c.x)

# c.x = 5
# print(c.x)




List = [2, 1,1,1,1, 2, 2, 1, 3] 
print(max(set(List), key = List.count))