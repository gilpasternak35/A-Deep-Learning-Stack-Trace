import argparse
import string
import math 
import random


def preprocess_sequence(sequence: str) -> str:
    """
    Removes punctuation from string and converts to lowercase

    args:
        sequence: string of words

    returns:
        string of words with no punctuation, newlines, or lowercase
    """
    return sequence.lower().translate(str.maketrans('', '', string.punctuation)).replace('\n', ' ').strip()


def sample(corpus_counts: dict) -> str:
    """Samples a word"""
    # building a cumulative probability range for every word
    cum_probs = []
    corresponding_words = []
    curr_prob = 0
    sum_corpus_counts = sum(corpus_counts.values())
    for word, count in corpus_counts.items():

        # cummulative proability range creation, as dictated by word counts
        cum_probs.append((curr_prob, curr_prob + count/sum_corpus_counts))
        curr_prob += count/sum_corpus_counts

        # appending corresponding word to probability range for the maintanence of consistency
        corresponding_words.append(word)

    print(cum_probs, corresponding_words)

    # sampling a random number
    rand_prob = random.randint(0,10_000)/10_000

    # finding the word corresponding to the uniform probability
    for idx, prob_range in enumerate(cum_probs):
        if prob_range[0] <= rand_prob <= prob_range[1]:
            return corresponding_words[idx]

    # if not found in given probability range   
    return "Error"


def model_sample(corpus_counts: dict, corpus_counts_one_gram: dict) -> str:
    """
    Samples a random sentence from the n-gram language model.

    :param: corpus_counts: dictionary of n-grams and their counts
    :param: corpus_counts_one_gram: dictionary of 1-grams and their counts

    :returns: a string, the sampled sentence
    """
    # obtaining first word
    sen = sample(corpus_counts_one_gram)

    # lining up values by probability so that they can be sampled by respective probabilities
    # repeatedly sampling until EOS token is sampled
    # returning sampled sentence

    return sen



def get_sequence_probability(sequence: str, corpus_counts: dict, corpus_counts_one_less: dict,  n_gram_size: int) -> float:
    """
    Returns the probability fo a given sequence in a given corpus, given a certain n-gram-size
    
    args:
        sequence: string of words
        corpus_counts: dictionary of n-grams and their counts
        corpus_counts_one_less: a dictionary of n-grams not including current word
        n_gram_size: size of n-gram to use

    returns:
        probability of sequence in corpus
    """
    # tokenizing sequence
    tokenized = sequence.split(" ")

    # conditional probability multiplier
    final_prob = 0

    # probability updates
    for counter in range(0, len(tokenized)-n_gram_size+1):
        # obtaining n-gram
        n_gram = " ".join(tokenized[counter:counter+n_gram_size])
        n_gram_no_last_word=" ".join(tokenized[counter:counter+n_gram_size-1])

        # returning final prob given space of context
        # using log prob as to avoid underflow, and adding 0.0001 to avoid 0 probabilities
        final_prob += math.log(corpus_counts.get(n_gram, 0.0001) / corpus_counts_one_less.get(n_gram_no_last_word, 1))

    # returning final probability
    return math.exp(final_prob)
    

def get_next_word_prediction(sequence: str, corpus: str, n_gram_size:int = 2) -> float:
    """Returns n-gram prediction for the next word given a certain text corpus"""

    # reprocessing to get counts dict for larger sequences (n-grams plus sequence)
    corpus_n_grams = preprocess_corpus(corpus, n_gram_size)
    words = preprocess_sequence(corpus).split(" ")
    corpus_n_grams_one_less = preprocess_corpus(corpus, n_gram_size-1)
    probs = []
    
    # checking every extension of sequence
    for word in words:

        # figuring out sequence with next word
        current_seq = sequence + ' ' + word

        # getting probability of sequence with word and appending to list
        current_seq_prob = get_sequence_probability(current_seq, corpus_n_grams, corpus_n_grams_one_less, n_gram_size)
        probs.append((current_seq_prob, current_seq))

    # custom sorting for sequence probabilities
    probs  = sorted(probs, reverse=True, key=lambda x: x[0])

    # returning most likely sequence
    return probs[0][1]


def preprocess_corpus(corpus: str, n_gram_size: int) -> dict:
    """
    Segments corpus and turns it into an n-gram counts hashmap
    
    args:
        corpus: string of words
        n_gram_size: size of n-gram to use

    returns:
        dictionary of n-grams and their counts
    """
    # preprocessing corpus
    corpus_processed = preprocess_sequence(corpus).split(" ")

    # counts dictionary
    counts = {}

    # iterating and hashing corpus words
    for i in range(len(corpus) - n_gram_size-1):
        # attaining current n-gram (combining words from list)
        current_n_gram = " ".join(corpus_processed[i:i+n_gram_size])

        # hashing
        counts[current_n_gram] = counts.get(current_n_gram, 0) + 1

    if ' ' in counts.keys():
        counts.pop(' ')

    return counts


if __name__ == "__main__":
    # instantiating argument parser and adding arguments
    parser= argparse.ArgumentParser()
    parser.add_argument('--corpus', type = str, default='corpus.txt', required=False)
    parser.add_argument('--sequence', type = str, default='check this', required=False)
    parser.add_argument('--n-gram', type = int, default=2, required=False)
    parser.add_argument('--sample', type = bool, default=True, required=False)


    # parsing argument
    args = parser.parse_args()
    
    # 1. preprocess the sequence and corpus
    proc_seq = preprocess_sequence(args.sequence)

    # processing corpus and turning into a counts dictionary
    with open(args.corpus, 'r') as corpus_reader:
        corpus = corpus_reader.read()

    corpus_counts = preprocess_corpus(corpus, args.n_gram)
    corpus_counts_one_less = preprocess_corpus(corpus, args.n_gram-1)
    corpus_counts_one_gram = preprocess_corpus(corpus, 1)


    # 2. use corpus to return the probability of the sequence
    print(get_sequence_probability(proc_seq, corpus_counts,corpus_counts_one_less, args.n_gram))

    # 3. predict next word in the sequence
    print(f"Next word prediction: {get_next_word_prediction(proc_seq, corpus, args.n_gram)}")

    # 4. sample a random sentence from the model
    if args.sample:
        print(f"Sampled sentence: {model_sample(corpus_counts, corpus_counts_one_gram)}")

    
    
