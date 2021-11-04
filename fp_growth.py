from collections import Counter
import utils
from association_rule import gen_rules


class FPNode:
    """The class of nodes in FP tree"""
    def __init__(self, data, freq=1, parent=None) -> None:
        self.data = data
        self.freq = freq
        self.parent = parent
        self.children = []
        self.next = None

    def get_children(self):
        return self.children

    def find_child(self, child_data):
        for c in self.children:
            if c.data == child_data:
                return c

        return None

    def add_child(self, child):
        """add child in FP node"""
        child.set_parent(self)
        self.children.append(child)

    def set_parent(self, parent):
        self.parent = parent


class FPHeaderTable:
    """The class of header table for FP tree"""
    def __init__(self, items_freq) -> None:
        """initialize FP header table
        :param items_freq: list of tuples (item, freq), sorted by freq
        """
        # use a 2-length list [item freqency pair, node] as table entry
        self.raw_table = [[item_freq, None] for item_freq in items_freq]

        # build a hash table to accelerate header search
        self.hash_table = {}
        for i in range(len(self.raw_table)):
            self.hash_table[self.raw_table[i][0][0]] = self.raw_table[i]

    def __len__(self):
        return len(self.raw_table)

    def __iter__(self):
        return iter(self.raw_table)

    def __getitem__(self, key):
        return self.raw_table[key]

    def __delitem__(self, key):
        prev_hash = self.raw_table[key][0][0]
        del self.raw_table[key]
        del self.hash_table[prev_hash]

    def __getslice__(self, i, j):
        return self.raw_table.__getslice__(i, j)

    def __delslice__(self, i, j):
        for e in self.raw_table[i:j]:
            del self.hash_table[e[0][0]]

        del self.raw_table[i:j]

    def __contains__(self, key):
        return key in self.hash_table

    def get_entry(self, data):
        """get table entry by data content"""
        return self.hash_table[data]

    def add_node(self, node):
        """add a new node in the link list"""
        entry = self.get_entry(node.data)
        if entry[1] is None:
            entry[1] = node
        else:
            p = entry[1]
            while p.next is not None:
                p = p.next
            p.next = node


class FPTree:
    """The class of FP tree"""
    def __init__(self, db, db_freq, sup_cnt) -> None:
        """initialize (build) a FP tree
        :param db: the data of transactions
        :param db_freq: the multiplicative frequency for each transaction
        :param sup_cnt: the minimum support count
        """
        self.root = FPNode(None, 0)
        self.tot_base = len(db)
        self.sup_cnt = sup_cnt

        self.construct(db, db_freq)

    def construct(self, db, db_freq):
        """construct the FP tree"""
        # build header table
        items_freq = utils.get_freq_items(db, self.sup_cnt, db_freq)
        self.header_table = FPHeaderTable(items_freq.most_common())

        # build the tree
        for i in range(len(db)):
            d = sorted(
                db[i],
                reverse=True,
                key=lambda x: -1 if x not in self.header_table\
                    else self.header_table.get_entry(x)[0][1])
            d_freq = db_freq[i]
            cur_node = self.root
            for item in d:
                if item not in self.header_table:
                    break
                c = cur_node.find_child(item)
                if c is None:
                    # add a new node
                    c = FPNode(item, freq=d_freq)
                    cur_node.add_child(c)
                    self.header_table.add_node(c)
                else:
                    c.freq += d_freq
                cur_node = c

    def get_conditional_pattern_bases(self, entry):
        """extract the conditional pattern bases in the constructed FP tree"""
        cond_pat_bases = []
        pat_freq = []
        node = entry[1]

        while node is not None:
            p = node.parent
            cond_pat = []
            while p.parent is not None:
                cond_pat.append(p.data)
                p = p.parent

            if len(cond_pat) != 0:
                cond_pat_bases.append(cond_pat)
                pat_freq.append(node.freq)
            node = node.next

        return cond_pat_bases, pat_freq

    def mine_freq_itemsets(self):
        """mine out all the frequent itemsets"""
        freq_itemsets = []
        for entry in self.header_table[-1::-1]:
            itset = frozenset([entry[0][0]])
            freq_itemsets.append(itset)

            # generate sub frequency itemsets recursively
            cond_pat_bases, pat_freq = self.get_conditional_pattern_bases(entry)
            cond_tree = FPTree(cond_pat_bases, pat_freq, self.sup_cnt)
            sub_itemsets = cond_tree.mine_freq_itemsets()
            freq_itemsets.extend([itset | itemset for itemset in sub_itemsets])

        return freq_itemsets


def fp_growth(db, min_sup, min_conf, ignore_single=False):
    """FP growth algorithm"""
    # get frequent itemsets
    tot_base = len(db)
    sup_cnt = int(tot_base * min_sup)
    fptree = FPTree(db, [1] * tot_base, sup_cnt)
    freq_itemsets = fptree.mine_freq_itemsets()

    freq_cnt = utils.count_freq(db, freq_itemsets)
    rules = []
    for itemset in freq_itemsets:
        if ignore_single and len(itemset) == 1:
            continue
        rules += gen_rules(
            itemset, freq_cnt[itemset], freq_cnt, min_conf, tot_base)

    return rules, freq_itemsets


if __name__ == "__main__":
    import preprocess
    tras = preprocess.process_groceries(
        preprocess.read_csv(
            './dataset/GroceryStore/Groceries.csv'))[:1000]

    # test FPHeaderTable
    item_counter = Counter()
    for t in tras:
        item_counter += Counter(t)
    items_freq = item_counter.most_common()
    print("========== Test FPHeaderTable ==========")
    table = FPHeaderTable(items_freq)
    print("---------- test __getitem__ ----------")
    print(table[0])
    print("---------- test __getslice__ ----------")
    for e in table[-1::-1]:
        print(e)
    print("---------- test __iter__ ----------")
    for e in table:
        print(e)
    print("---------- test __contains__ ----------")
    print('syrup' in table)
    print('aaaaaaa' in table)
    print("========== Test FPHeaderTable finished ==========")

    # test FPTree
    print("========== Test FPTree ==========")
    fptree = FPTree(tras, [1] * len(tras), 10)
    itemsets = fptree.mine_freq_itemsets()
    print(len(itemsets))
    for itset in itemsets:
        print(itset)
    print("========== Test FPTree finished ==========")

    # test fp growth
    print("========== Test fp_growth ==========")
    rules, itemsets = fp_growth(tras, 0.01, 0.5)
    print("itemsets {}".format(len(itemsets)))
    for itemset in itemsets:
        print(itemset)
    print("rules {}".format(len(rules)))
    for r in rules:
        if len(r.B) != 0:
            print(r)
    print("========== Test fp_growth finished ==========")
