from fp_growth import fp_growth
import preprocess as prep
from apriori import apriori
from dummy import exhaustive_search
import argparse
import time


def parse_args():
    """parse command line arguments"""
    desc = "Association Rule Mining via Apriori algo. and FP-growth algo."
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('--algo', type=str, default='apriori',
                        help='association rule mining algorithm to use'
                        '(apriori/fp-growth/apriori-no-prune/(other values will conduct apriori))')
    parser.add_argument('--dataset-file', type=str, default='./dataset/GroceryStore/Groceries.csv',
                        help='the dataset file to use')
    parser.add_argument('--dataset-type', type=str, default='grocery-store',
                        help='the dataset type (grocery-store/unix-usage)')
    parser.add_argument('--cmd-only', action='store_true', default=False,
                        help='only keep the cmd names for unix usage dataset')
    parser.add_argument('--min-sup', type=float, default=0.01,
                        help='the minimal support level to satisfy')
    parser.add_argument('--min-conf', type=float, default=0.5,
                        help='the minimal confidence to satisfy')
    parser.add_argument('-n', type=int, default=5,
                        help='run the experiment for n times and get summary by their mean')
    parser.add_argument('--baseline', type=str, default='exhaustive',
                        help='the baseline method to use '
                        '(apriori/fp-growth/apriori-no-prune/exhaustive/(other values will conduct no baseline))')

    return parser.parse_args()


methods = {
    'apriori':\
        lambda db, min_sup, min_conf:\
            apriori(db, min_sup, min_conf, prune=True),
    'fp-growth':\
        lambda db, min_sup, min_conf:\
            fp_growth(db, min_sup, min_conf),
    'apriori-no-prune':\
        lambda db, min_sup, min_conf:\
            apriori(db, min_sup, min_conf, prune=False),
}


def main():
    args = parse_args()

    if args.dataset_type == 'grocery-store':
        # grocery store data
        db = prep.process_groceries(
            prep.read_csv(args.dataset_file))
    else:
        db = prep.process_sessions(
            prep.read_sessions(args.dataset_file), cmd_only=True)

    summary = {}
    # run algo
    st = time.time()
    if args.algo not in methods:
        args.algo = 'apriori'
    algo = methods[args.algo]
    for _ in range(args.n):
        rules, freq_itemsets = algo(db, args.min_sup, args.min_conf)
    et = time.time()
    summary[args.algo+' time elapsed ({} times mean)'.format(args.n)] = (et-st) / args.n
    summary[args.algo+' generated frequent itemsets number'] = len(freq_itemsets)

    # add truncated exhaustive search to methods
    max_len = 0
    for itemset in freq_itemsets:
        max_len = max(max_len, len(itemset))
    methods['exhaustive'] = lambda db, min_sup, min_conf:\
        exhaustive_search(db, min_sup, min_conf, max_len=max_len)

    # run baseline
    if args.baseline in methods:
        st = time.time()
        for _ in range(args.n):
            baseline_rules, baseline_freq_itemsets = methods[args.baseline](
                db, args.min_sup, args.min_conf)
        et = time.time()
        summary['baseline {} time elapsed ({} times mean)'.format(args.baseline, args.n)]\
            = (et-st) / args.n
        summary['baseline {} generated frequent itemsets number'.format(args.baseline)]\
            = len(baseline_freq_itemsets)

    # show rules
    print('========== {} generate rules =========='.format(args.algo))
    for r in rules:
        print(r)
    if args.baseline in methods:
        print('========== baseline generate rules ==========')
        for r in baseline_rules:
            print(r)

    # show summary
    print('========== Summary ==========')
    for k, v in summary.items():
        print("{}: {}".format(k, v))


if __name__ == '__main__':
    main()
