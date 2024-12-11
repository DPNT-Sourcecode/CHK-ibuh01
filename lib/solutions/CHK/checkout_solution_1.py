from collections import Counter


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Check for invalid input
    if not isinstance(skus, str) or not all(c.isalpha() for c in skus):
        return -1

    prices = {"A": 50, "B": 30, "C": 20, "D": 15}

    # check if all items exist in price list
    if not all(item in prices for item in skus):
        return -1

    items_counts = Counter(skus)

    total = 0

    for item, count in items_counts.items():
        if item == "A":
            special_deals = count // 3
            remaining = count % 3
            total += (special_deals * 130) + (remaining * prices[item])
        elif item == "B":
            special_deals = count // 2
            remaining = count % 2
            total += (special_deals * 45) + (remaining * prices[item])
        else:
            total += count * prices[item]

    return total
