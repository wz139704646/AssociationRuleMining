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


def gen_subsets(items, nonempty=True):
    """generate subsets of items
    :param items: a set
    """
    items = list(items)
    n = len(items)
    s = 1 if nonempty else 0
    return list(chain.from_iterable(
        [set(c) for c in combinations(items, r)] for r in range(s, n+1)))


if __name__ == "__main__":
    # test binsearch_right
    a = [5, 4, 3, 3, 2, 1]
    p = binsearch_right(a, 3, lambda x,y: 1 if x>y else 0 if x==y else -1)
    print("arr: {}, position of {}: {}".format(a, 3, p))

    # test gen_subsets
    s = {1, 2, 3}
    ss = gen_subsets(s)
    for sub in ss:
        print(sub)