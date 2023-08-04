# A file for experiments with dealing with previously unseen words
from ngrams import preprocess_sequence, preprocess_corpus

def compute_unk_rate_from_corpus(training_corpus: str, val_corpus: str) -> float:
    """
    Given a training corpus and validation corpus,
    computes proportion of words in validation corpus which are previously unseen
    """
    process_train, process_val = preprocess_sequence(training_corpus).split(" "), preprocess_sequence(val_corpus).split(" ")
    return len([word for word in process_val if word not in process_train]) / len(process_val)

def compute_unk_rate_by_threshold(training_corpus: str, threshold: int) -> float:
    """
    Uses a count threshold to decide proportion of unknown words
    
        :param training_corpus - a corpus from which to obtain counts
        :param threshold - a threshold used to decide what qualifies as an unknown word
    """
    # obtaining word counts
    corpus_counts = preprocess_corpus(training_corpus, n_gram_size=1)

    # figuring out how many of words below threshold
    return sum(list(map(lambda x: x < threshold, list(corpus_counts.values())))) / len(corpus_counts)


#def compute_unk_rate_by_ranking(training_corpus: str, bottom_pct_unk: float) -> float:


if __name__ == "__main__":
    # reading in corpus
    with open('corpus.txt', 'r') as corpus_reader:
        train_corpus = corpus_reader.read()
    
    # reading in val corpus
    with open('val_corpus.txt', 'r') as val_corpus_reader:
        val_corpus = val_corpus_reader.read()

    # 40% of american pie song was unknown to my corpus!!
    print(f"Unknown word rate by val corpus: {compute_unk_rate_from_corpus(train_corpus, val_corpus)}")
    print(f"Unknown word rate by word counts below threshold: {compute_unk_rate_by_threshold(train_corpus, 2)}")
