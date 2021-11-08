# Association Rule Mining

## Codes

主要文件如下：

- apriori.py 中主要包含了 apriori 算法的核心过程，算法的入口为函数 `apriori` .
- fp_growth.py 中主要包含了 FP-Growth 算法的核心过程以及数据结构，算法的入口函数为 `fp_growth`.
- dummy.py 中主要包含了额外的 baseline 方法，目前实现了暴力搜索频繁项集的方法（入口为 `exhaustive_search`）。
- utils.py 中包含了一些在各算法中可复用的工具函数。
- association_rule.py 中定义了关联规则的数据类 (`Rule`)，并提供了从频繁项集中生成强关联规则的函数 `gen_rules` .
- statistics.ipynb 中主要对数据集的一些统计指标进行了分析。

## Usage
```cmd
$ python main.py --help

usage: main.py [-h] [--algo ALGO] [--dataset-file DATASET_FILE] [--dataset-type DATASET_TYPE] [--cmd-only] [--min-sup MIN_SUP] [--min-conf MIN_CONF] [-n N]
               [--baseline BASELINE]

Association Rule Mining via Apriori algo. and FP-growth algo.

optional arguments:
  -h, --help            show this help message and exit
  --algo ALGO           association rule mining algorithm to use(apriori/fp-growth/apriori-no-prune/(other values will conduct apriori))
  --dataset-file DATASET_FILE
                        the dataset file to use
  --dataset-type DATASET_TYPE
                        the dataset type (grocery-store/unix-usage)
  --cmd-only            only keep the cmd names for unix usage dataset
  --min-sup MIN_SUP     the minimal support level to satisfy
  --min-conf MIN_CONF   the minimal confidence to satisfy
  -n N                  run the experiment for n times and get summary by their mean
  --baseline BASELINE   the baseline method to use (apriori/fp-growth/apriori-no-prune/exhaustive/(other values will conduct no baseline))
```

## Experiments

