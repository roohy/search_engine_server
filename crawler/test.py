

def isDuplicate(a , b):
    shingle_n_gram = 2
    jaccard_threshold = 0.9

    def isSimilar(str1 , str2):
        aa = str1.split(' ')
        bb = str2.split(' ')
        e1 = set([tuple(aa[i:i + shingle_n_gram]) for i in range(len(aa) - shingle_n_gram + 1)])
        e2 = set([tuple(bb[i:i + shingle_n_gram]) for i in range(len(bb) - shingle_n_gram + 1)])

        jaccard = len(e1.intersection(e2)) / len(e1.union(e2))
        if jaccard >= jaccard_threshold:
            return True
        return False

    for k in b:
        if isSimilar(a , k.body):
            return True
    return False

