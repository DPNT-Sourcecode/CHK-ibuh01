

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
    


    # raise NotImplementedError()


