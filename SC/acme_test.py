import unittest
from acme import Product
from acme_report import generate_products, inventory_report

legal_names = []
ADJECTIVES = (['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved'])
NOUNS = (['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???'])
for adj in ADJECTIVES:
    for noun in NOUNS:
        legal_names.append('%s %s'%(adj, noun))


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_product_methods(self):
        """Test default product weight being 20."""
        prod = Product('Test Product', 10, 30, .8)
        self.assertEqual(prod.explode(), '...boom!')
        self.assertEqual(prod.stealability(), 'Not so stealable...')


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        """Test check to see if report returns 30 items"""
        names = inventory_report(generate_products())[0]
        self.assertEqual(len(names), 30)

    def test_legal_names(self):
        names = inventory_report(generate_products())[0]
        count = 0
        for name in names:
            if name in legal_names:
                count += 1
            else:
                continue

        self.assertEqual(count, len(names))

if __name__ == '__main__':
    unittest.main()
