# Association Rule Mining

## Reults
Grocery Store

Apriori:
```cmd
$ python main.py

========== apriori generate rules ==========
Rule(support 0.0223, confidence 0.5129: {'other vegetables', 'yogurt'} => frozenset({'whole milk'}))
Rule(support 0.0151, confidence 0.5174: {'tropical fruit', 'yogurt'} => frozenset({'whole milk'}))
Rule(support 0.0146, confidence 0.5070: {'other vegetables', 'whipped/sour cream'} => frozenset({'whole milk'}))
Rule(support 0.0145, confidence 0.5630: {'root vegetables', 'yogurt'} => frozenset({'whole milk'}))
Rule(support 0.0135, confidence 0.5175: {'other vegetables', 'pip fruit'} => frozenset({'whole milk'}))
Rule(support 0.0127, confidence 0.5230: {'rolls/buns', 'root vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0123, confidence 0.5845: {'tropical fruit', 'root vegetables'} => frozenset({'other vegetables'}))
Rule(support 0.0123, confidence 0.5525: {'domestic eggs', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0122, confidence 0.5021: {'rolls/buns', 'root vegetables'} => frozenset({'other vegetables'}))
Rule(support 0.0120, confidence 0.5700: {'tropical fruit', 'root vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0115, confidence 0.5736: {'other vegetables', 'butter'} => frozenset({'whole milk'}))
Rule(support 0.0109, confidence 0.5245: {'whipped/sour cream', 'yogurt'} => frozenset({'whole milk'}))
Rule(support 0.0104, confidence 0.5862: {'citrus fruit', 'root vegetables'} => frozenset({'other vegetables'}))
Rule(support 0.0101, confidence 0.5824: {'curd', 'yogurt'} => frozenset({'whole milk'}))
========== baseline generate rules ==========
Rule(support 0.0223, confidence 0.5129: {'other vegetables', 'yogurt'} => frozenset({'whole milk'}))
Rule(support 0.0151, confidence 0.5174: {'tropical fruit', 'yogurt'} => frozenset({'whole milk'}))
Rule(support 0.0146, confidence 0.5070: {'other vegetables', 'whipped/sour cream'} => frozenset({'whole milk'}))
Rule(support 0.0145, confidence 0.5630: {'root vegetables', 'yogurt'} => frozenset({'whole milk'}))
Rule(support 0.0135, confidence 0.5175: {'other vegetables', 'pip fruit'} => frozenset({'whole milk'}))
Rule(support 0.0127, confidence 0.5230: {'rolls/buns', 'root vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0123, confidence 0.5845: {'tropical fruit', 'root vegetables'} => frozenset({'other vegetables'}))
Rule(support 0.0123, confidence 0.5525: {'domestic eggs', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0122, confidence 0.5021: {'rolls/buns', 'root vegetables'} => frozenset({'other vegetables'}))
Rule(support 0.0120, confidence 0.5700: {'tropical fruit', 'root vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0115, confidence 0.5736: {'other vegetables', 'butter'} => frozenset({'whole milk'}))
Rule(support 0.0109, confidence 0.5245: {'whipped/sour cream', 'yogurt'} => frozenset({'whole milk'}))
Rule(support 0.0104, confidence 0.5862: {'citrus fruit', 'root vegetables'} => frozenset({'other vegetables'}))
Rule(support 0.0101, confidence 0.5824: {'curd', 'yogurt'} => frozenset({'whole milk'}))
========== Summary ==========
apriori time elapsed: 3.822706699371338
apriori generated frequent itemsets number: 341
baseline time elapsed: 5.81139349937439
baseline generated frequent itemsets number: 341
```

FP-growth:


```cmd
$ python main.py --algo fp-growth

========== fp-growth generate rules ==========
Rule(support 0.0101, confidence 0.5824: {'curd', 'yogurt'} => frozenset({'whole milk'}))
Rule(support 0.0115, confidence 0.5736: {'other vegetables', 'butter'} => frozenset({'whole milk'}))
Rule(support 0.0123, confidence 0.5525: {'domestic eggs', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0109, confidence 0.5245: {'whipped/sour cream', 'yogurt'} => frozenset({'whole milk'}))
Rule(support 0.0146, confidence 0.5070: {'other vegetables', 'whipped/sour cream'} => frozenset({'whole milk'}))
Rule(support 0.0135, confidence 0.5175: {'pip fruit', 'other vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0104, confidence 0.5862: {'citrus fruit', 'root vegetables'} => frozenset({'other vegetables'}))
Rule(support 0.0120, confidence 0.5700: {'tropical fruit', 'root vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0123, confidence 0.5845: {'tropical fruit', 'root vegetables'} => frozenset({'other vegetables'}))
Rule(support 0.0151, confidence 0.5174: {'yogurt', 'tropical fruit'} => frozenset({'whole milk'}))
Rule(support 0.0122, confidence 0.5021: {'rolls/buns', 'root vegetables'} => frozenset({'other vegetables'}))
Rule(support 0.0127, confidence 0.5230: {'rolls/buns', 'root vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0145, confidence 0.5630: {'yogurt', 'root vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0223, confidence 0.5129: {'other vegetables', 'yogurt'} => frozenset({'whole milk'}))
========== baseline generate rules ==========
Rule(support 0.0223, confidence 0.5129: {'other vegetables', 'yogurt'} => frozenset({'whole milk'}))
Rule(support 0.0151, confidence 0.5174: {'yogurt', 'tropical fruit'} => frozenset({'whole milk'}))
Rule(support 0.0146, confidence 0.5070: {'other vegetables', 'whipped/sour cream'} => frozenset({'whole milk'}))
Rule(support 0.0145, confidence 0.5630: {'yogurt', 'root vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0135, confidence 0.5175: {'other vegetables', 'pip fruit'} => frozenset({'whole milk'}))
Rule(support 0.0127, confidence 0.5230: {'rolls/buns', 'root vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0123, confidence 0.5845: {'tropical fruit', 'root vegetables'} => frozenset({'other vegetables'}))
Rule(support 0.0123, confidence 0.5525: {'other vegetables', 'domestic eggs'} => frozenset({'whole milk'}))
Rule(support 0.0122, confidence 0.5021: {'rolls/buns', 'root vegetables'} => frozenset({'other vegetables'}))
Rule(support 0.0120, confidence 0.5700: {'tropical fruit', 'root vegetables'} => frozenset({'whole milk'}))
Rule(support 0.0115, confidence 0.5736: {'other vegetables', 'butter'} => frozenset({'whole milk'}))
Rule(support 0.0109, confidence 0.5245: {'yogurt', 'whipped/sour cream'} => frozenset({'whole milk'}))
Rule(support 0.0104, confidence 0.5862: {'citrus fruit', 'root vegetables'} => frozenset({'other vegetables'}))
Rule(support 0.0101, confidence 0.5824: {'curd', 'yogurt'} => frozenset({'whole milk'}))
========== Summary ==========
fp-growth time elapsed: 0.8700008392333984
fp-growth generated frequent itemsets number: 341
baseline time elapsed: 5.682998418807983
baseline generated frequent itemsets number: 341
```