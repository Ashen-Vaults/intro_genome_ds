def pattern_matching(text, pattern):
    return [[x, str(len(pattern) + x)] for x in range(len(text) - len(pattern) + 1) if pattern in text[x:len(pattern) + x]]


def frequent_words(text, k):
    """ Finds the most common k-mers of k """
    counts = [len(pattern_matching(text, text[x:x + k])) for x in range(len(text) - k)]
    return set([text[x:x + k] for x in range(len(text) - k) if counts[x] == max(counts)])


def reverse_complement(pattern):
    """ Formed by taking the complement of each nucleotide in Pattern """
    complements = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    return ''.join([complements.get(c, c) for c in pattern][::-1])


def find_invert_repeats(text, pattern_size):
    freqs = frequent_words(text, pattern_size)
    rev_freqs = frequent_words(reverse_complement(text), pattern_size)
    data = [[x, str(pattern_matching(text,x))] for x in set(freqs).intersection(rev_freqs)]
    return data


#print([x[0] for x in pattern_matching("GATATATGCATATACTT", "ATAT")])
#print(frequent_words("BABBASDCABCBABDDASDBBCASDBAB", 3))
#print(reverse_complement("AGGGTTTCCCTGACCTTCACTGCAGGTCATGCA"))  # -> ACCGGGTTTT
print(find_invert_repeats("AGGGTTTCCCTGACCTTCACTGCAGGTCATGCA", 6))
