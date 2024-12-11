
from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string


def apply_free_items(item_counts):
    # could be free for other items or free for self
    rules = [
        ('E', 2,  'B', 1),
        ('F', 2,  'F', 1),
        ('N', 3,  'M', 1),
        ('R', 3,  'Q', 1),
        ('U', 3,  'U', 1),
    ]

    for buy_item, buy_count, free_item, free_count in rules:
        if buy_item in item_counts:
            free_count = item_counts[buy_item] // buy_count
            if free_item != buy_item:
                item_counts[free_item] = max(0, item_counts[free_item] - free_count)
            else:
                # should be at least pay free_count*buy_count as we are removing the free items
                item_counts[buy_item] = max(item_counts[buy_item] - free_count, free_count*buy_count)
    
    return item_counts



def checkout(skus):

    # Check for invalid input
    if not isinstance(skus, str) or not all(c.isalpha() for c in skus):
        return -1   
    
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10,
        'G': 20,
        'H': 10,
        'I': 35,
        'J': 60,
        'K': 80,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 30,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 90,
        'Y': 10,
        'Z': 50
    }

    # check if all items exist in price list
    if not all(item in prices for item in skus):
        return -1
    
    items_counts = Counter(skus)
    items_counts = apply_free_items(items_counts)

    

    # # handle E special offers
    # if 'E' in items_counts and 'B' in items_counts:
    #     free_b_count = items_counts['E'] // 2
    #     # compare the removed B with the offer of 2B for 45 which is lower?  not possible as 2B only saves 15, so always remove B
    #     items_counts['B'] = max(0, items_counts['B'] - free_b_count)
    

    # # handle F special offers
    # if 'F' in items_counts:
    #     f_count = items_counts['F']
    #     free_f_count = f_count // 3
    #     items_counts['F'] = max(0, items_counts['F'] - free_f_count)

    # total = 0

    # for item, count in items_counts.items():
    #     if item == 'A':
    #         fives = count // 5
    #         remainder = count % 5
    #         threes = remainder //3
    #         singles = remainder % 3
    #         total += (fives * 200) + (threes * 130) + (singles * 50)
    #     elif item == 'B':
    #         twos = count // 2
    #         remainder = count % 2
    #         total += (twos * 45) + (remainder * 30)
    #     else:
    #         total += count * prices[item]

    return total
