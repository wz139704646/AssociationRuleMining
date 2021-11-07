# Association Rule Mining

## Reults
Grocery Store

Apriori:
```cmd
$ python main.py

========== apriori generate rules ==========
Rule(support 0.0151, confidence 0.5174: {'yogurt', 'tropical fruit'} => frozenset({'whole milk'}))
Rule(support 0.0101, confidence 0.5824: {'curd', 'yogurt'} => frozenset({'whole milk'}))
Rule(support 0.0123, confidence 0.5845: {'root vegetables', 'tropical fruit'} => frozenset({'other vegetables'}))
Rule(support 0.0122, confidence 0.5021: {'root vegetables', 'rolls/buns'} => frozenset({'other vegetables'}))
Rule(support 0.0146, confidence 0.5070: {'whipped/sour cream', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0120, confidence 0.5700: {'root vegetables', 'tropical fruit'} => frozenset({'whole milk'}))
Rule(support 0.0145, confidence 0.5630: {'root vegetables', 'yogurt'} => frozenset({'whole milk'}))
Rule(support 0.0127, confidence 0.5230: {'root vegetables', 'rolls/buns'} => frozenset({'whole milk'}))
Rule(support 0.0104, confidence 0.5862: {'root vegetables', 'citrus fruit'} => frozenset({'other vegetables'}))
Rule(support 0.0123, confidence 0.5525: {'domestic eggs', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0135, confidence 0.5175: {'pip fruit', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0223, confidence 0.5129: {'yogurt', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0109, confidence 0.5245: {'yogurt', 'whipped/sour cream'} => frozenset({'whole milk'}))
Rule(support 0.0115, confidence 0.5736: {'butter', 'other vegetables'} => frozenset({'whole milk'}))
========== baseline generate rules ==========
Rule(support 0.0151, confidence 0.5174: {'yogurt', 'tropical fruit'} => frozenset({'whole milk'}))
Rule(support 0.0101, confidence 0.5824: {'curd', 'yogurt'} => frozenset({'whole milk'}))
Rule(support 0.0123, confidence 0.5845: {'root vegetables', 'tropical fruit'} => frozenset({'other vegetables'}))
Rule(support 0.0122, confidence 0.5021: {'root vegetables', 'rolls/buns'} => frozenset({'other vegetables'}))
Rule(support 0.0146, confidence 0.5070: {'whipped/sour cream', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0145, confidence 0.5630: {'root vegetables', 'yogurt'} => frozenset({'whole milk'}))
Rule(support 0.0120, confidence 0.5700: {'root vegetables', 'tropical fruit'} => frozenset({'whole milk'}))
Rule(support 0.0127, confidence 0.5230: {'root vegetables', 'rolls/buns'} => frozenset({'whole milk'}))
Rule(support 0.0104, confidence 0.5862: {'citrus fruit', 'root vegetables'} => frozenset({'other vegetables'}))
Rule(support 0.0123, confidence 0.5525: {'domestic eggs', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0135, confidence 0.5175: {'pip fruit', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0223, confidence 0.5129: {'yogurt', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0109, confidence 0.5245: {'yogurt', 'whipped/sour cream'} => frozenset({'whole milk'}))
Rule(support 0.0115, confidence 0.5736: {'butter', 'other vegetables'} => frozenset({'whole milk'}))
========== Summary ==========
apriori time elapsed (5 times mean): 3.5393945217132567
apriori generated frequent itemsets number: 333
baseline exhaustive time elapsed (5 times mean): 72.31740670204162
baseline exhaustive generated frequent itemsets number: 333
```

FP-growth:


```cmd
$ python main.py --algo fp-growth

========== fp-growth generate rules ==========
Rule(support 0.0101, confidence 0.5824: {'yogurt', 'curd'} => frozenset({'whole milk'}))
Rule(support 0.0115, confidence 0.5736: {'butter', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0123, confidence 0.5525: {'domestic eggs', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0109, confidence 0.5245: {'yogurt', 'whipped/sour cream'} => frozenset({'whole milk'}))
Rule(support 0.0146, confidence 0.5070: {'whipped/sour cream', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0135, confidence 0.5175: {'pip fruit', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0104, confidence 0.5862: {'citrus fruit', 'root vegetables'} => frozenset({'other vegetables'}))
Rule(support 0.0120, confidence 0.5700: {'root vegetables', 'tropical fruit'} => frozenset({'whole milk'}))
Rule(support 0.0123, confidence 0.5845: {'root vegetables', 'tropical fruit'} => frozenset({'other vegetables'}))
Rule(support 0.0151, confidence 0.5174: {'yogurt', 'tropical fruit'} => frozenset({'whole milk'}))
Rule(support 0.0122, confidence 0.5021: {'rolls/buns', 'root vegetables'} => frozenset({'other vegetables'}))
Rule(support 0.0127, confidence 0.5230: {'rolls/buns', 'root vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0145, confidence 0.5630: {'yogurt', 'root vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0223, confidence 0.5129: {'yogurt', 'other vegetables'} => frozenset({'whole milk'}))
========== baseline generate rules ==========
Rule(support 0.0151, confidence 0.5174: {'yogurt', 'tropical fruit'} => frozenset({'whole milk'}))
Rule(support 0.0101, confidence 0.5824: {'yogurt', 'curd'} => frozenset({'whole milk'}))
Rule(support 0.0123, confidence 0.5845: {'root vegetables', 'tropical fruit'} => frozenset({'other vegetables'}))
Rule(support 0.0122, confidence 0.5021: {'rolls/buns', 'root vegetables'} => frozenset({'other vegetables'}))
Rule(support 0.0146, confidence 0.5070: {'whipped/sour cream', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0145, confidence 0.5630: {'yogurt', 'root vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0120, confidence 0.5700: {'root vegetables', 'tropical fruit'} => frozenset({'whole milk'}))
Rule(support 0.0127, confidence 0.5230: {'rolls/buns', 'root vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0104, confidence 0.5862: {'citrus fruit', 'root vegetables'} => frozenset({'other vegetables'}))
Rule(support 0.0123, confidence 0.5525: {'domestic eggs', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0135, confidence 0.5175: {'pip fruit', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0223, confidence 0.5129: {'yogurt', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0109, confidence 0.5245: {'yogurt', 'whipped/sour cream'} => frozenset({'whole milk'}))
Rule(support 0.0115, confidence 0.5736: {'butter', 'other vegetables'} => frozenset({'whole milk'}))
========== Summary ==========
fp-growth time elapsed (5 times mean): 0.968793535232544
fp-growth generated frequent itemsets number: 333
baseline exhaustive time elapsed (5 times mean): 74.13179950714111
baseline exhaustive generated frequent itemsets number: 333
```