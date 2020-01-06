from django.test import TestCase
from .models import Product

# Create Product tests here.
class ProductTests(TestCase):
    """
    We will define our Product tests
    here that we will test against the Product Models
    """

    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')
        