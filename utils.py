from collections import Counter
from itertools import chain, combinations


def binsearch_right(
    arr, tar,
    comp=lambda x,y: 1 if x<y else 0 if x==y else -1):
    """ binary search the right border
    :param arr: the sorted array search in
    :param tar: the target to search
    :param comp: a compare function to define the relative position,
        get x,y and return 1/0/-1; if comp return 1, x should be placed
        before y, 0 means x==y and x will be placed after y because of
        the right search; -1 to place x after y
    :return: the position of tar in arr (will be after the existed same elements)
    """
    lo = 0
    hi = len(arr)

    while lo < hi:
        mid = (lo + hi) // 2
        if comp(tar, arr[mid]) > 0:
            hi = mid
        else:
            lo = mid + 1

    return lo


def get_freq_items(db, sup_cnt, db_freq=1):
    """find frequent items"""
    item_counter = Counter()
    for i in range(len(db)):
        tra = db[i]
        tra_cnt = {}
        for item in tra:
            if hasattr(db_freq, '__iter__'):
                tra_cnt[item] = db_freq[i]
            else:
                tra_cnt[item] = db_freq
        item_counter += tra_cnt

    return counter_above(item_counter, sup_cnt)


def counter_above(cnt, threshold):
    keys = list(cnt.keys())
    for key in keys:
        if cnt[key] <= threshold:
            del cnt[key]

    return cnt


def count_freq(db, itemsets):
    """count the frequency for each itemset in itemsets"""
    sets_cnt = Counter()
    for t in db:
        st = frozenset(t)
        for itset in itemsets:
            if itset.issubset(st):
                sets_cnt[itset] += 1

    return sets_cnt


def gen_subsets(items, nonempty=True, proper=True, max_len=None):
    """generate subsets of items
    :param items: a set of items
    :param nonempty: require the subset is nonempty
    :param proper: require the subset is a proper subset
    :param max_len: specify the max length of the subset
    """
    items = list(items)
    n = max_len or (len(items)-proper)
    s = 1 if nonempty else 0
    return list(chain.from_iterable(
        [set(c) for c in combinations(items, r)] for r in range(s, n+1)))


if __name__ == "__main__":
    import preprocess
    tras = preprocess.process_groceries(
        preprocess.read_csv(
            './dataset/GroceryStore/Groceries.csv'))[:1000]

    # test binsearch_right
    a = [5, 4, 3, 3, 2, 1]
    p = binsearch_right(a, 3, lambda x,y: 1 if x>y else 0 if x==y else -1)
    print("arr: {}, position of {}: {}".format(a, 3, p))

    # test gen_subsets
    s = {1, 2, 3, 4}
    ss = gen_subsets(s)
    for sub in ss:
        print(sub)

    # test get_freq_items
    print("========== Test get_freq_items ==========")
    items = get_freq_items(tras, 100).most_common()
    print(len(items))
    for item in items:
        print(item)
    print("========== Test get_freq_items finished ==========")