from collections import Counter
from utils import binsearch_right, gen_subsets
from association_rule import Rule


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
    s = 1 if ignore_single else 0
    for k in range(s, len(Lsets)):
        for (itemset, freq) in Lsets[k]:
            rules += gen_rules(
                itemset, freq, freq_cnt, min_conf, tot_tra)

    return rules


def gen_rules(freq_itemset, supp, freq_map, min_conf, tot_base):
    """generate association rules"""
    rules = []
    subs = gen_subsets(freq_itemset, nonempty=True)
    for s in subs:
        freq = freq_map[frozenset(s)]
        conf = float(supp) / freq
        if conf > min_conf:
            rules.append(Rule(
                s, freq_itemset-s, float(freq)/tot_base, conf))

    return rules


def gen_freq_itemsets(db, sup_cnt, prune=True):
    """generate freq itemsets"""
    # get frequent 1-itemset
    items = get_freq_items(db, sup_cnt)
    items = [(frozenset([item[0]]), item[1]) for item in items]

    cur_Lset = set([item[0] for item in items])
    Lsets = []
    k = 1
    while len(cur_Lset) != 0:
        Lsets.append(items)
        cands = gen_cand(cur_Lset, k+1, prune)
        k += 1

        # scan db for counting
        cand_counter = count_freq(db, cands)

        # filtering candidates
        cands = cand_counter.most_common()
        del_p = binsearch_right(
            cands, ('', sup_cnt),
            lambda x,y: 1 if x[1]>y[1] else 0 if x[1]==y[1] else -1)
        items = cands[:del_p]
        cur_Lset = set([item[0] for item in items])
        # cur_Lset = set()
        # for c in cand_counter.keys():
        #     if cand_counter[c] >= sup_cnt:
        #         cur_Lset.add(c)

    return Lsets


def count_freq(db, itemsets):
    """count the frequency for each itemset in itemsets"""
    sets_cnt = Counter()
    for t in db:
        st = frozenset(t)
        for itset in itemsets:
            if itset.issubset(st):
                sets_cnt[itset] += 1

    return sets_cnt


def get_freq_items(db, sup_cnt):
    """find frequent items"""
    item_counter = Counter()
    for tra in db:
        item_counter += Counter(tra)

    # items with freq
    items = item_counter.most_common()
    # delete infrequent items
    del_p = binsearch_right(
        items, ('', sup_cnt),
        lambda x,y: 1 if x[1]>y[1] else 0 if x[1]==y[1] else -1)

    return items[:del_p]


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

    # test get_freq_items
    print("========== Test get_freq_items ==========")
    items = get_freq_items(tras, 100)
    print(len(items))
    for item in items:
        print(item)
    print("========== Test get_freq_items finished ==========")

    # test gen_cand
    print("========== Test gen_cand ==========")
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
    rules = apriori(tras, 0.01, 0.5)
    for r in rules:
        if len(r.B) != 0:
            print(r)
    print("========== Test apriori finished ==========")