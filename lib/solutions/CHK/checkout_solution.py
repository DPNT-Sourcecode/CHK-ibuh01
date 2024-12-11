
from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    # Check for invalid input
    if not isinstance(skus, str) or not all(c.isalpha() for c in skus):
        return -1   
    
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }

    # check if all items exist in price list
    if not all(item in prices for item in skus):
        return -1
    
    items_counts = Counter(skus)

    # handle E special offers
    if 'E' in items_counts and 'B' in items_counts:
        free_b_count = items_counts['E'] // 2
        items_counts['B'] = max(0, items_counts['B'] - free_b_count)

    total = 0

    for item, count in items_counts.items():
        if item == 'A':
            fives = count // 5
            remaining = count % 5
            total += (fives * 200) + (remaining * prices[item])
        elif item == 'B':
            twos = count // 2
            remaining = count % 2
            total += (twos * 45) + (remaining * prices[item])
        else:
            total += count * prices[item]

    return total
