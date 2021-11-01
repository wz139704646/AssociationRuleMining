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


if __name__ == "__main__":
    r = Rule({"milk"}, {"eggs"}, 0.01, 0.6)
    print(r)