- [x] `python main.py --min-sup 0.008 --min-conf 0.5 > results/result0`
- [x] `python main.py --min-sup 0.01 --min-conf 0.5 > results/result1`
- [x] `python main.py --min-sup 0.02 --min-conf 0.5 > results/result2`
- [x] `mprof run python main.py --min-sup 0.008 --min-conf 0.5 --baseline no -n 1`
- [x] `mprof run python main.py --min-sup 0.01 --min-conf 0.5 --baseline no -n 1`
- [x] `mprof run python main.py --min-sup 0.02 --min-conf 0.5 --baseline no -n 1`
- [x] `python main.py --min-sup 0.008 --min-conf 0.5 --baseline no --algo fp-growth > results/result3`
- [x] `python main.py --min-sup 0.01 --min-conf 0.5 --baseline no --algo fp-growth > results/result4`
- [x] `python main.py --min-sup 0.02 --min-conf 0.5 --baseline no --algo fp-growth > results/result5`
- [x] `mprof run python main.py --min-sup 0.008 --min-conf 0.5 --baseline no -n 1 --algo fp-growth`
- [x] `mprof run python main.py --min-sup 0.01 --min-conf 0.5 --baseline no -n 1 --algo fp-growth`
- [x] `mprof run python main.py --min-sup 0.02 --min-conf 0.5 --baseline no -n 1 --algo fp-growth`
- [x] `mprof run python main.py --min-sup 0.008 --min-conf 0.5 --baseline no -n 1 --algo exhaustive`
- [x] `mprof run python main.py --min-sup 0.01 --min-conf 0.5 --baseline no -n 1 --algo exhaustive`
- [x] `mprof run python main.py --min-sup 0.02 --min-conf 0.5 --baseline no -n 1 --algo exhaustive`
- [x] `python main.py --min-sup 0.1 --min-conf 0.75 --dataset-type unix-usage --dataset-file ./dataset/UNIX_usage/all_users.981115184025 > results/result6`
- [x] `python main.py --min-sup 0.05 --min-conf 0.75 --dataset-type unix-usage --dataset-file ./dataset/UNIX_usage/all_users.981115184025 > results/result7`
- [x] `python main.py --min-sup 0.025 --min-conf 0.75 --dataset-type unix-usage --dataset-file ./dataset/UNIX_usage/all_users.981115184025 > results/result8`
- [x] `mprof run python main.py --min-sup 0.1 --min-conf 0.75 --dataset-type unix-usage --dataset-file ./dataset/UNIX_usage/all_users.981115184025 --baseline no -n 1`
- [x] `mprof run python main.py --min-sup 0.05 --min-conf 0.75 --dataset-type unix-usage --dataset-file ./dataset/UNIX_usage/all_users.981115184025 --baseline no -n 1`
- [x] `mprof run python main.py --min-sup 0.025 --min-conf 0.75 --dataset-type unix-usage --dataset-file ./dataset/UNIX_usage/all_users.981115184025 --baseline no -n 1`
- [x] `python main.py --min-sup 0.1 --min-conf 0.75 --dataset-type unix-usage --dataset-file ./dataset/UNIX_usage/all_users.981115184025 --algo fp-growth --baseline no > results/result9`
- [x] `python main.py --min-sup 0.05 --min-conf 0.75 --dataset-type unix-usage --dataset-file ./dataset/UNIX_usage/all_users.981115184025 --algo fp-growth --baseline no > results/result10`
- [x] `python main.py --min-sup 0.025 --min-conf 0.75 --dataset-type unix-usage --dataset-file ./dataset/UNIX_usage/all_users.981115184025 --algo fp-growth --baseline no > results/result11`
- [x] `mprof run python main.py --min-sup 0.1 --min-conf 0.75 --dataset-type unix-usage --dataset-file ./dataset/UNIX_usage/all_users.981115184025 --algo fp-growth --baseline no -n 1`
- [x] `mprof run python main.py --min-sup 0.05 --min-conf 0.75 --dataset-type unix-usage --dataset-file ./dataset/UNIX_usage/all_users.981115184025 --algo fp-growth --baseline no -n 1`
- [x] `mprof run python main.py --min-sup 0.025 --min-conf 0.75 --dataset-type unix-usage --dataset-file ./dataset/UNIX_usage/all_users.981115184025 --algo fp-growth --baseline no -n 1`
- [x] `mprof run python main.py --min-sup 0.1 --min-conf 0.75 --dataset-type unix-usage --dataset-file ./dataset/UNIX_usage/all_users.981115184025 --algo exhaustive --baseline no -n 1`
- [x] `mprof run python main.py --min-sup 0.05 --min-conf 0.75 --dataset-type unix-usage --dataset-file ./dataset/UNIX_usage/all_users.981115184025 --algo exhaustive --baseline no -n 1 --max-len 4`
- [x] `mprof run python main.py --min-sup 0.025 --min-conf 0.75 --dataset-type unix-usage --dataset-file ./dataset/UNIX_usage/all_users.981115184025 --algo exhaustive --baseline no -n 1 --max-len 5`

## Reults
Grocery Store

