from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string


MIXED_GROUP_OFFER_PRICE = 45
MIXED_GROUP_COUNT = 3

def get_prices():
    return {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
        "G": 20,
        "H": 10,
        "I": 35,
        "J": 60,
        "K": 70,
        "L": 90,
        "M": 15,
        "N": 40,
        "O": 10,
        "P": 50,
        "Q": 30,
        "R": 50,
        "S": 20,
        "T": 20,
        "U": 40,
        "V": 50,
        "W": 20,
        "X": 17,
        "Y": 20,
        "Z": 21,
    }


def apply_free_items(item_counts):
    # could be free for other items or free for self
    rules = [
        ("E", 2, "B", 1),
        ("F", 2, "F", 1),
        ("N", 3, "M", 1),
        ("R", 3, "Q", 1),
        ("U", 3, "U", 1),
    ]

    for buy_item, buy_count, free_item, free_count in rules:
        if buy_item in item_counts:
            applied_free_count = (item_counts[buy_item] // buy_count) * free_count
            if buy_item == free_item:
                applied_free_count = (
                    item_counts[buy_item] // (buy_count + free_count)
                ) * free_count
            item_counts[free_item] = max(0, item_counts[free_item] - applied_free_count)

    return item_counts


def apply_mixed_group_offers(items_counts):
    group_items = ["S", "T", "X", "Y", "Z"]

    available_items = []

    for item in group_items:
        if item in items_counts:
            available_items.extend([item] * items_counts[item])

    prices = get_prices()

    available_items.sort(
        key=lambda x: (-prices[x], x)
    )  # should be consistent in order to compute the remaining items
    groups = len(available_items) // MIXED_GROUP_COUNT
    remaining_items = {}

    for item in available_items[groups * 3 :]:
        remaining_items[item] = remaining_items.get(item, 0) + 1

    print("remaining_items", remaining_items)

    # update items_counts
    for item in group_items:
        if item in items_counts:
            if item in remaining_items:
                items_counts[item] = remaining_items[item]
            else:
                del items_counts[item]

    print("items_counts", items_counts)
    print("groups", groups)
    return groups, items_counts


def calculate_group_offers(item, count):
    group_offers = {
        "A": [(5, 200), (3, 130)],
        "B": [(2, 45)],
        "H": [(10, 80), (5, 45)],
        "K": [(2, 150)],
        "P": [(5, 200)],
        "Q": [(3, 80)],
        "V": [(3, 130), (2, 90)],
    }

    prices = get_prices()

    if item not in group_offers:
        return count * prices[item]

    total = 0
    remaining = count

    for offer_count, offer_price in group_offers[item]:
        groups = remaining // offer_count
        total += groups * offer_price
        remaining = remaining % offer_count

    total += remaining * prices[item]
    return total


def checkout(skus):
    # Check for invalid input
    if not isinstance(skus, str) or not all(c.isalpha() for c in skus):
        return -1

    prices = get_prices()

    # check if all items exist in price list
    if not all(item in prices for item in skus):
        return -1

    items_counts = Counter(skus)
    items_counts = apply_free_items(items_counts)

    # handle mixed group offers
    groups, items_counts = apply_mixed_group_offers(items_counts)

    total = 0
    total += groups * MIXED_GROUP_OFFER_PRICE

    for item, count in items_counts.items():
        total += calculate_group_offers(item, count)
    return total





