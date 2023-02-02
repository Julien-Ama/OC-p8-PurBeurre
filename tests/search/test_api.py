import unittest
from unittest.mock import patch

from search.api import Api


# Mock result of GET request API
mock_result = {
    "page": 1,
    "products": [
        {
            "product_name_fr": "Prince",
            "code": "7622210449283",
            "brands": "Lu, Prince, Mondelez",
            "nutriscore_grade": "",
            "url": "https://fr.openfoodfacts.org/"
                   "produit/7622210449283/prince-lu",
            "image_url": "https://static.openfoodfacts.org/"
                         "images/products/762/221/044/9283/"
                         "front_fr.415.400.jpg",
            "image_small_url": "https://static.openfoodfacts.org/"
                               "images/products/762/221/044/9283/"
                               "front_fr.415.200.jpg",
            "categories": "Snacks, Snacks sucrés, Biscuits et gâteaux, "
                          "Biscuits, Biscuits au chocolat",
            "nutriments": {
                "energy_100g": 0.0,
                "sugars_100g": 4.8,
                "sodium_100g": 4.04,
                "fat_100g": 1.6,
                "salt_100g": 0.1,
            },
        },
        {
            "product_name_fr": "Nutella",
            "code": "3017620422003",
            "brands": "Ferrero, Nutella",
            "nutriscore_grade": "e",
            "url": "https://fr.openfoodfacts.org/"
                   "produit/3017620422003/nutella-ferrero",
            "image_url": "https://static.openfoodfacts.org/"
                         "images/products/301/762/042/2003/"
                         "front_fr.248.400.jpg",
            "image_small_url": "https://static.openfoodfacts.org/"
                               "images/products/301/762/042/2003/"
                               "front_fr.248.200.jpg",
            "categories": "Produits à tartiner, Petit-déjeuners, "
                          "Aides culinaires, Produits à tartiner sucrés, "
                          "Aides à la pâtisserie, Pâtes à tartiner, "
                          "Pâtes à tartiner aux noisettes, Pâtes à tartiner "
                          "au chocolat, Pâtes à tartiner aux noisettes et au "
                          "cacao, Aide culinaire sucrée",
            "nutriments": {
                "energy_100g": 0.0,
                "sugars_100g": 56.3,
                "sodium_100g": 0.0428,
                "fat_100g": 30.9,
                "salt_100g": 0.107,
            },
        },
    ],
}

# Mock products list
mock_products_result = [
    {
        "product_name_fr": "Prince",
        "code": "7622210449283",
        "brands": "",
        "nutriscore_grade": "d",
        "url": "https://fr.openfoodfacts.org/produit/7622210449283/prince-lu",
        "image_url": "https://static.openfoodfacts.org/"
                     "images/products/762/221/044/9283/front_fr.415.400.jpg",
        "image_small_url": "https://static.openfoodfacts.org/"
                           "images/products/762/221/044/9283/"
                           "front_fr.415.200.jpg",
        "categories": "Snacks, Snacks sucrés, Biscuits et gâteaux, Biscuits, "
                      "Biscuits au chocolat",
        "nutriments": {
            "energy_100g": 0.0,
            "sugars_100g": 4.8,
            "sodium_100g": 4.04,
            "fat_100g": 1.6,
            "salt_100g": 0.1,
        },
    },
    {
        "product_name_fr": "Nutella",
        "code": "3017620422003",
        "brands": "Ferrero, Nutella",
        "nutriscore_grade": "e",
        "url": "https://fr.openfoodfacts.org/"
               "produit/3017620422003/nutella-ferrero",
        "image_url": "https://static.openfoodfacts.org/"
                     "images/products/301/762/042/2003/front_fr.248.400.jpg",
        "image_small_url": "https://static.openfoodfacts.org/images/products/"
                           "301/762/042/2003/front_fr.248.200.jpg",
        "categories": "Produits à tartiner, Petit-déjeuners, "
                      "Aides culinaires, Produits à tartiner sucrés, "
                      "Aides à la pâtisserie, Pâtes à tartiner, "
                      "Pâtes à tartiner aux noisettes, Pâtes à tartiner au "
                      "chocolat, Pâtes à tartiner aux noisettes et au cacao, "
                      "Aide culinaire sucrée",
        "nutriments": {
            "energy_100g": 0.0,
            "sugars_100g": 56.3,
            "sodium_100g": 0.0428,
            "fat_100g": 30.9,
            "salt_100g": 0.107,
        },
    },
]


class ProductMockResponse:
    def __init__(self):
        self.status_code = 200

    def json(self):
        return mock_result


class TestApi(unittest.TestCase):
    def mock_get_products(self):
        return ProductMockResponse()

    @patch("requests.get", return_value=ProductMockResponse())
    def test_get_products(self, mocked):
        """GIVEN a mock/patch version of requests.get()
        WHEN the HTTP response is successful
        THEN check the HTTP response"""
        api = Api()

        # Get the list of products from the mock result
        expected_products = mock_result.get("products")

        # Compare results
        self.assertEqual(api.products, expected_products)

    def test_avoid_empty(self):
        """GIVEN a mock version of api.products
        WHEN a list of products contain a min of an empty value
        RETURN only products without empty value"""
        api = Api()
        api.products = mock_products_result

        # Get the list of products without empty values
        expected_full_products = [
            {
                "product_name_fr": "Nutella",
                "code": "3017620422003",
                "brands": "Ferrero, Nutella",
                "nutriscore_grade": "e",
                "url": "https://fr.openfoodfacts.org/"
                       "produit/3017620422003/nutella-ferrero",
                "image_url": "https://static.openfoodfacts.org/"
                             "images/products/301/762/042/2003/"
                             "front_fr.248.400.jpg",
                "image_small_url": "https://static.openfoodfacts.org/"
                                   "images/products/301/762/042/2003/"
                                   "front_fr.248.200.jpg",
                "categories": "Produits à tartiner, Petit-déjeuners, "
                              "Aides culinaires, Produits à tartiner sucrés, "
                              "Aides à la pâtisserie, Pâtes à tartiner, "
                              "Pâtes à tartiner aux noisettes, "
                              "Pâtes à tartiner au chocolat, Pâtes à tartiner "
                              "aux noisettes et au cacao, "
                              "Aide culinaire sucrée",
                "nutriments": {
                    "energy_100g": 0.0,
                    "sugars_100g": 56.3,
                    "sodium_100g": 0.0428,
                    "fat_100g": 30.9,
                    "salt_100g": 0.107,
                },
            }
        ]

        # Compare results
        self.assertEqual(api.avoid_empty(), expected_full_products)
