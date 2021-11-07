from collections import Counter
import utils
from association_rule import gen_rules


def exhaustive_search(db, min_sup, min_conf, max_len=None):
    """exhaustive search for frequent itemsets and generate rules"""
    # generate frequent items
    tot_base = len(db)
    sup_cnt = min_sup * tot_base
    # search frequent itemsets exhaustively
    sets_cnt = search_freq_itemsets(db, sup_cnt, max_len)

    # generate rules
    rules = []
    freq_itemsets = []
    for (itemset, freq) in sets_cnt.items():
        rules += gen_rules(
            itemset, freq, sets_cnt, min_conf, tot_base)
        freq_itemsets.append(itemset)

    return rules, freq_itemsets


def search_freq_itemsets(db, sup_cnt, max_len=None):
    # get frequent 1-itemset
    items = utils.get_freq_items(db, sup_cnt)
    max_freq_len = max_len or get_max_freq_len(db, items)

    # generate subsets
    items = [item[0] for item in items.items()]
    itemsets = utils.gen_subsets(items, max_len=max_freq_len, proper=False)
    itemsets = [frozenset(itset) for itset in itemsets]
    sets_cnt = utils.count_freq(db, itemsets)

    return utils.counter_above(sets_cnt, sup_cnt)


def get_max_freq_len(db, freq_items):
    max_freq_len = -1
    for t in db:
        freq_len = 0
        for item in t:
            if item in freq_items.keys():
                freq_len += 1

        max_freq_len = max(max_freq_len, freq_len)

    return max_freq_len


if __name__ == '__main__':
    import preprocess
    tras = preprocess.process_groceries(
        preprocess.read_csv(
            './dataset/GroceryStore/Groceries.csv'))
    # test exhaustive search
    print("========== Test exhaustive_search ==========")
    rules, freq_itemsets = exhaustive_search(tras, 0.01, 0.5, max_len=3)
    print("itemsets {}".format(len(freq_itemsets)))
    for itemset in freq_itemsets:
        print(itemset)
    print("rules {}".format(len(rules)))
    for r in rules:
        print(r)
    print("========== Test exhaustive_search finish ==========")
