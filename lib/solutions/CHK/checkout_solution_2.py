from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    # Check for invalid input
    if not isinstance(skus, str) or not all(c.isalpha() for c in skus):
        return -1

    prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}

    # check if all items exist in price list
    if not all(item in prices for item in skus):
        return -1

    items_counts = Counter(skus)

    # handle E special offers
    if "E" in items_counts and "B" in items_counts:
        free_b_count = items_counts["E"] // 2
        # compare the removed B with the offer of 2B for 45 which is lower?  not possible as 2B only saves 15, so always remove B
        items_counts["B"] = max(0, items_counts["B"] - free_b_count)

    total = 0

    for item, count in items_counts.items():
        if item == "A":
            fives = count // 5
            remainder = count % 5
            threes = remainder // 3
            singles = remainder % 3
            total += (fives * 200) + (threes * 130) + (singles * 50)
        elif item == "B":
            twos = count // 2
            remainder = count % 2
            total += (twos * 45) + (remainder * 30)
        else:
            total += count * prices[item]

    return total
