from collections import Counter
import utils
from association_rule import gen_rules


def apriori(db, min_sup, min_conf, ignore_single=False, prune=True):
    """apriori algorithm"""
    # generate frequent itemsets
    tot_tra = len(db)
    sup_cnt = int(min_sup * tot_tra)
    Lsets = gen_freq_itemsets(db, sup_cnt, prune)
    freq_cnt = Counter()

    # build the whole counter
    for lset in Lsets:
        for item_freq in lset:
            freq_cnt[item_freq[0]] = item_freq[1]

    # generate rules
    rules = []
    freq_itemsets = []
    s = 1 if ignore_single else 0
    for k in range(s, len(Lsets)):
        for (itemset, freq) in Lsets[k]:
            freq_itemsets.append(itemset)
            rules += gen_rules(
                itemset, freq, freq_cnt, min_conf, tot_tra)

    return rules, freq_itemsets


def gen_freq_itemsets(db, sup_cnt, prune=True):
    """generate freq itemsets"""
    # get frequent 1-itemset
    items = utils.get_freq_items(db, sup_cnt)
    items = [(frozenset([item[0]]), item[1]) for item in items]

    cur_Lset = set([item[0] for item in items])
    Lsets = []
    k = 1
    while len(cur_Lset) != 0:
        Lsets.append(items)
        cands = gen_cand(cur_Lset, k+1, prune)
        k += 1

        # scan db for counting
        cand_counter = utils.count_freq(db, cands)

        # filtering candidates
        cands = cand_counter.most_common()
        del_p = utils.binsearch_right(
            cands, ('', sup_cnt),
            lambda x,y: 1 if x[1]>y[1] else 0 if x[1]==y[1] else -1)
        items = cands[:del_p]
        cur_Lset = set([item[0] for item in items])
        # cur_Lset = set()
        # for c in cand_counter.keys():
        #     if cand_counter[c] >= sup_cnt:
        #         cur_Lset.add(c)

    return Lsets


def gen_cand(freq_itemset, k, prune=True):
    """generate k-candidates"""
    cands = set()
    freq_list = list(freq_itemset)
    for i in range(len(freq_list)):
        for j in range(i+1, len(freq_list)):
            c = freq_list[i] | freq_list[j]
            if len(c) == k:
                if prune and be_pruned(c, freq_itemset):
                    continue
                cands.add(c)

    return cands


def be_pruned(cand, freq_itemset):
    """whether the candidate has a infrequent subset (should be pruned)"""
    for c in cand:
        if not {cand - {c}}.issubset(freq_itemset):
            return True

    return False


if __name__ == "__main__":
    import preprocess
    tras = preprocess.process_groceries(
        preprocess.read_csv(
            './dataset/GroceryStore/Groceries.csv'))[:1000]

    # test gen_cand
    print("========== Test gen_cand ==========")
    items = utils.get_freq_items(tras, 100)
    l1 = set([frozenset({item[0]}) for item in items])
    c2 = gen_cand(l1, 2)
    print(len(c2))
    for c in c2:
        print(c)
    print("========== Test gen_cand finished ==========")

    # test gen_freq_items
    print("========== Test gen_cand ==========")
    Lsets = gen_freq_itemsets(tras, 20)
    print(len(Lsets))
    print(Lsets[-1])
    print("========== Test gen_cand finished ==========")

    # test apriori
    print("========== Test apriori==========")
    rules, freq_itemsets = apriori(tras, 0.01, 0.5)
    print("itemsets {}".format(len(freq_itemsets)))
    for itemset in freq_itemsets:
        print(itemset)
    print("rules {}".format(len(rules)))
    for r in rules:
        if len(r.B) != 0:
            print(r)
    print("========== Test apriori finished ==========")