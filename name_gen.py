import random

import numpy as np


def get_chars(filepath):
	file = open(filepath)
	text = file.read()
	chars = [max(0, ord(char) - 96) for char in text.lower()]

	return chars


def count_chars(chars):
	previous_char = 0
	transition_matrix = np.zeros((27, 27))
	for char in chars:
		transition_matrix[previous_char][char] += 1
		previous_char = char

	return transition_matrix


def normalise_transition_matrix(transition_matrix):
	row_index = 0
	for row in transition_matrix:
		row_count = np.sum(row)
		prev_entry = 0
		entry_index = 0
		if row_count != 0:
			for entry in row:
				prev_entry = prev_entry + entry / row_count
				transition_matrix[row_index][entry_index] = prev_entry
				entry_index += 1
		row_index += 1

	return transition_matrix


def get_name(transition_matrix):
	previous_char = 0
	name = ""
	while True:
		prob = random.random()
		row = transition_matrix[previous_char]
		for char in range(row.shape[0] + 1):
			if prob < row[char]:
				break
		if char == 0:
			break
		previous_char = char
		name += chr(char + 96)

	return name


if __name__ == '__main__':
	chars = get_chars("./names.txt")
	transition_matrix = count_chars(chars)
	transition_matrix = normalise_transition_matrix(transition_matrix)
	for i in range(20):
		name = get_name(transition_matrix)
		print(name)
