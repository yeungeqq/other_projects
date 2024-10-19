import os
import random
import re
import sys
from collections import Counter


DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    prob_dist = {}
    for item in corpus:
        if item in corpus[page]:
            prob = damping_factor/len(corpus[page]) + (1 - damping_factor)/len(corpus)
            prob_dist[item] = prob
        else:
            prob  = (1 - damping_factor)/len(corpus)
            prob_dist[item] = prob

    return prob_dist


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    surfer = random.choices([*corpus])[0]
    result = []
    for i in range(n):
        prob = transition_model(corpus, surfer, DAMPING)
        pages = [*prob]
        distributions = list(prob.values())
        surfer = random.choices(pages, distributions)[0]
        result.append(surfer)
    rank = dict(Counter(result))
    for item in [*corpus]:
        rank[item] = rank[item]/n

    return rank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    prob = {}
    check = [False for page in corpus]
    for page in corpus:
        prob[page] = 1/len(corpus)
    while not all(check):
        new = {}
        for page in corpus:
            pr_per_link = [prob[link]/len(corpus[link]) for link in corpus if page in corpus[link]]
            for link in corpus:
                if corpus[link] == set():
                    pr_per_link.append(prob[link]/len(corpus))
            new_prob = (1-damping_factor)/len(corpus) + damping_factor*(sum(pr_per_link))
            new[page] = new_prob
        check = [True if abs(new[page] - prob[page]) <= 0.001 else False for page in corpus]
        for page in corpus:
            prob[page] = new[page]

    return prob


if __name__ == "__main__":
    main()
