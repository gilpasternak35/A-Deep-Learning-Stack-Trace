import argparse
import string


def preprocess_sequence(sequence: str) -> str:
    """Removes punctuation from string and converts to lowercase"""
    return sequence.lower().translate(str.maketrans('', '', string.punctuation))

def get_sequence_probability(sequence: str, corpus: str, n_gram_size: int) -> float:
    """Returns the probability fo a given sequence in a given corpus, given a certain n-gram-size"""
    pass

def get_next_word_prediction(sequence: str, corpus: str, n_gram_size: int) -> float:
    """Returns n-gram prediction for the next word given a certain text corpus"""
    pass

def preprocess_corpus(corpus: str, n_gram_size: int) -> dict:
    """Segments corpus and turns it into a dictionary"""
    # preprocessing corpus
    corpus_processed = preprocess_sequence(corpus)

    # counts dictionary
    counts = {}

    # iterating and hashing corpus words
    for i in range(len(corpus) - n_gram_size-1):
        # attaining current n-gram
        current_n_gram = corpus_processed[i:i+n_gram_size]

        # hashing
        counts[current_n_gram] = counts.get(current_n_gram, 0) + 1

    return counts

if __name__ == "__main__":
    # instantiating argument parser and adding arguments
    parser= argparse.ArgumentParser()
    parser.add_argument('--sequence', type = str, default='check this', required=False)

    # parsing argument
    args = parser.parse_args()
    
    # 1. preprocess the sequence
    print(preprocess_sequence(args.sequence))

    # 2. use corpus to return the probability of the sequence
    # 3. predict next word in the sequence
