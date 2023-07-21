from argparse import ArgumentParser
import heapq

def bpe_encoding(document: str, k: int = 10):
	"""Takes a filename, returns bpe encoding (Chapter 1 Jurafsky Pg. 19)"""
	# reading in file
	with open(document, 'r') as file_reader:
		doc_as_string = file_reader.read()
		string_by_char = [char for char in doc_as_string]

	# to keep track of groupings
	groupings = []

	for i in range(k):
		# obtaining vocabulary as set
		vocab = set(string_by_char)
		adj_pairs_counts = {}
		adj_pairs_heap = []

		# maintaining counts of adjacent pairs
		for i in range(len(string_by_char) - 2):
			pair = string_by_char[i] + string_by_char[i+1]

			# ensuring pairs added are only within a single word
			if ' ' not in pair and '\n' not in pair:
				# upddating counts and setting to 1 if not previously seen
				adj_pairs_counts[pair] = adj_pairs_counts.get(pair, 0) + 1

		adj_pairs_heap = []

		# creating heap of adjacent pairs
		for pair, count in adj_pairs_counts.items():
			heapq.heappush(adj_pairs_heap, (-count, pair))


		# obtaining most frequent adjacent pair
		most_freq_pair = adj_pairs_heap[0]

		# appending most frequent pair to list of groupings
		groupings.append(most_freq_pair[1])

		# resetting counter
		c = 0

		# merging most frequent pair and updating vocab
		while c <= len(string_by_char) - 2:
			# ie need to be merged, merging and updating
			if string_by_char[c] + string_by_char[c+1] == most_freq_pair[1]:
				string_by_char[c] = string_by_char[c] + string_by_char[c+1]
				# deleting second character and updating vocab length
				del string_by_char[c+1]
			c += 1
	# printing groupings
	return groupings

def tokenize_by_groupings(text: str, groupings: list, k: int) -> list:
	"""
	Takes a string and tokenizes it by byte pair encoding groupings (goal: get to words without lexicon)
	"""
	# Traverse through text and tokenize by groupings when possible
	text_as_chars = [char for char in text]

	# k merges of any two found characters in the text
	for i in range(k):
		# counter to keep track of index (while so that no preset length) - retraverse every time
		i = 0
		while i <= len(text_as_chars) - 2:
			# splitting by grouping
			if text_as_chars[i] + text_as_chars[i+1] in groupings:
				# if grouping present, merge the two characters and delete the next index
				text_as_chars[i] = text_as_chars[i] + text_as_chars[i+1]
				del text_as_chars[i+1]

			# incrementing counter
			i += 1

	# returning tokenized strings with found substrings merged together
	return text_as_chars


if __name__ == "__main__":
	# obtaining arguments with argpase
	parser = ArgumentParser("BPE Encoding", description="Computes BPE Encoding of a given document")
	parser.add_argument("--document", type=str, help="Document to be encoded", required=True)
	parser.add_argument("-k", type=int, help="Number of iterations to run BPE", default=10, required=False)
	parser.add_argument("-s", type=str, help="Input string to tokenize", default="Mary had a little lamb, wow what a world", required=False)

	# argparse based bpe encoding
	groupings = bpe_encoding(parser.parse_args().document, parser.parse_args().k)

	# returning actual tokenization
	print(tokenize_by_groupings(parser.parse_args().s, groupings, parser.parse_args().k))
