import utils


class Rule:
    """The Association Rule Class"""
    def __init__(self, itemset1, itemset2, supp, conf):
        self.A = itemset1
        self.B = itemset2
        self.supp = supp
        self.conf = conf

    def __repr__(self):
        return "Rule(support {:.4f}, confidence {:.4f}: {} => {})".format(
            self.supp, self.conf, self.A, self.B)


def gen_rules(freq_itemset, supp, freq_map, min_conf, tot_base):
    """generate association rules"""
    rules = []
    supp_rate = supp / tot_base
    subs = utils.gen_subsets(freq_itemset, nonempty=True)
    for s in subs:
        freq = freq_map[frozenset(s)]
        conf = float(supp) / freq
        if conf > min_conf:
            rules.append(Rule(
                s, freq_itemset-s, supp_rate, conf))

    return rules


if __name__ == "__main__":
    r = Rule({"milk"}, {"eggs"}, 0.01, 0.6)
    print(r)