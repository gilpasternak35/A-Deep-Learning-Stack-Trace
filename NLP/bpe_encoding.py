from argparse import ArgumentParser
import heapq

def bpe_encoding(document: str, k: int = 10):
	"""Takes a filename, returns bpe encoding (Chapter 1 Jurafsky Pg. 19)"""
	# reading in file
	with open(document, 'r') as file_reader:
		doc_as_string = file_reader.read()
		string_by_char = [char for char in doc_as_string]

	
	for i in range(k):
	
		# obtaining vocabulary as set
		vocab = set(string_by_char)
		adj_pairs_counts = {}
		adj_pairs_heap = []

		# maintaining counts of adjacent pairs
		for i in range(len(doc_as_string) - 2):
			pair = doc_as_string[i] + doc_as_string[i+1]

			# upddating counts and setting to 1 if not previously seen
			adj_pairs_counts[pair] = adj_pairs_counts.get(pair, 0) + 1

		adj_pairs_heap = []

		# creating heap of adjacent pairs
		for pair, count in adj_pairs_counts.items():
			heapq.heappush(adj_pairs_heap, (count, pair))

		# obtaining most frequent adjacent pair
		most_freq_pair = adj_pairs_heap[0]

		print(most_freq_pair)

if __name__ == "__main__":
	# obtaining arguments with argpase
	parser = ArgumentParser("BPE Encoding", description="Computes BPE Encoding of a given document")
	parser.add_argument("--document", type=str, help="Document to be encoded", required=True)
	parser.add_argument("-k", type=int, help="Number of iterations to run BPE", default=10, required=False)

	# argparse based bpe encoding
	bpe_encoding(parser.parse_args().document, parser.parse_args().k)