Apriori:
```cmd
$ python main.py

========== apriori generate rules ==========
Rule(support 0.0151, confidence 0.5174: {'yogurt', 'tropical fruit'} => frozenset({'whole milk'}))
Rule(support 0.0101, confidence 0.5824: {'curd', 'yogurt'} => frozenset({'whole milk'}))
Rule(support 0.0122, confidence 0.5021: {'rolls/buns', 'root vegetables'} => frozenset({'other vegetables'}))
Rule(support 0.0123, confidence 0.5845: {'root vegetables', 'tropical fruit'} => frozenset({'other vegetables'}))
Rule(support 0.0146, confidence 0.5070: {'other vegetables', 'whipped/sour cream'} => frozenset({'whole milk'}))
Rule(support 0.0120, confidence 0.5700: {'root vegetables', 'tropical fruit'} => frozenset({'whole milk'}))
Rule(support 0.0145, confidence 0.5630: {'yogurt', 'root vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0127, confidence 0.5230: {'rolls/buns', 'root vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0104, confidence 0.5862: {'citrus fruit', 'root vegetables'} => frozenset({'other vegetables'}))
Rule(support 0.0123, confidence 0.5525: {'domestic eggs', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0135, confidence 0.5175: {'other vegetables', 'pip fruit'} => frozenset({'whole milk'}))
Rule(support 0.0223, confidence 0.5129: {'yogurt', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0115, confidence 0.5736: {'other vegetables', 'butter'} => frozenset({'whole milk'}))
Rule(support 0.0109, confidence 0.5245: {'yogurt', 'whipped/sour cream'} => frozenset({'whole milk'}))
========== baseline generate rules ==========
Rule(support 0.0151, confidence 0.5174: {'yogurt', 'tropical fruit'} => frozenset({'whole milk'}))
Rule(support 0.0101, confidence 0.5824: {'curd', 'yogurt'} => frozenset({'whole milk'}))
Rule(support 0.0123, confidence 0.5845: {'root vegetables', 'tropical fruit'} => frozenset({'other vegetables'}))
Rule(support 0.0122, confidence 0.5021: {'rolls/buns', 'root vegetables'} => frozenset({'other vegetables'}))
Rule(support 0.0146, confidence 0.5070: {'other vegetables', 'whipped/sour cream'} => frozenset({'whole milk'}))
Rule(support 0.0145, confidence 0.5630: {'yogurt', 'root vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0120, confidence 0.5700: {'root vegetables', 'tropical fruit'} => frozenset({'whole milk'}))
Rule(support 0.0127, confidence 0.5230: {'rolls/buns', 'root vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0104, confidence 0.5862: {'citrus fruit', 'root vegetables'} => frozenset({'other vegetables'}))
Rule(support 0.0123, confidence 0.5525: {'domestic eggs', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0135, confidence 0.5175: {'other vegetables', 'pip fruit'} => frozenset({'whole milk'}))
Rule(support 0.0223, confidence 0.5129: {'yogurt', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0109, confidence 0.5245: {'yogurt', 'whipped/sour cream'} => frozenset({'whole milk'}))
Rule(support 0.0115, confidence 0.5736: {'other vegetables', 'butter'} => frozenset({'whole milk'}))
========== Summary ==========
apriori time elapsed (5 times mean): 3.624164915084839
apriori generated frequent itemsets number: 333
apriori generated rules number: 14
apriori generated frequent itemsets max length: 3
baseline exhaustive time elapsed (5 times mean): 72.81702527999877
baseline exhaustive generated frequent itemsets number: 333
baseline exhaustive generated rules number: 14
baseline exhaustive generated frequent itemsets max length: 3
```

FP-growth:


```cmd
$ python main.py --algo fp-growth --baseline no

========== fp-growth generate rules ==========
Rule(support 0.0101, confidence 0.5824: {'yogurt', 'curd'} => frozenset({'whole milk'}))
Rule(support 0.0115, confidence 0.5736: {'butter', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0123, confidence 0.5525: {'domestic eggs', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0109, confidence 0.5245: {'whipped/sour cream', 'yogurt'} => frozenset({'whole milk'}))
Rule(support 0.0146, confidence 0.5070: {'whipped/sour cream', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0135, confidence 0.5175: {'pip fruit', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0104, confidence 0.5862: {'root vegetables', 'citrus fruit'} => frozenset({'other vegetables'}))
Rule(support 0.0120, confidence 0.5700: {'tropical fruit', 'root vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0123, confidence 0.5845: {'tropical fruit', 'root vegetables'} => frozenset({'other vegetables'}))
Rule(support 0.0151, confidence 0.5174: {'tropical fruit', 'yogurt'} => frozenset({'whole milk'}))
Rule(support 0.0122, confidence 0.5021: {'rolls/buns', 'root vegetables'} => frozenset({'other vegetables'}))
Rule(support 0.0127, confidence 0.5230: {'rolls/buns', 'root vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0145, confidence 0.5630: {'yogurt', 'root vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0223, confidence 0.5129: {'yogurt', 'other vegetables'} => frozenset({'whole milk'}))
========== Summary ==========
fp-growth time elapsed (5 times mean): 0.8856001377105713
fp-growth generated frequent itemsets number: 333
fp-growth generated rules number: 14
fp-growth generated frequent itemsets max length: 3
```