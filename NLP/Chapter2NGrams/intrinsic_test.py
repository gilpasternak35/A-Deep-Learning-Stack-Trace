from ngrams import get_sequence_probability, get_next_word_prediction, preprocess_corpus, preprocess_sequence

# list of test corpuses to compute imperfect mle in intrinsic evaluation
test_corpuses = {
"test_corpus_1": """this is a test corpus, what is the probability of this sequence?""",
"test_corpus_2" : "This is another test, and I wonder what the model will think of this. I hope it works well!",
"test_corpus_3" : "The galaxy is so massive, so infinite in its scope, that it is almost impossible to imagine what it might contain.",
"test_corpus_4": "A coin is a small object, usually round and flat, used primarily as a medium of exchange or legal tender. They are standardized in weight, and produced in large quantities at a mint in order to facilitate trade. They are most often issued by a government. Coins often have images, numerals, or text on them. The faces of coins or medals are sometimes called the obverse and the reverse, referring to the front and back sides, respectively. The obverse of a coin is commonly called heads, because it often depicts the head of a prominent person, and the reverse is known as tails. "
}

# train corpus
with open('corpus.txt', 'r') as train_corpus:
    train_corpus = train_corpus.read()

# testing intrinsic evaluation - checking which model assigns higher likelihood to each of four reasonable sequences
for sequence in test_corpuses.values():
    for n in range(1, 5):
        # getting counts dict
        counts_dict = preprocess_corpus(train_corpus, n)
        counts_dict_one_less = preprocess_corpus(train_corpus, n-1)

        # displaying probability, based of sequence, counts dict, counts dict of prior, and model choice
        print(f"n: {n}, sequence: {sequence}, prob; {get_sequence_probability(sequence, counts_dict, counts_dict_one_less, n)}")


# Conclusion: as n gets larger, the model is forced to multiply more and more probabilities, rendering the sequence unlikely. 
# This means that sequences which do less multiplications (the larger n-grams, do to your sliding window mechanism) will be more likely
# generally seems that n=3/4 is best for this corpus
# some n-grams will be much more likely than others, especially is correspond to something in training set