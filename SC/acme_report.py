from acme import Product
from random import randint, sample, uniform

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for _ in range(0, num_products, 1):
        adj_choice = ADJECTIVES[randint(0, 4)]
        noun_choice = NOUNS[randint(0, 4)]
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = round(uniform(0, 2.5), 1)
        products.append(Product('%s %s'%(str(adj_choice), str(noun_choice)),
            price=price, weight=weight, flammability=flammability))
    return products


def inventory_report(products):
    names = []
    prices = []
    weights = []
    flammabilities = []

    if products == []:
        return 'You have no products'
    else:
        for product in products:
            names.append(product.name)
            prices.append(product.price)
            weights.append(product.weight)
            flammabilities.append(product.flammability)

    unique_names = []
    for name in names:
        if name in unique_names:
            continue
        else:
            unique_names.append(name)

    mean_prices = sum(prices) / len(prices)
    mean_weights = sum(weights) / len(weights)
    mean_flammability = sum(flammabilities) / len(flammabilities)

    print(f'''
    ACME CORPORATION OFFICIAL INVENTORY REPORT
    Unique product names: {len(unique_names)}
    Average price: {mean_prices}
    Average weight: {mean_weights}
    Average flammability: {mean_flammability}
    ''')
    return names, mean_prices, mean_weights, mean_flammability

if __name__ == '__main__':
    inventory_report(generate_products())
