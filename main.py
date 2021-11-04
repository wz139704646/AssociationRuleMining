from fp_growth import fp_growth
import preprocess as prep
from apriori import apriori
import argparse
import time


def parse_args():
    """parse command line arguments"""
    desc = "Association Rule Mining via Apriori algo. and FP-growth algo."
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('--algo', type=str, default='apriori',
                        help='association rule mining algorithm to use (apriori/fp-growth)')
    parser.add_argument('--dataset-file', type=str, default='./dataset/GroceryStore/Groceries.csv',
                        help='the dataset file to use')
    parser.add_argument('--dataset-type', type=str, default='grocery-store',
                        help='the dataset type (grocery-store/unix-usage)')
    parser.add_argument('--allow-empty', action='store_true', default=False,
                        help='whether allow empty rule generated (only empty postfix)')
    parser.add_argument('--ignore-single', action='store_true', default=False,
                        help='whether ignore rules that containing single item')
    parser.add_argument('--min-sup', type=float, default=0.01,
                        help='the minimal support level to satisfy')
    parser.add_argument('--min-conf', type=float, default=0.5,
                        help='the minimal confidence to satisfy')
    parser.add_argument('-n', type=int, default=5,
                        help='run the experiment for n times and get summary by their mean')

    return parser.parse_args()


def main():
    args = parse_args()

    if args.dataset_type == 'grocery-store':
        # grocery store data
        db = prep.process_groceries(
            prep.read_csv(args.dataset_file))
    else:
        db = prep.process_sessions(
            prep.read_sessions(args.dataset_file))

    summary = {}
    st = time.time()
    if args.algo == 'apriori':
        # run apriori
        for _ in range(args.n):
            rules, freq_itemsets = apriori(db, args.min_sup, args.min_conf, args.ignore_single)
    else:
        # run FP-growth
        for _ in range(args.n):
            rules, freq_itemsets = fp_growth(db, args.min_sup, args.min_conf, args.ignore_single)
    et = time.time()
    summary[args.algo+' time elapsed ({} times mean)'.format(args.n)] = (et-st) / args.n
    summary[args.algo+' generated frequent itemsets number'] = len(freq_itemsets)

    st = time.time()
    for _ in range(args.n):
        baseline_rules, baseline_freq_itemsets = apriori(
            db, args.min_sup, args.min_conf, args.ignore_single, prune=False)
    et = time.time()
    summary['baseline time elapsed ({} times mean)'.format(args.n)] = (et-st) / args.n
    summary['baseline generated frequent itemsets number'] = len(baseline_freq_itemsets)

    # show rules
    print('========== {} generate rules =========='.format(args.algo))
    for r in rules:
        if not args.allow_empty and len(r.B) == 0:
            continue
        print(r)
    print('========== baseline generate rules ==========')
    for r in baseline_rules:
        if not args.allow_empty and len(r.B) == 0:
            continue
        print(r)

    # show summary
    print('========== Summary ==========')
    for k, v in summary.items():
        print("{}: {}".format(k, v))


if __name__ == '__main__':
    main()
