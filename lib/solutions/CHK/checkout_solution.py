

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

    raise NotImplementedError()

