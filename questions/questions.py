import nltk
import sys
import os
import string
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    files = {}
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename)) as f:
            files[filename] = str(f.read())
    return files


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    doc = document.lower()
    raw_words = nltk.word_tokenize(doc)
    words = [word for word in raw_words if word not in string.punctuation if not word in nltk.corpus.stopwords.words('english')]
    return words


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    idfs = {}
    words = set()
    for filename in documents:
        words.update(documents[filename])
    for word in words:
        f = sum(word in documents[filename] for filename in documents)
        idf = math.log(len(documents) / f)
        idfs[word] = idf
    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    tf_idf = {}
    for filename in files:
        tf_idf[filename] = 0
        for word in query:
            if word in files[filename]:
                tf = sum([True for word_ in files[filename] if word_ == word]) / len(files[filename])
                tf_idf[filename] += idfs[word] * tf
    result = sorted(tf_idf, key=lambda i: tf_idf[i], reverse=True)[:n]
    return result


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    idf = {}
    term_density = {}
    for sentence in sentences:
        idf[sentence] = sum([idfs[word] for word in query if word in sentences[sentence]])
        term_density[sentence] = sum([True for word in sentences[sentence] for word_ in query if word_ == word]) / len(sentences[sentence])
    result = dict(sorted(idf.items(), key=lambda item: item[1], reverse=True))
    same_idf = [(sentence_1, sentence_2) for sentence_1 in result for sentence_2 in result if result[sentence_1] == result[sentence_2]]
    result_list = sorted(result, key=lambda i: result[i], reverse=True)
    for sentence in same_idf:
        if sentence[0] == sentence[1]:
            continue
        if term_density[sentence[0]] > term_density[sentence[1]]:
            if result_list.index(sentence[0]) > result_list.index(sentence[1]):
                result_list[result_list.index(sentence[0])] = sentence[1]
                result_list[result_list.index(sentence[1])] = sentence[0]
    return result_list[:n]


if __name__ == "__main__":
    main()
